# Richard Feynman perspective — 1.0

**Candidate.** This release uses persona-distiller's current incremental migration
format. Package and bounded source checks are recorded in
[validation.json](transworld-identity/validation.json). **Machine recognition was
not run:** the user explicitly requested no new evaluation and Candidate publication.
The version number is a release label, not a fidelity certification.

The perspective supports scientific reasoning, concrete explanation, learning,
scrutiny of evidence and reflective conversation about curiosity and uncertainty.
It draws on Feynman's dated lectures, interviews and memoirs; generated speech is
not an authentic quotation or a claim to be the historical person.

## What changed in 1.0

- Migrated all old evidence to `transworld-identity/`, preserving original bytes,
  result scope and source lineage. Historical outcomes are indexed in
  [applicability-1.0.json](transworld-identity/applicability-1.0.json).
- Added situated evidence, core-claim decisions, a bounded source review and an
  unexecuted recognition profile. No new model evaluation was performed.
- Clarified fixed historical background, stipulated changes and conditions for
  reconsidering an endorsement in [scope](references/scope.md).
- Preserved the core, frameworks, voice and all seven source-oriented topic modules;
  updated CI to persona-distiller revision `a010b3ed320a6edf7273d1510908c9540501f6dc`.

## Use and installation

Clone this repository, check out tag `1.0`, and open it as a conversation workspace.
The local [AGENTS.md](AGENTS.md) activates the perspective while honoring explicit
requests to leave the voice or maintain the package. For another skill host, install
the root [SKILL.md](SKILL.md) with its `references/` directory. The relative discovery
link `.agents/skills/feynman-perspective -> ../..` points to that single runtime copy.

The host loads [scope](references/scope.md) with the core, [voice](references/voice.md)
before sustained prose, and [frameworks](references/frameworks.md) for procedures
and historical judgments. Seven topic modules provide deeper source examples.

Examples: find a test that distinguishes two explanations; recover a formula's
sign from one physical example; examine the evidence that could hurt a favored
claim; explain in Chinese while keeping the reasoning concrete.

## Sources and limits

The seven user-supplied works remain the corpus: *Surely You're Joking, Mr. Feynman!*,
*What Do You Care What Other People Think?*, *The Pleasure of Finding Things Out*,
*The Character of Physical Law*, *Six Easy Pieces*, *Feynman's Tips on Physics*,
and *New Textbooks for the “New” Mathematics*. Sources span public material from
1955–1986 and later memoir publication. Feynman's lecture text is distinguished
from editors, students and other authors. Full books and scans are not distributed.

The 1.0 source review inspected 21 located excerpts within a 24-unit, zero-OCR
boundary and reviewed all retained core claims. It is machine-assisted editorial
review, not independent historical auditing. See [provenance](transworld-identity/provenance.md)
and [source review](transworld-identity/source-review-1.0.json).

Historical development performance was **0.75 for both the persona and a minimal
Feynman prompt**, on two correlated probes. Earlier finals stopped at **11 of 32
planned answers**, with scoring incomplete. Those records remain history, not
current acceptance. Introductory English lecture measurements are narrow;
broader register comparisons remain inconclusive, and Chinese voice is unvalidated.
Modern factual applications need current evidence and clear attribution boundaries.

## Validation

With the pinned persona-distiller checkout beside this repository:

```sh
python3 ../persona-distiller/scripts/validate_package.py . --strict --headings transworld-identity/required-headings.txt
python3 scripts/check_release.py
```

CI checks structure, portable release evidence, JSON, runtime hashes, historical
byte preservation and the skill symlink. It makes no model calls. A passing CI run
does not convert this Candidate into Standard accepted. Contributor material is
MIT-licensed; source rights remain separate under [NOTICE](NOTICE.md).
