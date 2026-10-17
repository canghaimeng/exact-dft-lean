# Publication relocation: only certificate/report paths and command text changed.
# Mathematical checking logic is unchanged from the accepted proof artifact.
"""Standalone exact checker for the declarative C588AT provider.

Only Python's standard library is used. No Lean, source parser, floating
point, model call, or earlier checker is used. Scalar checking propagates
output covectors backwards, independently of the prior input-column replay.
The report checks finite premises; it is not an Euler proof verdict.
"""

from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import sys


EXPECTED_SHA256 = "b52b8e31dd731c7bdc1fa3e556224ffa51c76dc66ca36849ecec8c85733f9624"
EXPECTED_RANKS = {1: 2568, 2: 492, 3: 280, 4: 232, 5: 56, 6: 56, 8: 92}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def dot(a, b):
    return (a & b).bit_count() % 2


def fraction(pair):
    require(isinstance(pair, list) and len(pair) == 2, "rational encoding")
    require(all(type(x) is int for x in pair) and pair[1] > 0, "rational domain")
    return Fraction(*pair)


def verify(data):
    require(data["schema"] == "c588at-explicit-provider-v1", "schema")
    h, v, slots = data["h"], data["v"], data["slots"]
    require((h, v, slots) == (9, 112, 588), "dimensions")
    n = 2 * v + slots
    frames = data["frames"]
    start, final = data["start"], data["final"]
    require(len(start) == len(final) == n, "state widths")
    require(len(frames) == 1082 and frames[0] == [], "frame table")
    require(len(set(map(tuple, frames))) == len(frames), "unique frames")
    spaces = []
    for index, basis in enumerate(frames):
        require(all(type(x) is int and 0 < x < 2**h for x in basis), "basis range")
        pivots = [x.bit_length() - 1 for x in basis]
        require(pivots == sorted(set(pivots), reverse=True), "pivot order")
        require(all(((x >> p) & 1) == int(j == k)
                    for j, x in enumerate(basis) for k, p in enumerate(pivots)),
                "echelon identity")
        subspace = {0}
        for x in basis:
            subspace |= {y ^ x for y in tuple(subspace)}
        require(len(subspace) == 2 ** len(basis), "basis independence")
        spaces.append(subspace)
    require(all(type(t) is int and 0 <= t < len(frames) for t in start + final),
            "frame references")
    ports, obases = data["ports"], data["orthobases"]
    retained, gauges = data["retained"], data["gauges"]
    require(len(ports) == len(obases) == v and len(retained) == 8, "ports/copies")
    require(all(type(q) is int and 2*v <= q < n and type(t) is int
                and 0 <= t < len(frames) for q, t in retained + gauges),
            "slot references")
    gauged = {q for q, _ in gauges}
    require(len(gauged) == len(gauges) == 228, "gauge count")
    require(gauged == {q for q in range(2*v, n) if start[q] != 0}, "entrance gauges")
    require(all(start[q] == t for q, t in gauges), "entrance references")
    for j, (port, obase) in enumerate(zip(ports, obases)):
        require(type(port) is int and 0 < port < 2**h-1 and dot(port, port) == 1,
                "unit port with zero coordinate")
        require(len(frames[start[j]]) == 1 and port in spaces[start[j]], "input line")
        require(start[v+j] == 0, "zero input Y label")
        require(len(frames[final[j]]) == h, "full output X label")
        require(len(frames[final[v+j]]) == h-1, "output hyperplane dimension")
        require(all(dot(port, x) == 0 for x in spaces[final[v+j]]), "output orthogonality")
        require(len(obase) == h and obase[0] == port, "orthobase width")
        require(all(type(x) is int and 0 <= x < 2**h for x in obase), "orthobase range")
        require(all(dot(x, y) == int(a == b) for a, x in enumerate(obase)
                    for b, y in enumerate(obase)), "orthobase identity")
    require(all(len(frames[t]) == h for t in final[2*v:]), "full output helpers")

    labels = list(start)
    phase_ranks = {}
    adds = {}
    for phase in ("A", "B", "finish"):
        ranks = Counter()
        operations = []
        for gate in data[phase]:
            require(isinstance(gate, list) and len(gate) == 5, "gate encoding")
            kind, frame, register, terms, extras = gate
            require(type(kind) is int and kind in (0, 1), "gate kind")
            require(type(frame) is int and 0 <= frame < len(frames), "gate frame")
            require(kind == 0 or extras == [], "inward gate extras")
            if phase == "finish":
                require(kind == 0 and not terms, "finish is frame-only")
            for q in [register] + [term[0] for term in terms] + extras:
                require(type(q) is int and 0 <= q < n, "gate register")
                previous = labels[q]
                if previous != frame:
                    rank = len(frames[frame]) - len(frames[previous])
                    require(rank > 0 and spaces[previous] <= spaces[frame], "strict nested climb")
                    ranks[rank] += 1
                    labels[q] = frame
            for other, pair in terms:
                coefficient = fraction(pair)
                target, source = (other, register) if kind == 0 else (register, other)
                require(target != source and labels[target] == labels[source], "legal scalar add")
                if phase == "A":
                    require((target >= 2*v and (source < v or source >= 2*v))
                            or (target < v and source < v), "phase A scalar support")
                if phase == "B":
                    require(target >= v or source < v, "phase B X support")
                    require(source < v or source >= 2*v or v <= target < 2*v,
                            "phase B Y-to-helper prohibition")
                operations.append((target, source, coefficient))
        if phase == "A":
            require(all(labels[v+j] == 0 for j in range(v)), "middle Y label")
            require(all(labels[q] == t and len(frames[t]) == 8 for q, t in retained),
                    "retained centre labels")
        phase_ranks[phase] = ranks
        adds[phase] = operations
    require(labels == final, "final label state")
    require(not adds["finish"], "no final scalar operations")
    ranks = sum(phase_ranks.values(), Counter())
    ranks[8] += len(retained)
    require(ranks == Counter(EXPECTED_RANKS), "invocation rank histogram")
    residuals = Counter(h - len(frames[t]) for t in start[2*v:])
    require(residuals == Counter({9:360, 8:140, 7:32, 5:8, 4:48}), "residual histogram")

    rows = data["scatter"]
    require(len(rows) == v, "scatter width")
    scatter = []
    for j, row in enumerate(rows):
        for centre, pair in row:
            require(type(centre) is int and 0 <= centre < len(retained), "scatter centre")
            scatter.append((v+j, retained[centre][0], fraction(pair)))

    # A never reads Y or changes Y. B never sends Y into X or S.
    # J changes only Y from S. Thus all non-Y output rows have zero
    # initial-Y coefficients. It remains to check the Y-Y block below.
    # Check output rows by multiplying covectors by B, J, A in that order.
    chronological = adds["A"] + scatter + adds["B"]
    checks = Counter()
    for output in range(2*v):
        covector = [Fraction(0)] * n
        covector[output] = Fraction(1)
        for target, source, coefficient in reversed(chronological):
            if covector[target]:
                covector[source] += coefficient * covector[target]
        if output < v:
            require(all(x == int(j == output) for j, x in enumerate(covector)),
                    f"X identity row {output}")
            checks["X_rows"] += n
        else:
            t = output - v
            require(all(covector[j] == int(j == t) for j in range(v)), f"Y-from-X row {t}")
            require(all(covector[v+j] == int(j == t) for j in range(v)), f"Y-from-Y row {t}")
            require(all(covector[q] == 0 for q in gauged), f"gauge cancellation row {t}")
            checks["Y_from_X"] += v
            checks["Y_from_Y"] += v
            checks["Y_from_gauged"] += len(gauged)

    return {
        "result": "PASS finite premises only, not a proof-gateway verdict",
        "frames": len(frames), "live_scalar_registers": n, "central_copies": len(retained),
        "phase_rank_counts": {p: dict(sorted(c.items())) for p, c in phase_ranks.items()},
        "scalar_add_counts": {p: len(a) for p, a in adds.items()},
        "invocation_ranks": dict(sorted(ranks.items())),
        "rank_sum": sum(r * count for r, count in ranks.items()),
        "residual_ranks": dict(sorted(residuals.items())),
        "residual_sum": sum(r * count for r, count in residuals.items()),
        "exact_scalar_entries_checked": dict(checks),
        "non_Y_from_Y_entries": "zero by explicitly checked triangular gate support",
        "unproved_here": "complex frame semantics, full 72-call closure and DFT root",
    }


def main():
    root = Path(__file__).resolve().parent
    certificate = Path(sys.argv[1]) if len(sys.argv) > 1 else root.parent / "code/c588at-provider.json"
    (root.parent / ".build").mkdir(exist_ok=True)
    raw = certificate.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    require(digest == EXPECTED_SHA256, "certificate byte binding")
    report = verify(json.loads(raw))
    report.update({"certificate_sha256": digest, "certificate_bytes": len(raw),
                   "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   "command": "python3 checkers/check_provider_certificate.py",
                   "python": platform.python_version(), "platform": platform.platform(),
                   "seed": "none; exhaustive exact rational covector propagation",
                   "utc": datetime.now(timezone.utc).isoformat()})
    (root.parent / ".build/provider-certificate-check.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
