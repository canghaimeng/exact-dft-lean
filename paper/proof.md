# Expanded mathematical proofs

This supplement preserves the ordinary mathematical arguments used by the
accepted proof. It accompanies `main.tex` and `paper.pdf`; it is not a new proof
submission or a publication approval. The source archive SHA-256 is
`70be76665602658491b9fadc2280c6aaac8da3f1cbc7c0d139c831154326e760`.

Editorial changes are limited to section headings, file locations and pointers
to the separately supplied certificate and checkers. Operational submission
history, native metadata and finite-check transcripts are omitted. The
conditional lemmas retain their hypotheses; the main paper supplies those
hypotheses by the preceding concrete construction. Scope cautions in individual
lemmas refer to those lemmas alone.

The full 241357-byte rational certificate is `code/c588at-provider.json`, SHA-256
`b52b8e31dd731c7bdc1fa3e556224ffa51c76dc66ca36849ecec8c85733f9624`.
The complete executable checks are `checkers/check_provider_certificate.py`,
`checkers/check_bridge_geometry.py`, and
`checkers/check_schedule_rate_certificate.py`. They replace the duplicate
embedded programs and encoded copy in the source archive. They use only the
Python standard library. The provider check uses backward rational covectors.
`ATTRIBUTION.md`, `LICENSE` and `NOTICE` preserve source credits and notices.

Within Part A, references to its Appendix A mean Part A.1 below; references to
its Appendix B and C mean the provider checker and JSON certificate above.
Within Part B the invocation premise is Part A and the frame theorem is Part
A.1. Within Part C the standalone arithmetic verifier is the rate checker.
All mathematical text below is extracted from the frozen archive, with only
these pointer adjustments. Finite inequalities remain exact, not floating point.



# A. Local invocation on arbitrary helpers

1. Explicit certificate and local theorem
The complete certificate is the JSON data in code/c588at-provider.json. Its decoded bytes have SHA256
b52b8e31dd731c7bdc1fa3e556224ffa51c76dc66ca36849ecec8c85733f9624
and length 241357. This hash binds the exact data, not a claimed proof.
checkers/check_provider_certificate.py is the complete independent checker. It uses only exact
integer, finite-set and rational arithmetic in Python's standard library.
It neither imports prior checkers nor executes the source declarations.
It propagates output covectors backwards, in contrast with the earlier
forward-input-column experiment. Both the data and checking algorithm
are part of this submission; there is no missing downloaded premise.

There are h=9 binary label coordinates, v=112 ports, R=588 helper slots,
and c=8 additional central copies. Live scalar registers are numbered
X_t=t, Y_t=112+t, S_q=224+q, for 0<=t<112 and 0<=q<588. The copies
are distinct from all 812 live registers and are explicitly initialized.
All live inputs, including every helper input, are arbitrary.

Let d>9 be fixed. An admissible nine-dimensional window means the
following explicit data. In V=F_2^d choose a direct-sum decomposition
    V=A direct_sum E(F_2^9) direct_sum D,
with fixed ordered bases of A and D and an injective linear map E.
Let a=dim A and Q:V->F_2^d be coordinates in the resulting ordered
basis (A first, the nine E coordinates next, D last). This definition
does not assume a nondegenerate ambient dot product on any subspace.

For a listed RREF label U in F_2^9, let its nonzero echelon rows be b_p,
indexed by their pivot coordinates p. Define
    G_U x = x + sum_p x_p(b_p+e_p).
Since b_p+e_p vanishes at every pivot, the added linear map has square
zero. Thus G_U is an involution, sends b_p to e_p, and maps U to its
pivot coordinate space. Let L_U=diag(I_a,G_U,I_{d-a-9}) Q, and let
I_U consist of the first a coordinates and the shifted pivot indices
a+p. With K and P defined in Appendix A, put
    Phi(U)=K_{L_U} P_{I_U} K_{L_U}^{-1}.
It represents the subspace A direct_sum E(U). Write Phi(0) for the
zero label and Phi(H) for H=F_2^9. All these matrices are invertible.
Containment of labels lifts to containment of represented subspaces,
with exactly the same dimension difference. Appendix A therefore
implements every strict label climb using one block of that rank,
and changes representatives of the same subspace using only explicitly
constructible monomial adapters. Every operation is charged there.

For each port let u_t be its listed binary vector and u_t^perp its
standard-dot orthogonal hyperplane in F_2^9. The invocation starts with
data frames Phi(span u_t) on X_t and Phi(0) on Y_t; its data output
frames are Phi(H) on X_t and Phi(u_t^perp) on Y_t. Equivalent chosen
representatives of these same embedded subspaces may replace these
frames using the free-of-recursive-calls adapters from Appendix A.

For helper q let U_q be its listed entrance label and define
    E_q=Phi(U_q),
    F_q=K_{L_{U_q}} P_{I_full} K_{L_{U_q}}^{-1},
where I_full comprises all the first a+9 coordinates. For arbitrary
incoming helper frame Z_q, the outgoing helper frame will be
    F_q E_q^{-1} Z_q.                                 (1)
The helper's scalar value is preserved. The matrix F_q E_q^{-1} is
K_{L_{U_q}} P_{I_full\I_{U_q}} K_{L_{U_q}}^{-1}, so its residual
rank is 9-dim U_q. The residual is an effect of the invocation already
counted below, not an additional paid call here.

The theorem is that on those input/output frames there are two exact
programs, with scalar live-register maps respectively
    (X,Y,S) -> (X,Y+X,S),
    (X,Y,S) -> (X-Y,Y,S).                              (2)
For every replication factor f>=1, each frame is replaced by its f-fold
column tensor product, with spectator bits allowed as in Appendix A.
Both programs use eight initialized copy arrays and exactly the recursive
rank histogram
    n_1=2568, n_2=492, n_3=280, n_4=232,
    n_5=56, n_6=56, n_8=92.                            (3)
A rank r denotes one adapted batch of C^{tensor rf}. All other work,
including scratch initialization/erasure, rational coefficient generation,
monomial adapters, movement and indexing, is O(820*2^{df+b}), and
nonrecursive memory is O(820*2^{df+b}). The constants are fixed finite
functions of the window and certificate, independent of f and b.

2. What the finite checker proves, and why its tests suffice

A gate is [kind,frame,register,terms,extras]. First every register named
by the gate (the register, term registers, extras) moves to the indicated
frame if it is not already there; repeated names do not pay twice.
The checker verifies that each such move is a strict subspace inclusion
and counts its dimension difference. It then executes scalar additions:
kind 0 adds coefficient times register to each term register, in order;
kind 1 adds coefficient times each term register into register, in order.
Every rational coefficient is encoded [integer numerator, positive
integer denominator]. No addition has target=source. The checker verifies
that the two registers of each addition have the identical current label.
Thus each scalar operation is a legal exact pointwise addition between
arrays with equal frames. Tensor replication preserves this property.

There are 1082 distinct, well-formed RREF labels; their independence and
subspace containments are checked by exhaustively constructing their
spans in F_2^9. Port vectors have u_t.u_t=1, are not the all-ones vector,
and the supplied 9-by-9 orthobases have first vector u_t and pairwise
dot products delta_jk. Input X labels are exactly the lines span u_t;
input Y labels are zero. Output X and helper labels have dimension nine,
and output Y labels have dimension eight with every vector orthogonal
to u_t. These facts identify the output labels uniquely as H or u_t^perp.
All helpers with a nonzero entrance label, and only these helpers, form
the explicitly listed set G of 228 gauged slots.

Let A and B now denote the rational 812-by-812 scalar matrices of the
phase-A and phase-B additions; this matrix A is distinct from the
background subspace A of the window. Each is a product of elementary
invertible shears. For clarity we use A_s,B_s for these matrices below.
Let C_s:Q^588->Q^8 select the eight retained helper registers. The data
field retained lists those registers and their common centre labels.
Let J_s:Q^8->Q^112 be the rational scatter matrix in the certificate.
The middle scalar shear is
    J(X,Y,S)=(X,Y+J_s C_s S,S).
It is invertible since it changes only Y and reads only S. Define
    M=B_s J A_s.

The structural phase-A checks say it never changes or reads Y, and that
its X targets read only X. Phase-B checks say X targets read only X,
and no non-Y target reads Y. Therefore, throughout M, no non-Y output
depends on the initial Y. The middle scatter also preserves this property.
The checker then computes every X and Y output row of M exactly. For
row w and an elementary addition I+c e_target e_source^T, multiplication
on the right updates only w_source <- w_source+c w_target. Applying
these row updates in reverse chronological order computes a row of M,
by induction on the number of factors. It is an exact calculation over Q.

The required comparisons establish all X output rows are identity;
the Y-from-X and Y-from-Y blocks are identity; and every coefficient
from a gauged helper into Y is zero. Together with the proved structural
zero blocks, these give the full block description
    M = [ I  0  0 ]
        [ I  I  K ]
        [ L  0  H ],        K[:,G]=0.                 (4)
Since M is invertible, so is H: if Hs=0 then M(0,-Ks,s)=0, which forces
s=0; H is a finite square matrix and hence invertible. The rational
inverse H^{-1} is constructively obtained by Gaussian elimination.

After phase A all Y labels remain zero. Each of the eight retained
helpers has the declared centre label, of dimension eight. The checker
then replays all phase B climbs/additions and the empty finishing phase,
and verifies the exact final label state. Its phase rank counts are
    A: {1:1028, 2:8, 4:56};
    B: {1:1540, 2:484, 3:280, 4:176, 5:56, 6:56, 8:84};
    finish: {}.
There are 1893 and 4631 scalar additions in the two phases.
Adding the eight centre moves gives (3), whose rank sum is 6672.
The entrance residual histogram is
    {9:360, 8:140, 7:32, 5:8, 4:48},
with sum 4816. These are computed from the data, not a manually assumed
price for the resulting program.

The exact local run of Appendix B passed. Its comparison counts are
90944 X-row entries, 12544 Y-from-X entries, 12544 Y-from-Y entries,
and 25536 Y-from-gauged entries. The other initial-Y zero entries follow
from the explicitly checked gate support as proved above. The checker
does not prove the complex semantics by itself; Sections 3--6 supply
that implication. Conversely, the mathematical argument relies on the
full concrete certificate checks, not only its printed rank histogram.

3. Forward scalar correction on arbitrary helpers

Define two rational shears/corrections on live scalars:
    g1(X,Y,S)=(X,Y-KS,S),
    g8(X,Y,S)=(X,Y,H^{-1}(S-LX)).
The second map is an invertible rational linear transformation of X,S
and leaves Y fixed. Equation (4) gives, by direct substitution,
    g8 M g1 (X,Y,S)=(X,Y+X,S).                        (5)
For example, after g1 the Y coordinate is Y-KS; after M it is
(Y-KS)+X+KS=Y+X, while the helper coordinate is LX+HS. The final
correction returns that helper coordinate to S.

The initial correction g1 is legal in the frame model: it reads only
ungauged helpers because K[:,G]=0. Every such helper has entrance label
zero, identical to Y's frame Phi(0). Execute this correction pointwise
on those arrays. After phase B every X and helper is at the same
full-window frame Phi(H). Thus g8 is a pointwise rational matrix on
arrays all carrying that identical frame. It can be executed with a
temporary array for each output, so simultaneous evaluation does not
destroy an input still needed. This is fixed linear overhead and storage,
not a recursive call. Its constants K,L,H^{-1} are generated exactly
from the finite rational matrices, not provided as free arbitrary scalars.

4. How the middle scatter is physically realized

It is generally illegal to perform J directly, since retained helper
arrays have positive-dimensional frames and Y has frame Phi(0).
Instead initialize eight new copy arrays to zero; a zero array can
be regarded as carrying any frame without performing a frame change.
After phase A, copy each selected helper scalar into the corresponding
copy array at its centre frame, by a pointwise assignment/addition
between identical frames. More generally the same construction supports
any retained linear combination of helpers at that exact label; here
each centre selects the explicitly named helper.

Move each copy down from its centre label to zero using the reverse
nested transition of Appendix A, at exactly one rank-eight block.
The copy now equals Phi(0) times its retained scalar. Add the prescribed
scatter coefficients into Y, whose frame is also Phi(0). Phase B and
the final correction act on the live registers, not the copies. Erase
the copies afterward; eight array writes per position are charged.

Tracking scalar coordinates through these operations shows that their
net effect on the live registers is exactly J between A_s and B_s.
No zero assumption was made on a live helper; only the eight explicitly
additional arrays were initialized. Combined with the label climbs and
the corrections this proves (5) in the physical complex-array model.

5. The inverse-transpose scalar shear, at the same price

For an invertible real/rational scalar matrix D, write D^{-T} for the
transpose of its inverse. The operation satisfies (D E)^{-T}=D^{-T}E^{-T}.
For an elementary scalar addition I+c e_t e_s^T with t!=s, its inverse
transpose is I-c e_s e_t^T. Thus replace each scalar addition of phase
A or B by its inverse transpose, in the SAME chronological order, and
keep its original frame visits. Both registers were visited to the same
frame, so the reversed direction and negated coefficient remain legal.
The total scalar matrices of those two phases are A_s^{-T}, B_s^{-T},
with unchanged climb counts. This does not transpose any complex frame
matrix; it only replaces the rational scalar additions.

Replace g1 by g1^{-T} and g8 by g8^{-T}. The former only connects Y
with ungauged helpers, which have identical input frames. The latter
only connects X with full-frame helpers, which have identical output
frames. They remain legal fixed-size rational pointwise operations.

To realize J^{-T}, initialize the eight copies at zero frame, copy
J_s^T Y into them by pointwise operations, move each copy up to its
centre frame at one rank-eight block, and add -C_s^T times the copies
into the corresponding helpers. At this middle point phase A^{-T}
has the same label trajectory and leaves all Y labels at zero; helpers
selected by C_s have exactly the centre labels. Hence every scalar
addition is between identical frames. Erase the copies after phase B.
This gives the live scalar map
    g8^{-T} B_s^{-T} J^{-T} A_s^{-T} g1^{-T}
      = (g8 B_s J A_s g1)^{-T}
      : (X,Y,S) -> (X-Y,Y,S),                          (6)
as required. It uses precisely the same recursive rank histogram (3).

6. Entrance gauges and arbitrary incoming helper frames

For now the canonical route just proved starts helper q at E_q and
ends it at Phi(H). A monomial change of representative, supplied by
Appendix A, changes the latter to F_q: both represent A direct_sum E(H).
It has no recursive cost and all actual operations are charged.

Given an arbitrary incoming helper array Z_q s_q, interpret its initial
canonical scalar coordinate as E_q^{-1} Z_q s_q. This is legitimate
because E_q is invertible. It is semantic interpretation only: the
program does not evaluate a new dense E_q^{-1} array map. The live
data scalar coordinates are unchanged, and both maps (5),(6) ignore
all helper values in their data outputs and preserve each helper's
scalar value. Consequently the outgoing physical helper is exactly
F_q E_q^{-1} Z_q s_q, proving (1). This also works when Z_q is singular,
and indeed for every initial helper array by taking Z_q=I.

As I_{U_q} is contained in I_full, the defining product shows
    F_q E_q^{-1}=K_{L_{U_q}} P_{I_full\I_{U_q}} K_{L_{U_q}}^{-1}.
This is the exact residual kernel factor of rank 9-dim U_q. This
identity, not just the dimension difference, is needed by later helper
bank hosting. The present theorem does not assume that hosting is done.

7. Relation to orthogonal boundary frames

For completeness, the common older boundary convention also fits this
lemma whenever its orthogonal bases are supplied. For an orthogonal
coordinate map G (G^T G=I) and coordinate set S, put
    B(G,S)=product_{j in S}(alpha I+beta X_{G^{-1}e_j}),
where X_z translates binary addresses by z. This is the old tensor
frame on the indicated orthonormal directions. Let
    lambda(x)=D(Gx)/D(x).
The identity D(x+y)=D(x)D(y)(-1)^{x.y}, together with orthogonality,
shows lambda(x+y)=lambda(x)lambda(y). Since lambda(0)=1 and V has
exponent two, lambda(x) is a sign character. Its value on the standard
basis constructs its binary character vector. We have K_G=diag(lambda)
times the plain address permutation G. Conjugating the translation
X_z by this sign diagonal multiplies it by lambda(z).

Therefore T(G,S) is the product of alpha I+lambda(z) beta X_z over
z=G^{-1}e_j, j in S. For lambda(z)=-1,
    alpha I-beta X_z = i X_z(alpha I+beta X_z),
because i beta=alpha and i alpha=-beta. All translations commute, so
    T(G,S)=i^t X_{sum_{lambda(z)=-1} z} B(G,S),
where t is the number of negative factors. This is an explicit monomial
adapter. Part 3 of Appendix A then relates it to every other core
representative of the same subspace. Thus older line/full/hyperplane
boundary frames with supplied orthogonal bases can replace the core
boundary frames without a hidden recursive call. No assertion that an
arbitrary orthogonal partial basis always extends is needed; the present
provider data actually supplies all 112 port orthobases in dimension nine.
The later 73-axis closure must still specify its ambient orthogonal windows.

8. Replication, constants and charged costs

All identities above hold on arbitrary vectors in the active address
space. Replace each frame and adapter by its f-column tensor product.
The scalar additions remain pointwise with the SAME rational coefficients,
since equal frames commute with mixing the role scalars. Each ranked
frame transition replicates into one adapted batch of C^{tensor rf},
not a new sequence of f separately charged recursive blocks. Spectators
are untouched. The phase/rank accounting is therefore exactly (3).

The JSON parsing and all matrix/table construction concern fixed finite
data. Rational matrix multiplication and Gaussian elimination terminate,
using exact equality tests on rationals; pivot existence for H follows
from (4). All coefficients can be prepared from integer constants by
finite exact operations. Their sizes and preparation costs are fixed
independently of f and n; they are included in the big-O constant, not
silently omitted. The frame lemma constructs all Q(i) phase coefficients
and implements monomial addressing by a prefix traversal with linear
total work. No term proportional to f per array entry is introduced.

There are finitely many scalar adds, fixed corrections, adapters and
copies. Every nonrecursive array operation is linear in 2^{df+b}. Fixed
matrix corrections use a fixed number of temporary arrays, counted in
the O(820*2^{df+b}) bound; they can be reused serially. The eight copies
are initialized and erased with charged writes. Offsets and counters
have O(df+b+1) bits. A block can be executed with linear memory by
ordinary in-place tensor butterflies; any later recursive substitution
must charge each fibre and preserve its stated memory bound. Nothing
in this theorem assumes a zero live helper or uncharged scalar oracle.

This completes the exact local invocation theorem. The separate claims
that the 72 invocations close over Q orthogonal classes, that all live
helper banks acquire the final C tensor map, and that the global invoice
has the improved moment are outside this theorem. They must be proved
before it can contribute to a root submission.


# A.1. Complete supporting frame proof

1. Statement, coordinates, and cost convention
Fix an integer d>=2. All binary vector and matrix operations in this proof
are over F_2. Let V=F_2^d with coordinates numbered 0,...,d-1, standard dot
product x.y=sum_j x_j y_j in F_2, and Hamming weight |x| as an ordinary
integer. Write D(x)=i^{|x|}. In exponents of (-1), a binary scalar is read
as 0 or 1. All complex coefficients below lie in Q(i).

Put alpha=(1+i)/2, beta=(1-i)/2 and
    C = [[alpha,beta],[beta,alpha]].
Let X exchange the two coordinates. Direct multiplication gives
C^2=X, C^4=I, and C^{-1}=X C. For S a subset of {0,...,d-1}, P_S denotes
the tensor product that applies C on every coordinate in S and I on every
other coordinate. Thus P_empty=I, P_all=C^{tensor d}, and
P_T=P_{T\S} P_S when S is contained in T.

An invertible binary d-by-d matrix G is a coordinate map on V. Define
    K_G(x,y) = 1_{Gx=y} D(x)/D(y),
    U(G,S) = {x in V : (Gx)_j=0 for j outside S},
    T(G,S) = K_G P_S K_{G^{-1}}.
The matrix convention is (A v)(x)=sum_y A(x,y)v(y).
K_G is an invertible monomial matrix: (K_G v)(x)=D(x)/D(Gx) v(Gx),
and K_G K_{G^{-1}}=I. All these assertions follow by substituting into
the displayed formula; each row has exactly one nonzero entry.

We prove:
(a) If U(G,S)=U(H,R), an explicitly computable invertible monomial A with
    nonzero entries in {1,-1,i,-i} satisfies T(H,R)=A T(G,S).
(b) If U(G,S) is strictly contained in U(H,R) and the dimension difference
    is r, 0<r<d, the transition from T(G,S) to T(H,R), or the reverse
    transition, is a product of monomial adapters and exactly one P_J
    with |J|=r. A same-dimensional containment costs adapters alone.
(c) Under f-fold column replication, with f>=1 and 0<=b<d spectator bits,
    each transition in (b) uses one adapted block
          I_{2^{(d-r)f+b}} tensor C^{tensor(rf)}.
    Here one adapted block means a batch on all complementary fibres;
    it is not a claim that all fibres cost one length-2^{rf} evaluation.
    Every operation apart from that block, including initial preparation,
    indexing, movement and adapters, costs O(2^{df+b}). Serial storage
    is O(2^{df+b}); addresses have O(df+b+1) bits. Constants in these
    bounds may depend on the fixed d and the fixed finite frame data,
    but not on f or b. This is the unit-cost logarithmic-word exact
    arithmetic/index model of the root, not a bit-operation estimate.

In particular, if an array represents T(G,S) z for arbitrary complex z,
the transition produces T(H,R) z. These are matrix identities; no initial
zeros or restriction on z is used. They continue to hold on multiplying
both sides on the right by any other matrix Z, invertible or not.

2. Entry formula

For u=x+y, P_S(x,y) vanishes unless u is supported in S. On that support,
each matching coordinate contributes alpha and each differing coordinate
contributes beta=-i alpha, so
    P_S(x,y)=alpha^{|S|} (-i)^{|u|}.
For binary vectors,
    D(x+y)=D(x)D(y)(-1)^{x.y}.
Equivalently, with y=x+u,
    D(x)/D(y) (-1)^{x.u}=D(u)^{-1}=(-i)^{|u|}.
Substitution into K_G P_S K_{G^{-1}} therefore gives

    T(G,S)(x,y) =
      1_{x+y in U(G,S)} alpha^{|S|}
      D(x)/D(y) (-1)^{(Gx).(G(x+y))}.                 (1)

This formula includes S=empty. It also proves invertibility directly
from the defining product. All divisions in these formulas are by fourth
roots of unity; they can be replaced by products of at most three such
factors. No unknown complex scalar has to be tested for equality to zero.

3. Explicit change of representative

Suppose U=U(G,S)=U(H,R). Because the coordinate maps are bijective,
|S|=dim U=|R|. For j in S define v_j=G^{-1}e_j; these v_j form a basis
of U. Define the binary linear map p and then F by

    p(x)=sum_{j in S} ((Gx)_j + (Hx).(H v_j)) v_j,
    F(x)=x+p(x).                                      (2)

In particular p(x) belongs to U. For every u in U, expand
u=sum_{j in S}(Gu)_j v_j. It follows term by term from (2) that

    (G p(x)).(Gu) = (Gx).(Gu) + (Hx).(Hu),
    (G F(x)).(Gu) = (Hx).(Hu).                        (3)

F is invertible. Indeed, if F(x)=0 then x=p(x) belongs to U. Equation
(3) says (Hx).(Hu)=0 for every u in U. Since H maps U bijectively onto
the coordinate subspace supported in R, taking Hu=e_j for j in R
shows that every coordinate of Hx in R is zero. Its other coordinates
are already zero since x is in U. Hence Hx=0, so x=0. Thus the binary
linear endomorphism F has zero kernel and is bijective on the finite V.

Set
    a(x)=D(x)/D(F(x)) (-1)^{(G F(x)).(G p(x))},
    A(x,z)=1_{F(x)=z} a(x).                           (4)
This is an explicitly invertible monomial matrix. Its inverse maps
v to the array x -> a(F^{-1}x)^{-1} v(F^{-1}x), and all factors a(x)
are in {1,-1,i,-i}.

We claim T(H,R)=A T(G,S). To check entry (x,y), set u=x+y. Because
p(x) belongs to U, the support conditions u in U and F(x)+y in U
are equivalent. If either fails, both entries are zero. Otherwise
F(x)+y=u+p(x), and (3) gives
    (G F(x)).(G(F(x)+y))
      = (Hx).(Hu) + (G F(x)).(G p(x)).
Multiplying (1) at (F(x),y) by (4), the two copies of the second
binary term cancel in the exponent of (-1). The D(F(x)) factors
cancel as well. What remains is
    alpha^{|S|} D(x)/D(y) (-1)^{(Hx).(H(x+y))},
which is (1) for (H,R), since |S|=|R|. This proves (a), with no
nondegeneracy requirement on U relative to the ambient standard dot
product. The nondegenerate form used in the injectivity proof was
the coordinate form induced by H on U, which is always nondegenerate.

4. Containment and the single paid block

Let U=U(G,S) be contained in V'=U(H,R). Choose a basis of U, extend
it to a basis of V', then to a basis of V. These choices can be made
deterministically by binary Gaussian elimination followed by testing
standard coordinate vectors in their fixed order. Let B be the
coordinate map in the resulting basis. Let I={0,...,dim U-1} and
J={0,...,dim V'-1}. Then U=U(B,I), V'=U(B,J), and I is contained
in J. Part 3 constructs monomial matrices A_U,A_V satisfying
    T(B,I)=A_U T(G,S),
    T(H,R)=A_V T(B,J).
By multiplying the defining products and cancelling K_B^{-1} K_B,
    T(B,J)=K_B P_{J\I} K_B^{-1} T(B,I).
Consequently
    T(H,R)=A_V K_B P_{J\I} K_B^{-1} A_U T(G,S).      (5)
This has one block on r=|J\I| coordinates; everything else is monomial.

For the downward transition invert the matrix multiplying T(G,S) in
(5). The inverse of P_{J\I} is X_{J\I} P_{J\I}, where X_{J\I}
flips exactly those coordinates, since C^{-1}=X C. Therefore the
reverse transition also contains only one forward P_{J\I} block,
with additional monomial factors. If r=0, U=V' and part 3 alone
applies. This proves (b), including upward and downward moves.

5. Replication and arbitrary additional right factors

For f columns, identify the active binary address space with V^f.
Replication of a d-bit matrix M means M^{tensor f}, on those columns.
All identities in (3)--(5) tensor across columns. The tensor product
of monomial matrices is monomial, with its address map applied in
each column and its nonzero coefficient the product of the column
coefficients. The tensor product P_{J\I}^{tensor f} applies C on
the r selected bits of each column. A fixed bit-coordinate permutation
collects the rf selected bits and the (d-r)f unselected bits. With b
additional bits left unchanged, it is exactly the adapted block in
part (c). The same argument covers the downward transition.

For clarity, frames are a semantic way of tracking a computation, not
instructions to initialize an array by a dense T matrix. A maintained
physical array already equals its current frame applied to its scalar
data. Equation (5) changes that frame by executing the displayed
adapters and block. Multiplying (5) on the right by arbitrary Z proves
the same transformation for data of the form Z z. This is the exact
identity needed when a live helper carries unrelated, arbitrary data.
It does not itself establish the scalar cancellation of a provider.

6. Charged construction and implementation

The input frame description is fixed finite binary data G,H,S,R.
Their inverses, an adapted basis B, F,F^{-1}, and formulas (2),(4)
can all be obtained by a terminating sequence of binary arithmetic
and Gaussian elimination. All choices use the fixed coordinate order.
One may prepare explicit tables on V for each resulting monomial
address map and its coefficient. There are only 2^d entries per table,
and all coefficients are among four named rational-complex units.
Preparation takes a finite constant depending on d and the frame
data. This constant is charged, not declared free; since f>=1 and d
is fixed it is absorbed in the constant of O(2^{df+b}). No oracle,
nonconstructive source search, or variable-precision numerical routine
is required. The only kernel constants are alpha,beta, also prepared
by a fixed number of exact operations from 1 and i.

Here is an explicit linear-work implementation of a replicated
monomial M, which avoids recomputing f separate column contributions
at every output address. Order each column as a base-2^d digit and
enumerate the f-column addresses by a depth-first traversal of the
complete 2^d-ary prefix tree. A node carries its input address prefix,
its image prefix, and the product of the phase coefficients so far.
An edge appends one digit c and its precomputed image F(c), updating
each prefix by a shift of d bits and an addition, and multiplies the
phase by the precomputed coefficient a(c). At a leaf, read the input
entry at the completed image address and write its scaled value to
the completed output address. For b spectators repeat this traversal
for each spectator value. Thus v_new(x)=a_f(x)v_old(F_f(x)) exactly.

The number of nodes of a B-ary tree with B^f leaves is
(B^{f+1}-1)/(B-1), where B=2^d>=4. It is at most a fixed multiple of
the number of leaves. Each edge and leaf uses bounded many exact
arithmetic, word-index and data-movement operations. Phase products
can be maintained either as fourth-root units or as exponents modulo
4. They use constant space per node. Storage for the traversal stack
is O(f) logarithmic words, while source and destination arrays take
O(2^{df+b}) entries. Allocate a separate destination buffer and swap
the buffer roles; this avoids any hidden in-place permutation work.
Initializing or resetting that buffer is charged linear work.

The bit regrouping for the adapted block is also linear work. In a
similar prefix traversal, maintain a selected-bit prefix and an
unselected-bit prefix, appending the precomputed r-bit and (d-r)-bit
pieces of each d-bit digit. At each leaf concatenate those prefixes
and the spectator prefix to obtain the regrouped address. All shifts
are by fixed d,r or by a precomputed O(df+b)-bit word offset, and
every node uses bounded many word operations. The number of nodes
again is O(2^{df+b}). This proves both packing and unpacking bounds.
The regrouped block performs the length-2^{rf} kernel separately on
each complementary fibre. Whatever algorithm is later substituted
for that kernel must be charged for each fibre; no work of it is
included among the linear adapters established here.

All intermediate array addresses are less than a fixed multiple of
2^{df+b}, and all loop counters, offsets and depth counters need
O(df+b+1) bits. Computing f-dependent offsets and masks takes at
most O(df+b+1) word operations, also within the linear bound. A
constant number of successive adapters can reuse two buffers and
one stack. Nonrecursive storage is therefore O(2^{df+b}); the kernel
workspace, if any, is a separate charged item of the recursive
algorithm. For this lemma alone, ordinary in-place C butterflies on
the selected bits implement the block with constant temporary storage;
their arithmetic is the charged block work, not linear adapter work.
Thus the complete transition has a linear-memory implementation.
Substituting a linear-memory recursive kernel preserves this bound.
Sequential composition introduces no unaccounted parallel multiplier.

This proves the stated charged frame lemma. It contains no assertion
that a 72-invocation network closes, that its live-role count or call
invoice is valid, or that any root DFT exponent has been established.


# B. Global 73-axis closure

1. Precise invocation premise and notation
Let C=alpha I+beta X, alpha=(1+i)/2, beta=(1-i)/2, so C^2=X. For a
coordinate subset S of F_2^d let P_S apply C on S and the identity on
the other coordinates of arrays indexed by F_2^d. For invertible G set
  K_G(x,y)=1_{Gx=y} i^(|x|-|y|),
  T(G,S)=K_G P_S K_G^{-1}.
K_G and its inverse are explicit monomial matrices over Q(i). The
admitted frame theorem supplies an explicit monomial left adapter
between any two such T representing the same subspace G^{-1}F_2^S.
Between nested represented subspaces with dimension difference r it
supplies one adapted C^{tensor r} block in either direction, with only
monomial work besides that block. For f copies of the coordinate system
and b spectator bits this becomes one adapted C^{tensor rf} batch;
all other work, preparation, indexing and movement is O(2^(df+b)),
with O(2^(df+b)) memory and O(df+b+1)-bit addresses. Here and below
"one adapted batch" means the transform on each of the independent
lines of that width, not one transform of only 2^(rf) of the entries.

The separate local invocation premise has 112 ports with specified
vectors u_t and orthonormal bases B_t of F_2^9, first column u_t, and
588 live helper slots q. Its entrance labels U_q have residuals
  r_q=9-dim U_q,
with multiplicities {9:360,8:140,7:32,5:8,4:48}. Each invocation has
eight additional initialized central copy arrays. It works for arbitrary
live data, including all 588 helper arrays.

In any fixed direct-sum window V=A direct_sum E(F_2^9) direct_sum D,
with ordered coordinates, it starts the port X_t in a representative
of A+E(span u_t), and Y_t in a representative of A. It ends X_t in a
representative of A+E(F_2^9), and Y_t in one of A+E(u_t^perp).
There are two available scalar effects on the underlying array values:
  F: (x_t,y_t) -> (x_t,y_t+x_t),
  B: (x_t,y_t) -> (x_t-y_t,y_t).
Every helper's underlying value is unchanged. If its incoming physical
frame is any invertible Z_q, its outgoing frame is W_q Z_q, where
  W_q = C_q P_{R_q} C'_q,
C_q,C'_q are explicit invertible monomial matrices and |R_q|=r_q.
In the local proof C_q=K_{L_{U_q}} and C'_q=C_q^{-1}; the background
coordinates cancel, so R_q consists exactly of the nonpivot window
coordinates. Changes to chosen equivalent data representatives are
included among the nonrecursive adapters. Both orientations have
the same exact recursive profile
  h={1:2568,2:492,3:280,4:232,5:56,6:56,8:92}.
For f-fold columns every listed rank r means rf, without multiplying
the number of invocation copies or changing rational scalar gates.
Initialization/erasure of the eight extra arrays and all nonrecursive
work are charged and linear in the complete array length.

This is the full local interface used below. In particular the helper
residual is the effect of an already counted invocation; it is NOT an
additional recursively paid block, and it never assumes zero live data.

2. Finite class stock and common data frames

Use the 73-coordinate space
  V=H direct_sum E_0 direct_sum ... direct_sum E_7,
where H=F_2^9 has coordinates 0,...,8, and each E_c has coordinates
(c,j), 1<=j<=8. Numerically (c,j) is coordinate 9+8c+j-1. Write
H'={1,...,8}, p=0, and R_{<k}=E_0 union ... union E_{k-1}, with
R_{<0}=empty. These names also denote their coordinate subspaces.

Let Gamma={g in F_2^(73 by 73):g^T g=I} and Q=|Gamma|. This is a
nonempty explicitly finite set: enumerate all binary 73 by 73 matrices,
retain exactly those satisfying the displayed equality, in lexicographic
order. Such a g has inverse g^T. This prescription, not an oracle for
an unspecified finite object, defines Q and every class index.

For each port t put D_t=diag(B_t,I_64), and B_{g,t}=g D_t. It is
orthogonal. Define the data frame on coordinate set S by
  F_{g,t}(S)=T(B_{g,t}^{-1},S).
Thus it represents B_{g,t} span(S). There are eight separate replicas
rho=0,...,7. For each (rho,g,t) there are four pairs (X_j,Y_j), j=1,...,4.
Initially each X_j is assigned frame F_{g,t}({p}) and each Y_j frame I.
This is an invariant, not an actual initialization transform: for any
physical X input there is a unique abstract x with X=F({p})x. The
algorithm does not execute F({p})^{-1}. All inputs remain arbitrary.

There are also 4824 live helper banks for each g, initially in frame I,
and eight distinct central copies for each g. Hence the live stock is
  W=Q(8*4*2*112+4824)=Q*11992.
The explicitly initialized central-copy stock is 8Q arrays; these are
reused throughout the 72 sub-stages. They are not included in W or
treated as arbitrary live data. Ordinary serial adapter buffers and
local scalar work storage are charged separately in Section 8.

3. Nine invocation stages and the port-dependent class permutation

For stage k=0,...,8 and invocation class d in Gamma choose
  A=d span(R_{<k}), E(v)=d(v,0), D=d span(E_k union ... union E_7).
The three subspaces form the required direct sum. Use their ordered
coordinate basis (A first, H next, D last). The background dimension
is a=8k, and the nine-dimensional local window is always admissible.

At stage zero, data class (g,t) is served by invocation d=g. At stage
k>=1, put c=k-1 and let Pi_c exchange H coordinate j with (c,j) for
1<=j<=8, fixing p and all other coordinates. Set
  R_{t,k}=D_t Pi_c D_t^{-1},  d=g R_{t,k}.
For k=0 set R_{t,0}=I. Each R is orthogonal and an involution. Thus
g -> d is a permutation of Gamma for each fixed port t. Consequently
the Q invocations of one stage use every relevant data role exactly
once, although their port-to-class permutation depends on t. The lookup
tables are fixed and can be generated by finite binary matrix arithmetic.

Here are all data-frame identifications, proved directly in the class
basis B=B_{g,t}. At k=0 the input coordinate sets are {p} and empty,
and the output sets are H and H'. For k>=1,
  B^{-1} d = Pi_{k-1} D_t^{-1}.
Since D_t^{-1}u_t=e_p and D_t^{-1}(u_t^perp)=span(H'), it follows that
the input sets, for X and Y respectively, are
  H union R_{<k-1},       H' union R_{<k-1},
and the output sets are
  H union R_{<k},         H' union R_{<k}.
For example Pi sends the background row E_{k-1} to H', leaves the
earlier background rows fixed, sends the port line to p, and sends
the local port hyperplane H' to row E_{k-1}. This proves each assertion
on the explicitly specified basis generators. It holds for every g
by multiplication on the left by g; no enumeration of Gamma is used
as an experimental substitute for this universal identity.

Before and after each invocation use the admitted same-subspace
monomial adapters to choose these common F_{g,t} representatives.
These adapters preserve the abstract scalar values. The invocation
therefore realizes F or B on the class's scalar pair while advancing
its X and Y coordinate sets by eight dimensions. These wrappers use
no additional recursive blocks. For all f the identities tensor across
columns and retain the identical scalar map on arrays.

For shorthand let
  X[k]=H union R_{<k},  Y[k]=H' union R_{<k},  0<=k<=8.
An active pair exits stage k in F(X[k]),F(Y[k]). The input of stage
k>=1 is the preceding stage's output. The endpoints are X[8]=V and
Y[8]=V\{p}.

4. One run: four pairs, nine invocations, and all extra climbs

Fix a replica rho and data class (g,t); omit these subscripts in this
section. Run stage 0 forward on pair 1, then stage 1 backward on pair 1.
For j=2,3,4 in order perform the following actions:

  (a) Move the initially idle pair j to frames X[2j-3],Y[2j-3].
      Each move is nested and has rank 16(j-1): respectively 16,32,48.
  (b) At those equal pair frames do X_{j-1}+=X_j and Y_j-=Y_{j-1}.
  (c) Run stage 2j-2 forward on pair j-1.
  (d) Move pair j up by rank 8 on each side to X[2j-2],Y[2j-2].
  (e) Do Y_j+=Y_{j-1} and X_{j-1}-=X_j at equal frames.
  (f) Run stage 2j-1 backward on pair j.

After j=4, run stage 8 forward on pair 4. Finish each pair in common
frames F(V),F(V\{p}), using one nested move on each side of pair 1
of rank 48, of pair 2 of rank 32, and of pair 3 of rank 16. Pair 4
requires no final move. All these differences are strictly between
zero and 73. Finally, for j=4,3,2 in decreasing order, do
  Y_{j-1}-=Y_j,  X_j+=X_{j-1}.
The X gates connect equal F(V) frames and the Y gates connect equal
F(V\{p}) frames. Every other addition above also connects explicitly
equal frames, so it is an ordinary pointwise addition, not a hidden
transform.

This description gives the invocation list
  (stage,pair,orientation) =
  (0,1,F),(1,1,B),(2,1,F),(3,2,B),(4,2,F),
  (5,3,B),(6,3,F),(7,4,B),(8,4,F).
All Q invocation classes are executed at each stage with the permutation
in Section 3. Thus this is nine invocations per class per run.

For completeness the scalar calculation is given explicitly. Write
x_j,y_j for the initial abstract values. Just before the final decreasing
j gates, repeated substitutions in (a)--(f) and stages 0,1,8 give
  X_1=-y_1,               Y_1=x_1+x_2,
  X_2=y_1-y_2,            Y_2=x_2+x_3,
  X_3=-y_1+y_2-y_3,       Y_3=x_3+x_4,
  X_4=y_1-y_2+y_3-y_4,    Y_4=x_4.
The j=4 gate changes X_4 to -y_4 and Y_3 to x_3; j=3 changes X_3
to -y_3 and Y_2 to x_2; j=2 changes X_2 to -y_2 and Y_1 to x_1.
Thus the run's scalar map on every pair is exactly
  (x_j,y_j) -> (-y_j,x_j).
Each helper's scalar value is unchanged by every invocation and every
extra operation. Central copies are separate initialized storage and
may be reset between invocations. No scalar input on a live bank is
set to zero or discarded.

The non-invocation recursive price per port and run is therefore
  6 phi(8)+4 phi(16)+4 phi(32)+4 phi(48).
It follows from the explicit list of nested moves, not from subtracting
histograms in another construction. Across eight runs it is
  48 phi(8)+32 phi(16)+32 phi(32)+32 phi(48),
as required.

5. Turning the final data frames into the common full tensor

For each class write K=K_{B^{-1}}, F(S)=K P_S K^{-1}, L={p},
and Lc=V\L. The full-space case of the admitted adapter theorem gives
an explicitly constructible monomial N with
  N F(V)=P_V=C^{tensor 73}.
Moreover C^2=X implies
  F(V)F(L)=J F(Lc),  J=K X_p K^{-1},
and J is a monomial matrix. Hence
  N J F(Lc)=C^{tensor 73} F(L).
These are identities of matrices, not estimates. After the scalar
calculation, apply N to every X array and N J to every Y array, and
replace each physical pair (X,Y) by (Y,-X). Its outputs become
  C^{tensor 73} F(L)x_j,  C^{tensor 73} y_j,
exactly C^{tensor 73} times its original arbitrary physical inputs.
For f-fold columns use N^{tensor f} and J^{tensor f}. Their product
remains monomial, and the identical calculation gives C^{tensor 73f}.
Spectator bits are untouched. No initial frame inverse is executed.
This explicitly supplies the final permutations and phases even though
the intermediate old source frames are not our chosen representatives.

6. Residual-bank hosting on arbitrary inputs

The following elementary construction handles any finite schedule with
bank loads at most 73. A bank after some stages has frame
  Z=A P_U,
where A is a recorded invertible monomial and U a coordinate subset.
Initially A=I,U=empty. Suppose its next invocation residual is
  W=C P_R C',  |R|=r,
where C,C' are explicit monomials, and |U|+r<=73. Choose T to be the
first r unused coordinates, so T is disjoint from U. Choose the
coordinate permutation sigma taking the sorted elements of T to the
sorted elements of R, and the sorted complements to one another.
Let M_sigma be its address permutation, with
  P_R M_sigma=M_sigma P_T.
This identity follows by permuting tensor factors; the direction of
sigma is fixed by sigma(T)=R.

Before the invocation apply the monomial
  P=(C')^{-1} M_sigma A^{-1}
to the bank. The invocation then leaves frame
  W P Z
   =C P_R C' (C')^{-1} M_sigma A^{-1} A P_U
   =C M_sigma P_T P_U
   =(C M_sigma) P_{T union U}.
Thus replace A by C M_sigma and U by T union U. The bank's abstract
value has remained exactly unchanged. The choice of the next adapter
does not depend on that value. For an unused bank do nothing. The
pre-adapter is a charged monomial operation; it is not a paid recursive
block. The W effect is already contained in the invocation invoice.

At the end, if |U|=73 apply A^{-1}, obtaining P_V. Otherwise apply
A^{-1} and one coordinate batch P_{V\U}, of rank 73-|U|. Provided
1<=|U|, this rank is strictly less than 73. Because P_{V\U}P_U=P_V,
every bank now contains the full tensor of its original arbitrary
input. All identities also hold for f-fold columns. In particular this
construction requires no joint diagonalization of residuals from
different windows and no uncharged application of a dense frame inverse.
Only the explicitly monomial A,C,C' are inverted in the algorithm.

Here is the concrete schedule, with stage index k=9rho+l from 0 to 71.
List the 588 slots in groups by increasing slot index within residual
size, and use the following groups of sizes (9,8,7,5,4):
  30 copies of (6,1,1,0,1),
  18 copies of (5,3,0,0,1),
   3 copies of (7,0,0,2,0),
   1 copy   of (6,0,2,1,0),
   7 copies of (1,8,0,0,0),
   7 copies of (8,0,0,0,0),
   1 copy   of (0,0,0,1,0).
This gives 67 groups and uses every slot exactly once. If slot q is
at position j of group a, assign it at stage k to bank
  72a+((k+j) mod 72).
There are 4824 banks. Each group has fewer than 72 slots, so assignments
are injective at a fixed stage. Over the 72 stages, each bank of group
a gets every slot of that group once. Fifty-nine groups have load 73,
seven have load 72, and one has load 5. The pad histogram is consequently
  {0:4248,1:504,68:72}.
Partial loads cannot exceed final loads since all r_q are positive.
Thus every step in the explicit hosting procedure is valid, and every
bank has positive load. This is also precisely the independently
admitted finite schedule. Repeat it separately for each g; invocation
d always uses banks indexed by d, irrespective of its data-class
permutations. Across replicas all banks retain their running frames;
the padding is done only once, after stage 71.

7. Exact global invoice and the role count

All eight replicas execute the nine-stage run. There are 72 local
invocations per g, all using the same proved C588AT profile h. The
extra data climbs are 112 copies of the eight-run price in Section 4.
The only extra helper calls are 504 at rank 1 and 72 at rank 68.
The resulting rank counts per g are exactly
  n_1=72*2568+504=185400,
  n_2=72*492=35424,
  n_3=72*280=20160,
  n_4=72*232=16704,
  n_5=72*56=4032,
  n_6=72*56=4032,
  n_8=72*92+112*48=12000,
  n_16=n_32=n_48=112*32=3584,
  n_68=72.
Every other count is zero, and every rank lies in 1,...,72. Their rank
sum is 872856=73*11992-2560. Multiply every count by Q for the actual
program. Its W=Q*11992 live inputs all receive C^{tensor 73f} by
Sections 5 and 6. Central copies are 8Q additional initialized arrays,
not a subtraction from this arbitrary-input requirement.

For clarity, the normalized moment of this actual program is
  (1/(Q*11992)) sum_r Q n_r (r/73)^(1-a)
   =(1/11992) sum_r n_r (r/73)^(1-a).
The factor Q cancels exactly, without power-of-two padding or an
unproved elimination of physical roles. Part C proves
that at a=1261/1000000 this is <999989/1000000<1. This text's network
result is still distinct from the subsequent recurrence and Fourier
transfer, which require their own admitted hypotheses and root proof.

8. Constructive coefficients, charged preparation, indexing and storage

Everything specifying the finite program is determined by finite
algorithms: binary enumeration of Gamma, binary matrix products for
R_{t,k}, RREF/coordinate calculations for window representatives,
the explicit same-subspace adapter formula, the group schedule and
the sorted-complement coordinate permutation above, and the exact
rational provider corrections. The local theorem proves that its
rational correction matrices exist and gives Gaussian elimination as
their generation algorithm. No real-number search, external oracle,
existence-only printer, unspecified root, or bit-multiplication bound
is used. Table generation is counted. Its possibly enormous cost is
a fixed finite constant independent of f,b and all eventual DFT lengths.

Let N=2^(73f+b), 0<=b<73. Each finite monomial on the base address
space has a table for its input address permutation and Q(i) phase.
The table is fixed once; the f-fold operation is implemented by column
prefix traversal, carrying the mapped input and output prefixes and
the accumulated phase. The complete fixed-base branching tree has
O(N) nodes, and leaf traversal includes all spectators. It avoids
recomputing all f column maps at each leaf. The charged frame theorem
already proves the linear bound for this traversal, preparation,
movement and packing/unpacking of each recursive batch, including
the O(73f+b+1)-bit address bound. A composition of a fixed number of
its adapters is still O(N). Precompute compositions when convenient;
none of the matrices T(G,S) used as invariants is evaluated densely.

Role permutations and pair gates cost O(WN): Gamma multiplication
tables have a fixed finite size, each visited role index carries only
a fixed additive address length, and each pointwise addition traverses
its array once. All rational coefficients are prepared by the fixed
finite procedure and used as exact Q(i) values. For each invocation
its eight central arrays are explicitly initialized/reset in O(8N).
Store eight per g and reuse them between all 72 sub-stages. Serial
monomial moves can use one additional length-N output buffer; pointwise
finite correction maps can use a fixed number of scalar temporaries,
or a fixed finite number of length-N buffers. The local theorem and
the frame theorem give a fixed finite bound on these extra buffers.
They are workspace, are all charged, and are not falsely claimed as
arbitrary live roles. If S denotes 8Q plus that fixed buffer bound,
total nonrecursive work and serial memory are O((W+S)N), with S
independent of f and b. In particular these are O(WN) with a fixed
constant, since W and Q are fixed positive integers.

All recursive operations are precisely the adapted batches in
Section 7. There is no call of width 73f or greater. All temporary
initialization and final discard is permissible private storage in
the admitted initialized-workspace recurrence; live helper inputs
remain arbitrary and their full tensor outputs are retained. This
completes the constructive global realization from the stated local
invocation premise with the original charged model intact.


# C. Finite bank schedule and rational moment

## Statement

Suppose a set Q of 588 slots has residual weights with multiplicities
360 of 9, 140 of 8, 32 of 7, 8 of 5, and 48 of 4. There are 72 injective
maps from Q to a set of 4824 banks and integer paddings p_b such that
the total residual load of bank b over the 72 maps, plus p_b, is 73.
The padding multiset consists of 4248 zeros, 504 ones, and 72 copies of 68.

Let m=73, W=11992, a=1261/1000000, and let the nonzero call counts n_r be

| r | n_r |
|---:|---:|
|1|185400|
|2|35424|
|3|20160|
|4|16704|
|5|4032|
|6|4032|
|8|12000|
|16|3584|
|32|3584|
|48|3584|
|68|72|

Then

    Psi = sum_r (n_r/W) (r/m)^(1-a) < 999989/1000000 < 1,

and

    1/800 < 20099/16000000 < 63/50000 < 1261/1000000.

All powers here are positive real powers. The lemma specifies a schedule
and proves a real inequality for the displayed list; it does not identify
that list with the cost of any unproved circuit.

## Schedule proof

Partition the slots into groups according to the table below. The five
middle columns count slots of the indicated weights within one group.
Slots within each weight class may be taken in any fixed order.

| number of groups | 9 | 8 | 7 | 5 | 4 | group load |
|---:|---:|---:|---:|---:|---:|---:|
|30|6|1|1|0|1|73|
|18|5|3|0|0|1|73|
|3|7|0|0|2|0|73|
|1|6|0|2|1|0|73|
|7|1|8|0|0|0|73|
|7|8|0|0|0|0|72|
|1|0|0|0|1|0|5|

The weighted column sums are exactly (360,140,32,8,48), so every slot
is used once. There are 67 nonempty groups, each with at most nine slots.
Index the groups by g=0,...,66 and their slots by j=0,...,s_g-1.
Use banks (g,t), where t=0,...,71; their number is 67*72=4824.
At stage k=0,...,71 send slot j of group g to (g,(k+j) mod 72).
For fixed k this is injective: different groups have different first
coordinates, and distinct j in a group differ by less than 72.

For a fixed group g, bank (g,t), and slot j, there is exactly one
stage k with k+j=t mod 72. Thus each bank in group g receives every
slot of that group once, and its total load is the group load L_g.
Put p_(g,t)=73-L_g. There are 59 groups of load 73, seven of load 72,
and one of load 5. Their 72-fold replication gives respectively
4248 pads of 0, 504 pads of 1, and 72 pads of 68. All pads are in
[0,73), and load+pad=73, as required. Relabelling the slots transfers
this construction to any set Q with the stated multiplicities.

## Exact real-inequality proof

For 1<=t<=2 set z=(t-1)/(t+1). The derivative identity
2/(1-z^2)=2 sum_(j>=0) z^(2j), integrated from zero to z, gives

    log t = 2 sum_(j>=0) z^(2j+1)/(2j+1).

The series is nonnegative and z<=1/3. Hence, writing

    L(t)=2 sum_(j=0,...,39) z^(2j+1)/(2j+1),
    H(t)=L(t)+2*z^81/(81*(1-z^2)),

we have L(t)<=log t<=H(t). The tail bound follows by replacing each
denominator 2j+1, j>=40, by 81 and summing a geometric series.
For each rank r write 73/r=2^s t with s a nonnegative integer and
1<=t<2. Then log(73/r)<=s H(2)+H(t).

The following entirely rational upper bounds satisfy
s H(2)+H(t)<=u_r/10^9:

| r | u_r |
|---:|---:|
|1|4290459442|
|2|3597312261|
|3|3191847153|
|4|2904165081|
|5|2681021529|
|6|2498699972|
|8|2211017900|
|16|1517870719|
|32|824723539|
|48|419258431|
|68|70951736|

Define x_r=a*u_r/10^9. Each is nonnegative and less than 3. For any
0<=x<3, the exponential series and j!>=2*3^(j-2) for j>=2 give

    exp(x) <= E(x) := 1+x+x^2/(2*(1-x/3)).

Since the exponential is increasing,

    Psi = sum_r (r*n_r)/(73*11992) exp(a log(73/r))
        <= R := sum_r (r*n_r)/(73*11992) E(x_r).

R is a specified rational number. Exact arithmetic gives

    R < 999989/1000000.

The supplied standalone rate verifier checks both the logarithm table and this
last rational comparison using only integer arithmetic through Fraction.
No floating-point approximation is used. It also checks the schedule,
the tally sum r*n_r=73*11992-2560, and every comparison in the statement.
Its positive result, together with the analytic inequalities just proved,
establishes the strict moment inequality.


# D. Amplification with initialized private workspace

STATEMENT AND DEFINITIONS
Let C=1/2 [[1+i,1-i],[1-i,1+i]], and C^{tensor 0}=(1). Fix integers
m>=2, W>=1, S>=0 and n_r>=0 for 1<=r<m, and a rational a in (0,1).
Put alpha=1-a. Suppose a fixed, constructively specified family of linear
array programs P(f,b), f>=1, 0<=b<m, has the following contract. Here
k=mf+b.

1. There are W live arrays, each of length 2^k. Every entry in every live
   array is arbitrary, independently of all others, including any live
   array that the construction calls a helper bank. The program computes
   I_(2^b) tensor C^{tensor mf} on each of these W arrays. The choice of
   which b binary axes are spectators is fixed and explicitly indexed.

2. The program may use S additional arrays of length 2^k, initially zero,
   and any constant-factor additional temporary storage covered by its
   memory bound. These are distinct from the W live inputs. Their final
   values are unconstrained and may be discarded. Their initialization,
   address organization and all writes are charged. No zero premise is
   made about any of the W live inputs or about the values presented to
   a recursive call during the program.

3. Apart from its explicitly adapted calls, P uses only prepared Q(i)
   scalars, input-linear field operations, and deterministic integer and
   array operations. All scalar preparation, schedule construction,
   adaptations, initialization, indexing and nonrecursive operations cost
   at most A(W+S)2^k, with A fixed independently of f,b,k. Its serial
   memory is at most B(W+S)2^k complex/word cells, for a fixed B, and
   its addresses have O(k+1) bits.

4. The exact recursive invoice has n_r calls of type r. Such a call
   applies C^{tensor rf} to the 2^(k-rf) fibers of one length-2^k array,
   possibly in an explicitly changed binary coordinate system. Its
   preparation and the packing/unpacking needed to expose those fibers
   are included in item 3. All fibers have arbitrary current values.
   Inverse/correction/copy operations requiring recursive transforms are
   already included in these counts with justified adaptations. There
   are no unpriced recursive operations. The type-r call itself may act
   on one of the initialized scratch arrays after it has acquired data.

If

    Psi=(1/W) sum_{r=1}^{m-1} n_r (r/m)^alpha < 1,          (1)

then a single deterministic exact algorithm computes C^{tensor k} for
every integer k>=0 in O(2^k(k+1)^alpha) charged operations. It uses
O(2^k) serial memory and O(k+1)-bit integer addresses. The operations on
variable data are linear, scalar preparation is charged, and all
constants implicit in the bounds may depend on the fixed data of this
lemma, including W,S,m,a and the specified program, but not on k.

The relevant model is exact complex arithmetic with unrestricted
coefficients and logarithmic integer words, not finite precision or bit
multiplication. Divisions are confined to legal scalar preparation with
nonzero denominators. The only nonrational constant needed is i.

PROOF

1. Elementary base algorithm.

One factor C on a selected binary axis is evaluated by its displayed
two-by-two formula on disjoint coordinate pairs. The four scalar
coefficients are fixed Q(i) numbers and can be prepared in constant
work. A nested block/pair loop visits each pair in constant work.
Therefore p binary factors on an array of length 2^p take at most
B_0(p+1)2^p charged operations for an absolute B_0, and O(2^p) memory.
The same assertion holds fiberwise. This requires no assumption that
any initial input entry vanishes. For dimension zero the map is identity.

2. Recursive simultaneous algorithm on W arbitrary arrays.

We construct B(k), which transforms all W input arrays by C^{tensor k}.
For k<m, use the elementary algorithm on each array. This is a fixed
base range.

For k>=m, set f=floor(k/m) and b=k-mf. Apply the b spectator factors
directly to all W live arrays. Their cost is O(W m 2^k)=O(W2^k), since
m is fixed. Then run P(f,b), initializing its extra workspace as
required. These transformations compose to C^{tensor k} on every live
array, because tensor factors on disjoint axes commute.

It remains to implement each type-r call without assuming a divisibility
condition on W. Put p=rf and M=2^(k-p), the number of its fibers. After
the charged adaptation, arrange the fibers contiguously. Divide them
into q=floor(M/W) complete groups of W fibers and u=M-Wq leftovers,
where 0<=u<W. For every full group invoke B(p) on these W arbitrary
fibers. Allocate and initialize B(p)'s own workspace separately; neither
the other parent arrays nor any unrelated parent fiber is treated as
initialized scratch. On each of the u leftover fibers use the
elementary p-factor algorithm. Finally undo the charged adaptation.

Every child dimension p satisfies 1<=p<=((m-1)/m)k<k, so this is a
well-founded, explicitly specified recursive algorithm. Its correctness
follows by strong induction. In particular, when a type-r call acts on
a parent scratch array containing nonzero data, the induction applies
to that arbitrary data exactly as it does to an original live input.
The induction never calls the parent network on fewer than W inputs
or assumes that any member of a complete group is initially zero.

At the end of B(k), the W designated outputs have the required values.
Discard the extra scratch arrays. If a zero-on-return scratch convention
is desired, overwrite those additional cells with zero before returning;
this adds O((W+S)2^k) work and does not touch live outputs. The algorithm
does not promise to restore arbitrary initial contents in the explicitly
additional scratch arrays, because no such contents were supplied as
inputs in its contract.

3. Charged recurrence and its normalization.

Let T(k) bound the full cost of B(k), including allocation/initialization
of its own scratch, all adapters and array movements. Bookkeeping for a
batch loop costs O(M) per call, which is O(2^k); n_r,m,W,S are fixed.
Passing a fiber offset, iterating contiguous groups, or packing a group
into a recursive buffer costs at most O(2^k) per parent call. This is
absorbed in a constant A_0. The elementary leftover cost for p>=1 is
at most B_1 u p 2^p, increasing B_1 to absorb p+1 and fixed loop work.
Consequently for k>=m,

 T(k) <= A_0(W+S)2^k
       + sum_r n_r [floor(2^(k-rf)/W) T(rf)
                    + B_1(W-1)rf 2^(rf)].               (2)

All nonrecursive overhead in (2) is an upper bound, not an assertion
that initialized workspace is free. Define t(k)=T(k)/(W2^k). Since
q W<=2^(k-rf), a complete-batch term is bounded by

    q T(rf)/(W2^k) <= t(rf)/W.

Since k-rf=(m-r)f+b>=f and f 2^(-f)<=1 for every integer f>=1,

    rf 2^(rf-k)<=r f 2^(-f)<=r.

Thus every leftover contribution, after division by W2^k, is bounded
by a constant independent of k. Equation (2) yields

    t(k)<=A_1+(1/W)sum_r n_r t(r floor(k/m)),              (3)

where one possible A_1 is

    A_0(1+S/W)+B_1((W-1)/W)sum_r r n_r.

The extra initialized workspace changes this constant; it does not
alter the moment in (1). Only the W independently transformed live
inputs appear in the denominator of the recursive normalized work.
Every recursive operation on scratch remains in n_r in the numerator.

4. Strict-contraction induction, with the floor handled correctly.

For positive k we prove t(k)<=K k^alpha. Choose K large enough to cover
1<=k<m, and also so that K m^alpha(1-Psi)>=A_1. Such a finite K exists
because alpha>0 and Psi<1. For k>=m, every child is positive and smaller
than k. The induction hypothesis and rf<=rk/m give

    t(k)<=A_1+(K/W)sum_r n_r (rf)^alpha
         <=A_1+K k^alpha Psi
         <=K k^alpha.

The last step uses k>=m and the choice of K. The case k=0 is a separate
constant-cost base case. Therefore

    T(k)=O(W2^k(k+1)^alpha).                              (4)

We deliberately did not use the generally false inequality
rf+1 <= (r/m)(k+1). The positive-child induction is on k^alpha; the
globally convenient (k+1)^alpha notation is used only after the proof.

5. Serial memory, addresses and preparation.

Invoke full groups one at a time. At dimension k, retain the parent
live arrays, its scratch and a constant number of movement buffers.
They occupy O((W+S)2^k) cells. The active child has dimension at most
beta k, where beta=(m-1)/m<1. Along a recursion path the dimensions
strictly decrease as integers; hence the sum of the array lengths is
at most sum_{j=0}^k 2^j<2^(k+1). The total simultaneous storage is
O((W+S)2^k)=O(2^k). Offsets and fixed finite-role identifiers are
O(k+1)-bit integers, with constants depending only on the fixed program.
Even an explicit stack with O(k) frames and O(k) words per frame has
O(k^2) cells, bounded by O(2^k), and its actual work is charged in
the program/loop costs above. A depth-first implementation uses much
less stack, but that improvement is unnecessary here.

No scalar table is free: its construction is included at every parent
level in A_0(W+S)2^k, and at each recursive child in T(p). The same holds
for coordinate changes and inverse packing. The only number-theoretic
computations required in this recursive scheme itself are division of
k by the fixed m, computation of powers of two, division of M by fixed
W, offsets and loop counters. Their words have O(k+1) bits. The assumed
adapted-call indexing guarantee is not replaced by an uncharged scan
of all k coordinates for each array entry.

For reference, a common way to discharge that guarantee in a concrete
network is to regard each m-bit column as one digit of radix 2^m.
An explicitly fixed table describes a column coordinate change. A
depth-first traversal updates source/destination address contributions
in constant word work per prefix edge. A prefix tree with radix at
least two has fewer than twice as many nodes as leaves; the complete
array permutation is O(2^k), including any fixed b spectator bits.
This observation is not an additional hypothesis that an arbitrary
unexamined network automatically satisfies; its tables must be supplied.

6. A single input array.

To compute C^{tensor k} on one input, allocate W-1 additional live
arrays, initialize them to zero in O(W2^k) charged work, and call B(k).
Its arbitrary-live-input contract applies, and the designated output
is correct. Discard all other arrays. Since W is fixed, (4) is
O(2^k(k+1)^alpha), with O(2^k) memory and O(k+1)-bit addresses. This
completes the theorem.

WHY THIS DOES NOT ASSUME AWAY A LIVE AUXILIARY ROLE

Every one of the W live arrays, including helper banks used to gain the
finite saving, must be transformed from arbitrary data. A construction
whose helper bank works only at zero cannot count that bank among those
W arbitrary inputs. Conversely an explicitly additional scratch register
may be initialized, but its initialization, field operations and recursive
calls must be counted and its storage allocated at each relevant level.
The theorem therefore does not take a clean-scratch identity and
silently treat all of its auxiliary coordinates as recursive live output
stock. Its input and workspace distinction is stated before the
recurrence and is respected in each recursive group.

A common finite multiplicity Q can be retained rather than discarded:
if W=Q W_0 and n_r=Q c_r, then

    (1/W)sum_r n_r(r/m)^alpha
      =(1/W_0)sum_r c_r(r/m)^alpha.

The initialized workspace count S may also depend on this fixed Q; its
contribution is included in A_1 and the memory constant. Q and its tables
must have a fixed terminating construction with charged finite cost.
No exponent is imported from a bit-complexity statement.


# E. Complete charged tensor-to-Fourier transfer

## Statement and model
Write

    C = (1/2) [[1+i, 1-i], [1-i, 1+i]],
    zeta_d = exp(2 pi i/d),   F_d = (zeta_d^(jk))_(0<=j,k<d).

Fix a rational a with 0<a<1 and put alpha=1-a. Suppose there is a single
deterministic algorithm A which computes C^{tensor k} on arbitrary complex
input for every integer k>=0, in at most K 2^k(k+1)^alpha operations.
This bound includes its preparation of Q(i) coefficients, construction of
its schedule, indexing, and data movement. Its integer addresses have
O(k+1) bits. Here, as in the model of the parent obligation, operations on
the input vector are additions, subtractions, and multiplication by
prepared input-independent scalars; divisions occur only in scalar
preparation and have nonzero denominators. The program and its integer
schedule are uniform, rather than uncharged advice depending on k.

Then a single deterministic exact algorithm computes F_n for every n>=1
with total charged cost

    O(n (log n)^alpha (log log n)^(4-alpha))
      = O(n (log n)^(1-a) (log log n)^(3+a))                 (1)

as n tends to infinity. Its sole supplied root is zeta_{D_*}, for an
explicit positive integer D_*<1024 n^3. All additional scalar preparation
and integer work are charged. A fixed number of O(log(n+2))-bit words
suffices for every integer or address. There are no complex zero tests or
conjugations of input-dependent values. Consequently, for every fixed
rational 0<delta<a the cost is O(n(log n)^(1-delta)). In particular this
holds conditionally for a=1261/1000000 and delta=63/50000, whose difference
is 1/1000000.

As usual, an asymptotic bound describes the same algorithm at every
positive length; finitely many initial lengths can use the direct formula.
One can replace log n and log log n in all globally stated bounds by
1+log(n+2) and 1+log log(n+3), respectively.

The model counts exact field operations and integer operations/random
access on logarithmic words at unit cost. Complex magnitudes and precision
are unrestricted. The specified root is one unit-cost supplied value.
Nothing in the proof is an integer bit-multiplication or floating-point
claim.

## 1. Local Fourier compilation on exactly the original coordinates

We first construct, for every r>=1 and every primitive r-th root u, a word
for F_r(u)=(u^(ij)) consisting of O(1+log^4 r) slots. A slot is either an
invertible monomial matrix or disjoint forward copies of C on ordered
pairs, with identity on the unused singletons. All widths use a common
repeating slot pattern. Its scalar programs and schedule have polynomial
preparation cost in r, with an absolute exponent. Besides u and i they
require only power-of-two roots of order less than 8r. No extra coordinate
is present in the resulting word.

### 1.1 A triangular factorization

For r=1 the assertion is immediate. For r>1 let column k of P be the
coefficient vector of the monic polynomial product_{j=0}^{k-1}(Z-u^j).
Thus P is unit upper triangular. N=F_r(u)P is lower triangular, since its
entry (i,k) is that polynomial evaluated at u^i. Define

    H_0=1, H_j=product_{s=1}^j(1-u^s), 0<j<r.

Every H_j is nonzero by primitivity. For i>=k,

    N_ik=(-1)^k u^(k(k-1)/2) H_i/H_(i-k).

Hence N=diag(H_i) T diag((-1)^k u^(k(k-1)/2)), where T is the lower
triangular Toeplitz matrix with sequence h_j=1/H_j and diagonal 1. All its
diagonal factors are invertible and are prepared by polynomially many
field operations, using only nonzero denominators.

Let D_N=diag(N_kk) and L=N D_N^(-1). Then F_r=L D_N P^(-1) is a
unit-lower/diagonal/unit-upper factorization. Such a factorization is
unique: comparison puts a unit lower triangular matrix equal to an upper
triangular matrix, so it is identity, after which the diagonal and upper
factors agree. Since F_r is symmetric, transposition and uniqueness give
P^(-1)=L^T. Therefore

    F_r(u)=N D_N^(-1) N^T.                                 (2)

It remains to compile an invertible triangular Toeplitz matrix on its own
coordinates. Transposition will preserve the required layer types.

### 1.2 Linear convolution graphs

Convolution of variable data with a fixed vector, when their operand
lengths sum to v, has a linear arithmetic directed acyclic graph (DAG)
with O(v log(2+v)) gates, O(log(2+v)) depth, fan-in at most two, and absolute
bounded fan-out, including output uses. Zero extension is permitted inside
this auxiliary DAG; it will not add coordinates to the final word.

For completeness, pad to the least power of two L at least the full
product length. At L-th roots, a convolution is pointwise multiplication
of the transforms, followed by the inverse transform. The transform of
the fixed vector is prepared and used as scalars. Recursively split a
Fourier transform into even and odd input indices and combine pairs by
(b,c)->(b+omega c,b-omega c). This recursion has O(L log L) scalar gates
and O(log L) levels, with bounded fan-out. The inverse uses inverse roots
and scaling by 1/L. Indeed the sum of all L-th roots raised to an integer
t is L if L divides t, and zero otherwise, by the finite geometric-sum
identity. Reversing indices, selecting distinct outputs, composing a
fixed number of these DAGs, and summing a fixed number of branches preserve
the displayed bounds and bounded fan-out. Output scalings and sums count
as gates; an output itself is one designated source/gate read or zero.
The topology is printed before evaluating coefficients; even a gate with
a vanishing coefficient is retained.

### 1.3 Replay using arbitrary, restored borrowed coordinates

Suppose a linear map M:C^e->C^b has such a DAG, with g gates, depth H,
fan-in <=2 and fan-out <=d including outputs. On disjoint coordinate sets
x,y,z of sizes e,b,g we can implement

    (x,y,z) -> (x,y+Mx,z)                                  (3)

by at most 8g+2b shears, in O((d+1)(H+1)) layers of disjoint pairs. The
initial values in z can be arbitrary and correlated with all other data.

Assign coordinate z_v to each gate v. In topological order add the gate's
linear combination into z_v instead of overwriting z_v. Each gate takes
at most two shears. The forward sweep is z->U z+T x, with U unit lower
triangular. Write the output reads as F z+D x. When initial z is zero this
is the original computation, so F T+D=M.

Run this sweep, add its output reads into y, and undo the sweep. This
restores z and adds Mx+FUz to y. Run a second sweep with every direct edge
from x omitted, subtract the output FUz (omitting D x), and undo again.
The terms depending on initial z cancel exactly. The target y is never a
predecessor in either sweep. This proves (3) as a polynomial identity in
independent x,y,z and hence also for correlated starting values.

For the depth bound, assign gates their longest-path levels. At one level
the shear edges form an undirected multigraph of maximum degree at most
max(2,d): destinations are new gates, while predecessors are sources or
earlier gates. A greedy edge coloring uses at most 2 max(2,d)-1 colors,
because an edge meets at most twice the maximum degree minus two other
edges. A color is a disjoint-pair layer. No destination is a predecessor
at that level, so the reordering is valid. The output round has bounded
degree as well. Reverse sweeps reverse these layers and negate shear
coefficients. Four sweeps and two output rounds prove the claimed bounds.

### 1.4 Exact-width Toeplitz compilation

Write T_v=(h_(i-j)) for 0<=j<=i<v, zero above the diagonal, with h_0!=0.
The inverse sequence is prepared using

    g_0=1/h_0,
    g_k=-(1/h_0) sum_{j=1}^k h_j g_(k-j).

These coefficients invert every smaller triangular Toeplitz block; the
identity follows by equating coefficients in the product of the two
truncated power series. For v>1 split at p=floor(v/2). With the natural
lower-left block B,

    T_v = [[I,0],[E,I]] diag(T_p,T_(v-p)),    E=B T_p^(-1),
    E_ij=sum_{nu=j}^{p-1} h_(i-nu) g_(nu-j), p<=i<v, 0<=j<p.       (4)

The diagonal transforms run on their disjoint child intervals. We now
implement the cross update on the same v coordinates.

Partition the source and target intervals into consecutive chunks. For a
chunk M of size b by e, let J_b,J_e be the lower shift matrices. At an
entry away from the first local row and column, telescoping (4) gives

    E_ij-E_(i-1,j-1)=-h_(i-p) g_(p-j).

Thus D=M-J_b M J_e^T is a sum of three explicitly available outer
products. The first extends this last outer product to the entire chunk.
If R is the remainder, it is supported on the first row and column, and
equals

    e_0 R_(0,*) + (R_(*,0)-R_00 e_0) e_0^T.

We keep all three terms, even if one is zero; there is no rank test.
Nilpotence of shifts gives

    M=sum_{l>=0} J_b^l D (J_e^T)^l.                         (5)

For an outer product v w^T in D, its contribution applied to x is found
by two convolutions with zero extension:

    b_l=sum_{j=l}^{e-1} w_(j-l) x_j,  0<=l<e,
    c_i=sum_{l=0}^{e-1} v_(i-l) b_l, 0<=i<b.

The first is the coefficient at e-1-l of w convolved with the reversal
of x; the second is a truncated ordinary convolution. Three branches and
their output sum therefore give a printed DAG with absolute constants
K_0,K_1,d_0 such that

    g<=K_0(b+e)log_2(2+b+e),
    H<=K_1 log_2(2+b+e),    fan-out<=d_0.                   (6)

We choose chunk size by an entirely discrete algorithm. Try each
integer s=1,...,v; partition both intervals into chunks of length s, except
possibly the last; print every resulting chunk DAG and count gates.
Declare s admissible iff g+b+e<=v for every pair. Choose the largest
admissible s. If none exists, implement the whole T_v directly: visit rows
in decreasing order, scale the current coordinate by h_0, and add h_(i-j)
times each lower-index coordinate j<i. The latter still has its original
value. Width one is just the scaling h_0. Thus the algorithm is effective
even without knowing the constants in (6).

To bound its depth, fix for analysis an absolute D>=16K_0+16. For all
sufficiently large v, s_0=floor(v/(D log_2 v)) is at least
v/(2D log_2 v)>=1. Its chunk sizes satisfy b+e<=2v/(D log_2 v)<=v/8 and,
by (6), g<=4K_0 v/D<=v/4. Therefore s_0 is admissible. Direct fallback
occurs only for bounded v, and the chosen s leaves O(log v) chunks on
each side. For each of O(log^2 v) pairs, reserve its b+e source/target
coordinates and borrow g other coordinates from this same parent block.
They exist by the fit test. Apply (3), in O(1+log v) layers, and restore
every borrowed value before handling the next pair. A borrowed coordinate
may carry any other source or already updated target; this is allowed by
the arbitrary-state identity (3). All source chunks for the cross update
are unchanged at the end of each pair. The cross updates therefore add
exactly E times the transformed first interval.

The cross stage has O(1+log^3 v) layers. The two child words run in
parallel. Allowing a mixed round which, on disjoint regions, performs
monomial or shear layers, its depth satisfies

    d(v)<=max(d(floor(v/2)),d(ceil(v/2)))+O(1+log^3 v).

Summing over balanced recursion levels gives O(1+log^4 r). Split every
mixed round into a monomial layer and a shear layer, at constant cost.

All preparation is polynomial in r. The inverse sequence, entries in
(4), and three outer products require polynomial scalar work; only h_0
is a Toeplitz denominator. There are fewer than 2r recursion nodes. At a
node of width v, testing at most v chunk sizes and v^2 pairs per size,
and printing O(v log(2+v)) gates per pair, is polynomial integer work.
Levels, edge colorings and available borrowed coordinates are found by
finite scans of these lists. Only chosen graphs need coefficient
evaluation. Keep shared scalar programs as DAGs, not expanded expression
trees. The FFT lengths in the two convolutions are powers of two below
4r, so the single root of order 2^ceil(log_2(4r))<8r supplies them all.
Their fixed-vector transforms and inverse scaling cost polynomial work.
Compiler indices and gate-list addresses have O(log(r+2)) bits.

Apply this construction to T in section 1.1. Equation (2), the diagonal
factors of N, and the transposed word for N^T give F_r on exactly r
coordinates. Transposition reverses factor order and preserves monomial
and disjoint shear layers. The previous bounds and nonzero-denominator
guarantees are preserved.

### 1.5 Compiling every shear into forward C slots

Put A=(1+i)/2, S=diag(1,i), and H=[[1,1],[1,-1]]. Direct multiplication
shows H=A^(-1) S C S and

    H diag(2,1) H diag(-3,1) H = [[-8,-10],[0,-6]] = K.

For nonzero t define D_t=diag(4t/5,1). Then

    [[1,t],[0,1]]=D_t diag(-1/8,-1/6) K D_t^(-1).          (7)

This uses exactly three forward C factors and invertible diagonals. An
update y<-y+t x uses the ordered pair (y,x).

No test for a possibly zero shear coefficient mu is needed. Prepare
kappa=1+mu conjugate(mu), t_1=kappa, t_2=mu-kappa. If s=|mu|, then
1+s^2>s, since s^2-s+1=(s-1/2)^2+3/4>0. Hence both t_1 and t_2 are
nonzero. Their two upper shears compose to the mu shear. Formula (7)
gives exactly six forward C factors in the same slot pattern for every
mu, including zero.

All such conjugates are prepared scalars. Evaluate a second copy of the
coefficient's arithmetic DAG with every root replaced by its inverse,
and rational literals unchanged, including i replaced by -i. This gives
the complex conjugate. Every denominator is the conjugate of a proved
nonzero denominator. No variable input is conjugated and no zero test is
performed. Shared subexpressions remain shared. Preparing conjugates and
the constant-length replacements increases polynomial local preparation
by a constant factor.

Use these replacements in parallel on disjoint pairs. An unused
coordinate is a singleton identity at every C slot. Put each earlier
layer into a monomial round followed by a shear round, using identity
for the unused type, and replace the shear round by this fixed six-C
pattern. Idle rounds consist of identity monomials and singleton-only C
slots. All local words now have the same repeating pattern and can be
padded to O(1+log^4 r_max) slots for any collection of widths <=r_max.
This proves the local compiler stated at the start of section 1.

## 2. Synchronization with linear total indexing work

Let r_1,...,r_l>=2 and R=product r_j. Mixed-radix digits have their first
axis most significant. A recursive traversal of the digit tuples visits

    sum_{j=0}^l product_{i=1}^j r_i
       <=R sum_{j=0}^l 2^(j-l)<2R                         (8)

nodes. Use a depth-first stack, updating a constant number of states per
edge and restoring them on return, never copying a whole prefix. Thus a
constant-work prefix update costs O(R) over all tuples.

For a tensor monomial, store on each axis its digit permutation pi_j and
coefficient c_j. Extend the original and permuted addresses by
multiply-and-add, and the running coefficient by multiplication with
c_j. At each leaf move and scale the value. Equation (8) charges O(R)
operations, including all running scalar products, rather than O(R l).

For a tensor C slot, each axis has ordered pair blocks and singleton
blocks. Give those blocks any fixed order. A chosen block on axis j has
size q_j in {1,2}, p_j coordinates in preceding blocks, and local within-
block digit t_j; its actual coordinate a_j is tabulated. A sector chooses
one block per axis. Its width Q=product q_j=2^k, and its action is exactly
C^{tensor k}. Order sectors by block choices and coordinates within a
sector by their t_j digits. Let tau_j=product_{i>j}r_i. The start address
of the chosen sector is

    S=sum_{j=1}^l (product_{i<j}q_i) p_j tau_j.             (9)

To prove this, classify all earlier sectors by their first differing
axis. At that axis j their total width is p_j, the fixed earlier choices
contribute product_{i<j}q_i, and all later choices contribute tau_j.
These classes are disjoint and exhaust the preceding packed coordinates.

During digit traversal initialize S=0,Q=1,o=0,I=0 and extend by a_j via

    S<-S+Q p_j tau_j, Q<-Q q_j,
    o<-o q_j+t_j,    I<-I r_j+a_j.

At a leaf its packed address is S+o and original address I. This prints
the packing and its inverse in O(R) work by (8). Traverse block choices
instead to list sector starts, sizes and pair counts k. At each depth
the number of block prefixes is at most the number of digit prefixes
because the number of blocks on each axis is <=r_j. This remains true
when an axis has just one block. The total listing cost is O(R).

Apply section 1 to all F_(r_j) and pad to a common sequence of
O((1+log r_max)^4) slots. For a slot take the tensor product of the axis
matrices. Products of slots give the desired tensor product because
(tensor_j A_j)(tensor_j B_j)=tensor_j(A_j B_j). Local words were proved
as matrix identities on arbitrary states. Thus intervening operations
on other axes do not need to preserve the values borrowed by a local
word; the tensor-product identity already proves the synchronized word.

A monomial slot costs O(R). At a C slot invoke the assumed algorithm A
on each packed sector. Since k<=l and the sector widths sum to R, all
calls, including their own preparation and movements, cost at most

    K sum_sectors 2^k(k+1)^alpha <= K R(l+1)^alpha.

Packing, unpacking and listing sectors cost another O(R). Calls on
different sectors are sequential, so their address spaces can be reused;
offsetting their addresses costs constant work per access and uses
O(log(R+2)) bits. Their specified address bound and cost allow at most a
fixed polynomial in R total address range, even if the tensor subroutine
uses sparse addresses.

The local compilers, suffix products and tables have cost polynomial in
l,r_max,log(R+2). All other scalar products were charged to traversal.
We have proved the bound

    O(R(l+1)^alpha (1+log r_max)^4)
       +poly(l,r_max,log(R+2))                             (10)

for tensor_j F_(r_j), including every required coefficient and schedule.
The implicit constants may depend on the fixed assumed algorithm and a;
the preparation polynomial's degree is absolute.

## 3. Working lengths with elementary prime estimates

Let r_j be the j-th odd prime and R_l=product_{j=1}^l r_j, with R_0=1.
We establish r_j=O((j+1)^2) without a prime number theorem. For u>=1,

    4^u/(2u+1) <= binomial(2u,u) <= (2u)^(pi(2u)).         (11)

The central coefficient is the largest of the 2u+1 binomial coefficients
whose sum is 4^u, proving the first inequality. For a prime p, its
exponent in the central coefficient is

    sum_{s>=1} (floor(2u/p^s)-2 floor(u/p^s)).

Each term is 0 or 1, and only s<=floor(log_p(2u)) contribute. Thus each
prime-power contribution is at most 2u, proving the second inequality.
Taking logs in (11) and u=(j+1)^2 gives pi(2u)>j+1 for sufficiently large
j, since its lower bound grows as a positive constant times j^2/log j.
Absorb finitely many j in an absolute constant. It follows that
r_j=O((j+1)^2). Also r_j>=j+2, so R_l>=(l+2)!/2. Taking the last half
of these factors for the lower bound, and summing log r_j for the upper
bound, gives

    log R_l=Theta(l log(l+2)).

Choose maximal l with R_l<=2n. Then

    R_l<=2n<R_l r_(l+1).

The added logarithm log r_(l+1)=O(log(l+2)) is negligible relative to
l log(l+2). It follows, as n grows, that

    l=Theta(log n/log log n),    log l=Theta(log log n).    (12)

For example log n=Theta(l log l) first implies log l=Theta(log log n)
by taking logs, and substitution gives the first assertion.

This choice is algorithmic at polynomial cost in log(n+2). Enumerate
odd candidates and test primality by trial division, accumulating primes
until the next product exceeds 2n. The first unused prime is bounded by
a fixed polynomial in l+1=O(log(n+2)), so even these elementary tests have
polynomial cost. The final test product is at most 2n times that prime;
all relevant integers have O(log(n+2)) bits.

Let e>=0 be least with L=R_l 2^e>=2n. Then

    2n<=L<4n,   2^e<2 r_(l+1),   e=O(log(l+2)).            (13)

If e=0 the first bound follows from R_l=2n; otherwise minimality gives
L/2<2n. The second follows from R_l r_(l+1)>2n and minimal doubling.
The asymptotic analysis can assume l>=1; for n=1 the same rule gives
l=0,e=1,L=2. The rule is thus defined for every n>=1.

## 4. The Fourier transform at L, with charged CRT indexing

Factor L into the coprime factors q=r_1,...,r_l and q=2^e when e>0.
For each factor compute the unit d_q satisfying (L/q)d_q=1 mod q, and
put E_q=(L/q)d_q. The E_q are orthogonal idempotents modulo L and sum
to 1 modulo L: each is 1 modulo its own factor and 0 modulo the others.
Therefore j=sum E_q j_q mod L is a bijection from factor digits to
0,...,L-1, and the corresponding k satisfies

    zeta_L^(j k)=product_q zeta_q^(d_q j_q k_q),           (14)

because the cross terms vanish modulo L and E_q^2=E_q. Consequently
F_L is tensor_q F_q up to the input/output CRT permutations and the
local output-digit permutations k_q->d_q k_q mod q.

These permutations take O(L) total work, not O(L l). Prepare the tables
E_q a mod L and d_q a mod q for each local digit a. An extended Euclidean
algorithm computes d_q using polynomial logarithmic work (trial over the
polylogarithmic range q would also suffice). Traverse digit prefixes,
updating a CRT sum modulo L and a mixed-radix address at each edge. The
bound (8) is O(L) here. Inverse permutations can be printed by swapping
the two addresses. All local table sizes and their preparation are
polynomial in log(n+2), by (12)-(13).

Apply (10) on the odd-prime axes for each fixed digit on the 2^e axis,
sharing the local compiler tables. The cost is

    O(L(l+1)^alpha (1+log(l+2))^4)+poly(log(n+2)).

Any repeated per-call array work, scalar products or tensor-algorithm
preparation is included in the first term; shared local preparation is
only the displayed polynomial term. The remaining axis is handled by
the elementary binary FFT, at O(L(1+e)) work. Its twiddles are prepared
in O(2^e) work by successive powers, and its stage indexing is linear
per stage. This axis is only polynomial in l+1. Fiber packing, if needed,
is a rectangular transposition with constant work per entry.

Thus the total cost for F_L is

    O(L[(l+1)^alpha(1+log(l+2))^4+1+e])
       +poly(log(n+2))+O(1).                              (15)

The inverse has the same bound: the geometric root sum proves F_L^2=LJ,
where J negates the index modulo L. Hence F_L^(-1)=L^(-1)J F_L.
Preparing the scalar L takes O(log(L+2)) operations from 1 by binary
doubling and addition, and L is nonzero, so preparation of 1/L is legal.
The permutation and scaling are O(L).

## 5. All lengths, the root supply, and coefficient preparation

Put eta=zeta_(2n). For 0<=j,k<n the identity

    zeta_n^(jk)=eta^(k^2) eta^(-(k-j)^2) eta^(j^2)          (16)

follows by expanding the exponent. Define length-L arrays A and B by
A_j=eta^(j^2) x_j for 0<=j<n, zero elsewhere, and
B_u=eta^(-u^2) for the residues represented by -(n-1)<=u<=n-1, zero
elsewhere. These residues are distinct since L>=2n. For each 0<=k<n
and each supported input index j, the difference k-j lies in that very
interval. Consequently the cyclic convolution entry at k is exactly
sum_{j=0}^{n-1}eta^(-(k-j)^2) eta^(j^2)x_j, with no unwanted alias term.
Multiplication by eta^(k^2) gives (F_n x)_k.

By direct expansion using positive Fourier exponents, F_L takes a cyclic
convolution to the pointwise product of the two transforms. Compute
F_L A and F_L B, multiply pointwise, and apply F_L^(-1). B is fixed, so
its full transform is coefficient preparation, explicitly charged as one
of the three transforms. The pointwise variable operation is only
multiplication by the prepared entries of F_L B, even if some are zero.
No reciprocal of such an entry is used. The outer chirps are prepared
in O(n) work: if c_j=eta^(j^2), then c_(j+1)/c_j=eta^(2j+1), whose
successive ratios multiply by eta^2. Use this recurrence and its inverse
version, rather than a long exponentiation at each coordinate. The
negative-u entries use the same squares. Initialization and padding cost
O(L). Thus exactly three full working transforms and O(n) other work
suffice, including the fixed operand.

Specify the sole supplied root by

    D_*=(2n)L 2^ceil(log_2(16L)).                          (17)

Its order is computable by the integer procedure already given. The
orders 2n and L divide D_*, so eta and all factor roots zeta_q are powers
of this specified zeta_(D_*). All power-of-two roots required for the
local width-r compiler have order <8r<=8L, and hence divide the last
factor of (17). This also supplies i and all binary FFT roots. Integer
binary powering extracts each needed initial root in O(log(n+2)) field
operations. The count of local roots and local instructions is polynomial
in log(n+2); their entire preparation remains polylogarithmic. The large
array scalar products and the full transformed chirp kernel were already
charged separately in (15)-(16).

For x>0, 2^ceil(log_2 x)<2x. Therefore

    D_*<64 n L^2<1024 n^3.                               (18)

The inequalities also hold for n=1. No assumption that rational field
operations can manufacture unbounded-order roots is made: (17) is
precisely the allowed specified root supplied to the algorithm.

The scalar-preparation divisions throughout sections 1-5 are by powers
of roots, the nonzero H_j and Toeplitz h_0, nonzero integers such as FFT
lengths, the nonzero A=(1+i)/2, or the proved nonzero t_1,t_2 in (7).
The tensor subroutine's legal scalar divisions are part of its hypothesis.
Scalar conjugates are computed by inverse-root DAG evaluation as proved
in section 1.5. Integer choices, schedules and memory accesses depend
only on dimensions, table indices and printed DAGs, not on zero tests of
complex coefficients or on variable data.

All auxiliary integer quantities have polynomial size in n. Root orders
are bounded by (18). Local compiler lists are polynomial in
log(n+2); their indices have O(log(n+2)) bits. Array indices, products
of boundedly many indices in the CRT and sector formulas, and the tensor
subroutine's address range are polynomial in n. A fixed number of
O(log(n+2))-bit words represents each. A depth-first prefix stack uses
constant work per push/pop, so no uncharged copying of l-digit indices
has appeared. All operations on input-dependent complex data remain
linear. The deterministic finite schedule at each n can also be unrolled
to a circuit of no larger asymptotic size. This is the original charged
uniform exact-complex model.

## 6. Final bound and the strict exponent slack

Since alpha>0, e=O(log(l+2)) is absorbed in
(l+1)^alpha(1+log(l+2))^4. By (13), L=Theta(n). Equations (15)-(16)
therefore give

    O(n l^alpha (log l)^4)+poly(log(n+2))+O(1)

for all sufficiently large n. Every fixed power of log(n+2) is eventually
smaller than n, so the preparation polynomial is absorbed. Substitute
(12):

    n (log n/log log n)^alpha (log log n)^4
      = n (log n)^(1-a) (log log n)^(3+a),

which is (1).

For fixed delta<a put epsilon=a-delta>0. Setting t=log log n, the
remaining estimate is t^(3+a)=O(exp(epsilon t)). For a direct proof,
choose any integer M>3+a. The exponential series gives
exp(epsilon t)>=epsilon^M t^M/M! for t>=0, which eventually dominates
t^(3+a). Thus (log log n)^(3+a)=O((log n)^(a-delta)), proving the
claimed O(n(log n)^(1-delta)) bound. This uses strict slack; it does not
assert that delta=a is justified.

For a=1261/1000000, delta=63/50000=1260/1000000 is rational and satisfies
0<delta<a<1. Also delta-1/800=1/100000>0. For comparison with the
unaudited stronger public header, delta-20099/16000000=61/16000000>0.
These are exact comparisons, conditional on supplying the tensor
algorithm. This proof supplies no finite-network certificate, makes no
claim that the public header is verified, and does not discharge the root.
