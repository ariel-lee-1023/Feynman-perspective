# Provenance — Feynman 1.0 Candidate

## Contract and source boundary

This is an incremental upgrade of Richard P. Feynman's scientific reasoning,
teaching and reflective-conversation perspective. Supported period and domains
remain those in the runtime scope: public material from 1955–1986, 1961–1963
teaching, and memoirs published in 1985/1988 about earlier events. The seven supplied
works remain the construction corpus. This run adds no source work and no OCR.

The user asked for the latest persona-distiller old-repository upgrade, Git push
and tag `1.0`, then explicitly selected no new evaluation and Candidate publication.
The evaluation budget is therefore zero. Source review is separately bounded at
24 reading units and zero OCR pages; 21 units were inspected. A unit is a located
contiguous excerpt in an existing supplied transcription or retained cleaned
training source. The reading log records exact source and span hashes. Existing
runtime/evidence review and locator searches are not a new full-source extraction.

The confirmed existing `feynman-perspective` repository is upgraded in place,
preserving its Git history and clean baseline. It is not a newly built persona
to be relocated through staging. Private scratch stays outside the repository.
The delivery target is the existing origin branch `codex/refresh-feynman-20260912`
and annotated tag `1.0`; the existing `0.5` tag is retained.

## Lineage and decisions

Baseline: `39587f17002820f6437dd6c54002c30a476417f4` (`0.5`). Authoring tool:
`a010b3ed320a6edf7273d1510908c9540501f6dc`, confirmed equal to its remote HEAD.
The tool's lossless migration moved the old evidence directory to this canonical
directory and relinked active documentation and CI. Migration manifests retain
all original hashes. The previous live provenance is preserved byte for byte in
[history/pre-1.0/provenance.md](history/pre-1.0/provenance.md).

The core, frameworks, voice and all seven topic modules remain byte-identical.
Only scope gains explicit fixed-history, stipulated-change and defeasible-disposition
guidance plus the conditions for reconsidering a refusal. This is a bounded
editorial application, not newly attributed biographical behavior. Source-backed
claim decisions are in [claim-decisions-1.0.json](claim-decisions-1.0.json).

## Sources and attribution

The retained corpus consists of the two autobiographical collections (SYJ and
WDYC), *The Pleasure of Finding Things Out*, *The Character of Physical Law*,
*Six Easy Pieces*, *Feynman's Tips on Physics*, and *New Textbooks for the “New”
Mathematics*. Full titles are listed in the README; original source-file identities
are preserved in the round1 work inventory. This pass uses chapter/section locators, exact inspected
file hashes and line spans in [source-reading-log-1.0.json](source-reading-log-1.0.json).

Feynman's speech is distinguished from editorial framing, student questions and
footnotes. Later memoirs are recollections; the senator/publicity example is a
hypothetical illustration, not an actual engagement newly asserted here. Challenger
narrative and Appendix F belong to one inquiry. Beauty's strong rhetoric is retained
alongside the checked-experiment constraint, without resolving the tension by
discarding either. Existing OCR formulas and interleaved textbook columns are not
used for quantitative voice claims or unverified literal formulas.

## Current and historical outcomes

The directory name denotes the evidence and assessment function; it does not
assert numerical identity, essential properties or an identity certificate.

[validation.json](validation.json) is the current status. [source-review-1.0.json](source-review-1.0.json)
is the bounded machine-assisted editorial review, not an independent historical
audit. The recognition profile is unexecuted; it supplies no score and is not
presented as a frozen empirical run. No new generators, judges or research workers
were launched, and no future evaluation is scheduled.

[applicability-1.0.json](applicability-1.0.json) accounts for every old evidence file.
Old development results, incomplete final predictions, scores, disagreements and
voice measurements remain attached to their original inputs. The old 0.75/0.75
development tie does not show improvement. Eleven saved final answers out of 32
planned are not a finished final suite. None becomes a bounded-recognition pass.
Changing the loaded scope also prevents rebinding old whole-runtime answers.

The name review retains the two attested expressions, scientific integrity and
cargo cult science, as source-bound terms. Other procedural names are editorial
handles, including guess/derive/compare; no proprietary four-step Feynman Technique
is attributed. Voice variation is descriptive, not a universal quota. English
measurements do not establish Chinese voice fidelity. Full sources and scratch
are excluded; source rights and existing license terms remain unchanged.

## README reader-experience revision — 2026-09-12

This documentation-only pass follows persona-distiller
`49df17f36eaf4e4b65019e2108710b1387b27a15`, specifically its independent
reader-experience guidance. The baseline is `c46cddd`; local README history at
`39587f1` and `1adbf4a` was inspected alongside the current core, scope, methods,
voice and source modules. No fresh sources, OCR, model answers or judges were used.
The runtime, evidence packet, recognition profile and validation records remain
byte-identical. Current assessment applicability and Candidate status are unchanged.
The published `1.0` tag stays attached to its original commit; this is a later
documentation commit on the existing release branch.

### Passage decisions

| Passage | Decision and reason |
| --- | --- |
| Candidate, migration and validation opening | Replace the administrative introduction with a concrete difficulty involving a formula or reassuring report. Preserve the actual status in the visible confidence section. |
| Earlier concrete-example and wonder introduction | Recover its concerns selectively, supported by FY-FATHER and FY-FLOWER. The new prose is editorial writing, not restored historical wording or Feynman's speech. |
| Earlier formula-sign prompt | Develop into a clearly labeled suggested spring prompt, supported by FY-SPRING. The following explanation describes intended operation; it is not saved package output. |
| Earlier incident-review and jargon use cases | Qualify through current FY-SEAL, FY-NEWMATH and FY-MILLIKAN conditions. No universal claim that every survived anomaly proves danger or that precision is undesirable is restored. |
| Current installation and source rights | Preserve the workspace activation, canonical runtime and discovery link. Make the clone command select the actual current release branch; distinguish the immutable 1.0 snapshot. |
| Detailed migration counts, tool revision, calls and old scores | Remove from the introductory path and retain in linked maintainer records. Keep the practical consequence of incomplete recognition and broader assessment visible in the README. |

### Four editorial outcomes

- **Particularity:** The opening joins the father-and-bird distinction, physical
  interpretation of a sign and the flower discussion. FY-FATHER, FY-SPRING and
  FY-FLOWER support these particular concerns; a name substitution would lose the
  connection to the documented episodes.
- **Encounter:** The spring paragraph stays with the hand, restoring force and
  work account. The reliability and favored-conclusion examples show resistance
  to unsupported reassurance, with changed-condition and symmetric-scrutiny limits
  from FY-SEAL and FY-MILLIKAN. These are promises about supported methods, not
  observations from an unperformed demonstration.
- **Entry:** A labeled starting prompt supplies a concrete problem; the use
  section gives a clone command for the current branch and explains workspace
  activation and the portable skill files. The four use cases describe material
  to bring and what work the perspective is designed to do with it.
- **Honesty:** The opening distinguishes the skill from present-day testimony and
  authentic quotation. The source section bounds English/Chinese voice and dated
  factual claims. The confidence section preserves Candidate, states recognition
  has not run, and acknowledges the inconclusive earlier work without treating
  mechanical checks as a personality assessment.

These are authorial editorial judgments, not human validation or numerical
readability scores. Mechanical verification covers unchanged assessment/runtime
bytes, local links, structure and zero evaluation-call consumption. It does not
establish the literary success of the introduction.

## Maintenance checks

From the repository root, with persona-distiller checked out beside it:

```sh
python3 ../persona-distiller/scripts/validate_package.py . --strict --headings transworld-identity/required-headings.txt
python3 scripts/check_release.py
```

CI remains pinned to the 1.0 structural validator. The newer reader-experience
guidance adds an editorial obligation; it does not retrospectively change the
recognition protocol or authorize new evaluation calls.

Completed checks for this documentation pass: strict structure passed with zero
errors and warnings; 46 current relative links and the maintenance anchor resolve.
The release-integrity check verified all 148 historical files. All files other
than README and this provenance remain byte-identical to the documentation
baseline, including every runtime and assessment input; evaluation calls remain zero.
