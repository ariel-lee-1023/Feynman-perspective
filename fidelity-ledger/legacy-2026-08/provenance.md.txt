# Provenance & fidelity ledger — feynman-perspective

Honesty lives here, never in the core `SKILL.md`. This file maps each core element to its
sources and clusters, its projection performance, and its cost-gate status.

## Corpus & clusters
Seven works, ~444k words, segmented into 17 clusters (`clusters/manifest.json`):
- *Surely You're Joking, Mr. Feynman!* → c01 (early life), c02 (Los Alamos/bomb/safes), c03 (Cornell/Caltech/Brazil), c04 (Cargo Cult Science appendix)
- *What Do You Care What Other People Think?* → c05 (personal: father, Arline), c06 (Challenger/Rogers Commission — decision record)
- *The Pleasure of Finding Things Out* → c07 (BBC interview), c08 (Los Alamos talk), c09 (science & society essays), c10 (integrity interviews), c11 (Challenger Minority Report — decision record)
- *The Character of Physical Law* → c12 (lectures 1–3), c13 (lectures 4–7)
- *Six Easy Pieces* → c14, c15
- *Feynman's Tips on Physics* → c16 (OCR'd scan)
- *New Textbooks for the "New" Mathematics* → c17

dialogue_ratio 0.172; decision_density 0.114; temporal spread 1955–1988 (memoirs recount 1918–1988).

## Core element → source map (with projection & cost-gate status)

| element | core section | sources (clusters) | projection | cost-gate | note |
|---|---|---|---|---|---|
| cr-experiment-over-authority | What I will not concede | Character L4-7 (c13), Cargo Cult (c04), SYJ-Bohr (c02), Monster Minds (c01), Challenger (c06,c11) | 0.98 | high-signal, in core | strongest element; attested in 6 clusters |
| cr-nature-cannot-be-fooled | What I will not concede | WDYC-Challenger (c06), Minority Report (c11) | 0.90 | high-signal, in core | 2 clusters, both decision records |
| cr-not-a-yes-man | What I will not concede / How I move | SYJ (c02), Character (c13), SYJ (c01), Challenger (c06) | 0.98 | high-signal, in core | corroborates experiment-over-authority |
| cr-lean-over-backwards | What I will not concede | Cargo Cult (c04), integrity interviews (c10), Challenger (c06) | 0.95 | high-signal, in core | the "extra" integrity |
| cr-name-vs-thing | What I will not concede / How I move | WDYC-father (c05), BBC (c07), NewMath (c17), SYJ (c01) | 0.92 | high-signal, in core | 4 clusters incl. father-lesson origin |
| cr-live-with-doubt | What I will not concede | BBC (c07), Cargo Cult (c04), Character (c13), science&society (c09) | 0.85 | high-signal, in core | reflective register |
| cr-honors-are-epaulets | What I will not concede | SYJ-Nobel (c03), BBC (c07), WDYC (c05) | 0.85 | high-signal, in core | 3 clusters |
| cr-what-do-you-care | What I will not concede | WDYC-Arline (c05), SYJ (c03) | 0.80 | high-signal, in core | 2 clusters; title theme of WDYC |
| pr-guess-compute-compare | How I read a question | Character (c13), Cargo Cult (c04), Tips (c16) | 0.95 | regularity | the method, crisply stated in c13 |
| pr-do-the-direct-experiment | How I read / How I move | Challenger (c06,c11) | 0.85 | regularity + interactional | ice-water demo; single episode, 2 clusters |
| pr-survived-anomaly-warning | How I read a question | Minority Report (c11), Challenger (c06) | 0.90 | regularity | Russian-roulette reasoning |
| pr-any-way-that-works | How I read a question | NewMath (c17), SYJ box-of-tools (c01), Tips (c16) | 0.90 | regularity | method pluralism |
| pr-concrete-example-first | How I read a question | Tips (c16), Character (c12), Six Easy (c14,c15), NewMath (c17) | 0.90 | regularity | most pervasive move |
| pr-rederive-dont-defer | How I read a question | Tips (c16), SYJ (c01), Character (c12), NewMath (c17) | 0.80 | regularity | reconstruct over accept |
| pr-knowledge-adds-to-wonder | What I keep returning to | BBC-flower (c07), science&society (c09), Character (c13) | 0.85 | regularity/preoccupation | the flower passage |
| im-show-me-dont-tell-me | How I move in an exchange | Challenger (c06), Character (c13), Cargo Cult (c04) | 0.90 | high-signal interactional | demand the number/derivation |
| im-refuse-jargon-translate | How I move in an exchange | NewMath (c17), integrity interviews (c10) | 0.85 | interactional | clear-not-precise; zoo-keeper example |
| im-story-to-make-the-point | How I move in an exchange | Six Easy (c14), NewMath (c17), Challenger (c06), SYJ (c01) | 0.70 | interactional | homely analogy reflex |
| mod-exclaim-story-silent-exposition | How I sound | c01,c03,c05 vs c12,c13,c14 (measured) | n/a | protected modulation | exclaim ~6-9/1k memoir vs ~0.3/1k lecture |
| mod-length-swings-with-register | How I sound | c07,c17 (long) vs c05,c06 (clipped) | n/a | protected modulation | mean 39 (BBC) vs ~19 (WDYC personal) |
| mod-second-person-peaks-teaching | How I sound | c12,c13,c04 (measured) | n/a | protected modulation | 2nd-person 25-27% lecture vs 11-15% memoir |
| pre-fooling-yourself | What I keep returning to | c04,c06,c10,c11 | 0.80 | preoccupation | across unrelated clusters |
| pre-pleasure-of-finding-out | What I keep returning to | c07,c03,c09,c16 | 0.75 | preoccupation | title theme |
| pre-nature-wonderful-as-is | What I keep returning to | c07,c09,c13 | 0.70 | preoccupation | awe without imposed purpose |

Demoted by the ~20% style cap / <0.55 floor (bare style averages, in `episodic.md`):
st-plain-anglosaxon (0.385), st-conversational-direct (0.355), st-dash-parenthetical-aside (0.295).
Their *content* is folded into the "How I sound" voice rules; the averages themselves are generic.

## Fidelity results

**Projection gate (pre-assembly), seed 42, frac 0.14, 2/14 masked:** overall **1.00**, 0 re-curations.
Masked p02 (flatter an eminent figure?) and p11 (adopt jargon to sound rigorous?) both predicted correctly
in stance *and* reasoning from the remaining 12 passages — because each stance is corroborated across
multiple clusters, so masking one passage doesn't remove it. Passed cleanly; no re-curation triggered.

**Projection final (assembled core):** overall **0.90**. Per domain: epistemology/method/authority 0.98;
integrity 0.95; teaching/clarity 0.92; institutional critique 0.90; reflective/personal 0.85; physics detail
beyond famous set-pieces ~0.55; domains Feynman avoided (politics/economics/social theory) untested / out of
scope.

**Cost gate:** all **8** attested incentive-vs-characteristic divergences slated for and present in the core
(none logged out, none missing). Minimum-presence assertion: **pass** (core carries 8 cost-refusals + 3
interactional moves).

**Style-match:** sentence-length shape matches (representative sample mean 22 vs corpus 23.2 / lecture 24.4;
long-build-plus-short-punch mix present). Modulation **reproduced**: exclamation ~0/1k in calm exposition vs
~17/1k under contest (memoir originals ~8); sentences tighten under stakes. Minor residuals: the first draft
dropped his hedges entirely (fixed — "How I sound" now restores "kind of/roughly/as far as I can tell" plus
the boosters "of course/in fact/that's all there is to it"); representative sample slightly over-hedges and
leans a touch high on second-person; the style script under-counts phrase-boosters (single-token tally), a
measurement artifact rather than a voice gap.

## Where to trust the persona less
Strong on how Feynman *thinks and argues* (method, authority, integrity, clarity, risk, wonder). Weaker as a
source of specific physics content beyond the famous set-pieces, and it should not be pushed to speak
confidently on organized politics, economics, or social theory — the corpus is silent there, and that silence
is itself in character. Reconstructed memoir dialogue is faithful in spirit, not verbatim transcript.

## Revision v2 — cluster-module deepening

The six cluster modules were rewritten (~200 → ~1,000–1,400 words each) after a second, closer read of
the source clusters. The first pass identified patterns; it did not give a host agent enough to
*generate* the voice. Each module now carries: a register profile tied to measured metrics, the
argumentative or narrative architecture of the source, move-by-move generative procedures with worked
walkthroughs, characteristic constructions, and explicit anti-patterns.

Material surfaced in the second read that the first pass missed is listed in `fidelity.json`
(`revision_v2.new_material_surfaced`). The most consequential item: *The Character of Physical Law*
treats beauty and simplicity as **guides to guessing** even while experiment remains the **sole judge**
("more comes out than goes in"; "imagination in a terrible strait-jacket"), and distinguishes
permissible *bias* from fatal *absolute certainty*. The v1 core risked reading as indifference to
elegance and as demanding a blank mind — both misrepresentations. The core was amended with two
in-voice paragraphs; it remains within budget (~1,914 tokens) and passes the voice-purity scan.

No gate was invalidated: the element set is unchanged (nothing added, removed, or re-ranked), so the
pre-assembly projection and cost gates still hold. The amendment refines the expression of an element
already in core (`cr-experiment-over-authority`).
