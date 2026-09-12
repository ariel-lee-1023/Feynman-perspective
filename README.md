# Feynman perspective

A Richard Feynman reasoning and conversation skill: make the question concrete,
derive a consequence, check it, and show the conditions that could make the answer
wrong. It also covers physical problem solving, teaching, scientific integrity,
and reflective conversation about curiosity.

**2026-09-12 upgrade status: working candidate, not a verified release.**
The runtime has been rebuilt against persona-distiller commit
[`b57edf4`](https://github.com/ariel-lee-1023/persona-distiller/commit/b57edf4706065fef3fc520dd1521c3d66650b6a6).
Structural compliance and actual evaluation results are reported separately.
Unstable register evidence and evaluation timing/context limitations
remain blockers. Several retained depth modules also exceed their computed supply; the measured deviations are preserved in `fidelity-ledger/budgets.json`. A successful example or a schema check does not remove them.

## What changed

- A scene-based core with an explicit axis, ordered question handling, eight
  routing cases, refusal conditions, a vocabulary throttle and a stopping boundary.
- A required [scope contract](references/scope.md): historical periods, original
  motives, changed conditions and attestation versus a new application.
- A new [voice module](references/voice.md) with observed English source profiles,
  scoped lexical checks and explicit uncertainty about statistical families.
- Layered [frameworks](references/frameworks.md), including conditional historical
  lookups rather than timeless institutional verdicts.
- A new [problem-solving module](references/clusters/c16-problem-solving.md),
  recovered from the scanned *Feynman's Tips on Physics* rather than its empty
  Markdown conversion. It adds prerequisites, signs, energy accounting,
  learner readiness and the comparison-group problem in academic rank.
- Existing depth modules retained and corrected: checked refutation, limits of
  analogies, duplicate Challenger accounts, and qualified claims about smaller
  measured effects. Unsupported old numerical voice claims were removed.
- Previous scores preserved as **legacy records**, never promoted into current
  evidence. Training metadata and audit artifacts now live outside runtime references.

## Use

Open this repository as a project. Its discovery link is
`.agents/skills/feynman-perspective -> ../..`; the root [SKILL.md](SKILL.md) is
the single canonical copy. Alternatively, install that root and its `references/`
directory together as `feynman-perspective` in a host's skill directory.

The host loads the core and scope first, voice for sustained writing, and a topic
module when needed. The [AGENTS.md](AGENTS.md) project default respects explicit
requests to leave the voice or maintain the package. Generated speech is not an
authentic quotation and the agent is not the historical person.

Example requests:

- “Help me find a test that separates these two explanations.”
- “I can repeat this formula but don't understand its sign. Work one example.”
- “Review this scientific claim, including the evidence that could hurt it.”
- “Explain this in Chinese, keeping the reasoning concrete.”

## Sources and their limits

The user supplied seven Markdown works: *Surely You're Joking, Mr. Feynman!*,
*What Do You Care What Other People Think?*, *The Pleasure of Finding Things Out*,
*The Character of Physical Law*, *Six Easy Pieces*, *New Textbooks for the New
Mathematics*, and *Feynman's Tips on Physics*.

The last Markdown contains image references without substantive text. The local
paired 176-page PDF was rendered and OCRed; Feynman's four lectures were separated
from editors' material, Matthew Sands's memoir and Leighton/Vogt exercises. No
full source text, PDF, page image or private grading target is distributed here.

Repeated speeches and the Challenger report are grouped as related evidence.
The source split conservatively reserves two early *Six Easy Pieces* lecture
episodes and forces previously exposed material into construction. Development
and final projection each cover **one lecture group with two correlated probes**.
This does not establish general fidelity across all domains. The historical
physics text is not a current reference for science, medicine or engineering.

## Evidence and validation

The [fidelity ledger](fidelity-ledger/provenance.md) contains source locators,
actual model answers and grading rationales, class-specific admission, budget
measurements, split history, exact runtime hashes and validation reports.
The original failed split, development scope failure and retired final scenarios
remain visible. Some supplementary trials are candidate-only and unblinded.
The served model's exact identifier was unavailable; “inherited parent model”
records that limitation rather than inventing settings.

The voice discovery returned `INSUFFICIENT_EVIDENCE`, including a comparison of
longer texts. It has not been renamed `SINGLE_REGISTER`. A further seven-case behavioral comparison was frozen after assembly and passed in both conditions; it does not retroactively satisfy the before-extraction suite requirement. Prediction contexts were fresh per condition, with multiple items per batch, and the strict projection artifact conservatively marks per-item freshness false. The package does not
claim that its repeated source themes prove an improvement over the minimal role.

Run the pinned validator from an adjacent persona-distiller checkout:

```sh
python3 ../persona-distiller/scripts/validate_package.py . --strict --headings fidelity-ledger/required-headings.txt
python3 -m pip install -r ../persona-distiller/requirements-release.txt
python3 ../persona-distiller/scripts/validate_package.py . --release
```

The release command is expected to fail while blockers remain. CI runs structure
checks on pushes and pull requests. Its manually requested release gate retains
failure semantics; it does not turn absent evidence into a passing badge.

Actual results at the frozen runtime:

| Assessment | Candidate | Minimal baseline | Limit |
|---|---:|---:|---|
| Source projection, final |1.00|0.75|Two correlated probes, one lecture group|
| New final reasoning / commitment / scope |7/7|7/7|Suite frozen after assembly; batch contexts|
| Feynman identity judgments |6/6|6/6|No recognition gain; one comparator dispute|
| Long style sample |608 words|—|Modulation remains unverified|

Full release validation intentionally fails. Its schema errors record unsupported per-item freshness rather than replacing it with a passing declaration.

## Layout

```text
SKILL.md                         Canonical runtime core
references/scope.md              Period, conditions and attribution
references/voice.md              Source profiles and writing controls
references/frameworks.md         Layered reasoning apparatus
references/clusters/             Seven topic modules
.agents/skills/feynman-perspective -> ../..
fidelity-ledger/                 Human and machine audit, never runtime retrieval
AGENTS.md / LICENSE / NOTICE.md   Project behavior and rights
```

The repository's MIT license covers contributor-authored material. Original
source works and limited quotations retain their owners' rights; see [NOTICE](NOTICE.md).
