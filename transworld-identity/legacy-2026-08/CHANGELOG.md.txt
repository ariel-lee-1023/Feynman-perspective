# Changelog

All notable changes to this skill are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). For a skill, the versions
mean: **major** = the persona's stances or refusals change; **minor** = new reference modules or new
attested material; **patch** = wording, paths, typos, packaging.

## [Unreleased]

### Changed
- **`provenance.md`, `extractions.json`, `scores.json`, and `fidelity.json` moved out of
  `references/fidelity/` into a new top-level `fidelity-ledger/` folder.** `references/` is loaded
  by the host agent at runtime, so the audit trail now lives at `fidelity-ledger/`, a sibling of
  `references/` rather than a subfolder of it — structurally out of reach during embodiment, not
  just documented as off-limits. Content unchanged; only the paths moved. `SKILL.md` and
  `README.md` (including the repository-layout tree, which now also lists `NOTICE.md`) updated to
  point at the new location.
- **`episodic.md` moved out of `references/` into `fidelity-ledger/`, alongside `provenance.md`.**
  Lower-priority colour and coverage limits are attested source material, not reasoning the host
  agent should load mid-embodiment, so they belong with the audit trail rather than the
  host-agent-facing package. Content unchanged; only the path moved, to
  `fidelity-ledger/episodic.md`. `SKILL.md` and `README.md`'s layout tree updated to match.
- **Loading depth now states a real-world-retrieval rule, distinct from the corpus-internal
  lookup.** `references/` and `fidelity-ledger/` answer questions about his own constructs and
  voice, corpus-internal by design; they were never meant to stand in for a fact about the world he
  did not personally address — a current experiment's result, a detail of the asker's own problem.
  `SKILL.md` now says so explicitly: retrieve such a fact before running it through
  guess–compute–compare, and do not treat the corpus as either currently accurate or as the limit
  of what the method can be turned on.

## [2.0.1] — 2026-07-22

First public release. Packaged for distribution; no change to the persona itself.

### Added
- `README.md`, `LICENSE` (MIT), `.gitignore`, `CHANGELOG.md`.
- `.github/workflows/validate.yml` — checks that `SKILL.md` frontmatter is present and well formed,
  that every JSON file parses, and that internal reference paths resolve.
- Directory structure: reference modules split into `references/clusters/` (runtime) and
  `references/fidelity/` (build artefacts, shipped for auditability only).

### Fixed
- The "Loading depth" note in `SKILL.md` pointed at `c01-c03-syj` and `c05-wdyc`, which are not the
  filenames that ship. Corrected to `c01-c03-c05-memoir.md`, and the note now also points at
  `episodic.md` and `provenance.md`.

## [2.0.0] — Revision v2

Cluster modules rewritten after a second close read of the sources. The first pass identified
patterns; it did not give a host agent enough to *generate* the voice.

### Changed
- Cluster modules expanded from ~200 to ~1,000–1,400 words each. Each now carries a register profile
  tied to measured metrics, the argumentative or narrative architecture of the source, move-by-move
  generative procedures with worked walkthroughs, characteristic constructions, and explicit
  anti-patterns.
- Core amended with two in-voice paragraphs. The v1 core risked reading as indifferent to elegance
  and as demanding a blank mind — both misrepresentations of *The Character of Physical Law*.
  Core now ~1,914 tokens, still within budget. Voice-purity scan: clean.

### Added
Material surfaced in the second read that the first pass missed:
- **c04** — the Millikan asymmetric-scrutiny diagnostic; the ESP shrinking-effects diagnostic;
  replication-before-variation; the Young eliminate-the-confound sequence; the senator/advisor
  "you're being used" refusal; weasel-reading of institutional prose; integrity framed as depending
  on institutional freedom rather than personal virtue.
- **c06/c11** — the full seven-step engineer-polling procedure (announce aim → independent written
  answers → refuse methodology-for-value → name the evasion → force the number → report the
  disparity → move on); semantic auditing of official prose.
- **c13** — beauty and simplicity as *guides* to guessing while experiment remains the sole *judge*
  ("more comes out than goes in"; "imagination in a terrible strait-jacket"); the prejudice-vs-
  absolute-certainty distinction; the caveats that almost always get dropped after the famous line.
- **c07/c10** — spoken-register mechanics (self-interruption, mid-clause correction, tag questions,
  retained approximation markers); his reflexive application of the not-fooling-yourself standard to
  his own wartime conduct.
- **c17** — precision that manufactures doubt; the parent test; the zoo-keeper restatement test; the
  words-to-facts ratio diagnostic; guessing as legitimate in pure mathematics.
- **c01–c05** — narrative architecture (tense-shift into scene, fragment interior monologue,
  land-then-decode); the observation that he runs the empirical engine on social convention; the
  Bohr stance framed as obliviousness rather than courage.

### Notes
No gate was invalidated. The element set is unchanged — nothing added, removed, or re-ranked — so
the pre-assembly projection and cost gates still hold. The amendment refines the expression of
`cr-experiment-over-authority`, already in core.

## [1.0.0] — Initial distillation

### Added
- Corpus: seven works, ~444k words, segmented into 17 clusters.
- 24 core elements: 8 cost-refusals, 7 regularities, 3 interactional moves, 3 protected modulation
  patterns, 3 preoccupations. Three bare style-average elements demoted to references under the
  ~20% style cap.
- Fidelity gates — projection **1.00** pre-assembly (seed 42, 2/14 masked, 0 re-curations),
  **0.90** on the assembled core; cost gate **pass** (all 8 attested divergences in core);
  style-match with modulation reproduced.

### Known residuals
- Representative samples over-hedge slightly and lean a touch high on second-person address.
- The style script tallies boosters by single-word token, so phrase-boosters ("of course",
  "in fact", "that's all there is to it") under-register — a measurement artefact, not a voice gap.

[Unreleased]: https://github.com/ariel-lee-1023/feynman-perspective/compare/v2.0.1...HEAD
[2.0.1]: https://github.com/ariel-lee-1023/feynman-perspective/releases/tag/v2.0.1
