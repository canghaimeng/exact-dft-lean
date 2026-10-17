# Mathematical note

`main.tex` is the concise proof; `proof.md` retains the expanded mathematical
argument and source attribution. The accompanying Lean theorem is `Race.bound`
in the repository root. Exact finite checkers are provided under `checkers/`.

Build the paper:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

Run the three finite checks from this directory:

```sh
python3 checkers/check_provider_certificate.py
python3 checkers/check_bridge_geometry.py
python3 checkers/check_schedule_rate_certificate.py
```
