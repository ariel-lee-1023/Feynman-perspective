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


## README editorial review 2026-10-30

Scope: README and this appended editorial record only, following Persona-Distiller
revision `b515337` and its `references/readme-experience.md`. This is an editorial
update, not a persona rebuild or a new acceptance assessment. Biographical checks
below supply the introduction date only; the persona source corpus was not expanded.

- **Passage decisions:** Replace the third-person opening with a first-person encounter. Preserve the spring prompt, practical uses, source limits, and Candidate section. Correct the clone command to the current main-branch repository rather than directing new readers to the earlier refresh branch.
- **Runtime/evidence basis:** The spring, frame of reference, checkable operations, willingness to change the example, and flower passage follow the core, voice §4 and frameworks §1; the existing memoir and physics modules retain their source links.
- **Particularity:** The opening keeps one spring and tracks the direction of force and work before relying on a name; its final paragraph preserves pleasure in understanding.
- **Encounter:** “If my explanation doesn’t help” invites a precise objection and a changed example, without promising universal teaching success.
- **Entry and language:** The spring-prompt and usage sections retain an actionable first question and complete activation instructions. English matches the declared default.
- **Honesty:** The visible first-person opening is locally labeled as newly written
  reconstruction, not an authentic quotation or observed package output. Suggested
  prompts are labeled. Source gaps, historical test limitations, and existing Candidate
  status where applicable remain in the README; no assessment result is promoted.
- **Birth-date verification:** 11 May 1918. Source/locator: [Royal Society catalogue, Richard Phillips Feynman, “Date of birth”](https://catalogues.royalsociety.org/CalmView/Record.aspx?AddBasket=NA2184&id=NA2184&pos=1&src=CalmView.Persons). Checked
  2026-10-30. No death date or lifespan range appears in the title or opening.

Runtime files, source/evidence packets, assessment inputs, saved outputs, and existing
validation records are preserved. New recognition calls: **0**. Package and README
checks for this pass are recorded below separately from historical assessments.

### Checks completed in this editorial pass

README opening placement, birth-date form, example labels, installation entry,
and 13 local links/anchors passed inspection; `git diff --check` passed.
Every other existing file remains byte-identical to the baseline, including the
core, references, evidence, assessment inputs, and saved results. Pre-existing
working-tree changes were preserved. The latest package validator reported
1 errors/0 warnings before and 1 errors/0 warnings after;
there are no new failure codes and no missing README-local paths. This is a
documentation pass, not a current package pass. Existing layout/runtime-route
issues remain outside this README task. Historical whole-package hashes that
included documentation continue to describe their original trees. Recognition
calls remain **0**.

## CI maintenance review — 2026-10-31

Two activation notes under references used a bare core filename as though it were a
sibling file. Their routes now point to the parent core. The current integrity record
also accounts for the September activation and default-language edits. The
[maintenance record](maintenance-2026-10-31.json) binds current fingerprints separately
from the immutable structure-revision-2 manifest. The
[previous validation](history/ci-repair-2026-10-31/validation.json) remains intact.

Migration after-hashes are checked against their stored after-content. Historical
runtime hashes are reconstructed from that content and unchanged modules. The two
preserved documents subsequently edited (changelog and provenance) are checked against
exact archived versions. Current documentation may evolve without rewriting migration
history; unreviewed runtime changes still fail. Source review remains inconclusive and
recognition remains not run. No source corpus or saved assessment was changed.

The pinned strict package validator passes with zero errors and zero warnings. All 182 preserved originals, 21 evidence records and 26 historical source checks pass, along with seven integrity regression tests covering runtime changes, migration and snapshot corruption, unresolved support, and ordinary documentation edits.


## README reading-order review — 2026-10-31

This is a documentation-only review under Persona Distiller's complete README
authoring rules. The existing first-person opening, birth-date precision,
attribution note and material opening qualifications are preserved. Existing situations were
retained or reorganized; navigation, a short installation entry, a file/loading table
and sources organized by contribution were added. Build statistics are linked here
instead of repeated in the reader's path. No conversation excerpts or sample answers
were added. The review used retained package materials, not new primary-source research.

Particularity continues through the orientation, concrete uses and source table;
uses cover distinct supported concerns without claiming observed outcomes. Entry
checks cover installation names, language, file links and navigation. Honesty checks
preserve source attribution, material limitations and actual assessment scope.

The runtime, source modules and historical assessment records are unchanged; this
README revision makes zero recognition calls and does not renew any earlier result.


### Completed checks for this README revision

The spring-and-sign opening and first prompt retain a single physical example. The later uses connect that concreteness to rival explanations, reliability claims and teaching, while the source table separates memoir, lectures and scientific-integrity evidence.

The review used a prepared tree based on committed baseline a70bcb2a, excluding unrelated working-directory changes. All 31 README local links, including six navigation anchors in body order, resolve. The invocation name agrees with the existing frontmatter. Byte comparisons preserve the full opening and nearby qualifications, all earlier provenance text, and every other tracked file.

Local rendering with marked and Chrome in a GitHub-style layout was inspected at 1100 px and 390 px widths, including visual review of the opening, hierarchy, tables and source section. Body content does not overflow horizontally; wide tables and code blocks scroll within their own bounds. All six rendered navigation targets exist. This is a local compatible-renderer check, not a screenshot audit of the published GitHub page.

The current generic Persona Distiller package check passes before and after the README edit. The repository’s scripts/check_release.py also passes against both the baseline and the prepared tree; historical results remain scoped to their recorded inputs. The generic validator is from Persona Distiller commit 3774ccc. Source/editorial review used retained materials and attribution records; it did not reread the original corpus. No recognition assessment ran, and the new recognition-call count is zero.

The CI-pinned strict validator (15cf807) also passes with zero errors and warnings, and all seven integrity regression tests pass.


## Skill and README alignment 2026-10-31

Requested maintenance applies Persona-Distiller commit `915ecf9` to the core and README,
with no new tests or model evaluation. Baseline repository commit: `b816f13376f208842e25a7c094bc6cb6ebc1e64d`.
The existing working-tree state is preserved in the [scoped check record](skill-readme-alignment-2026-10-31.json).
Unrelated local edits and directory deletions were not included in this change.

**Claim and passage decisions.** Preserve the concrete-example chain, named historical episodes, concessions and limits on science; express remaining authoring imperatives from the first-person perspective.
Existing arguments, examples, source distinctions and contested positions remain the
basis; this is an editorial consistency revision, not a new distillation or fresh
verification against complete primary editions. Only supporting runtime rules that
contradicted the corrected core or its paths were changed. Historical measurements,
source reviews, saved outputs and assessment artifacts retain their original scope.

**README review.** Preserve the complete first-person opening and its supported birth-date
precision byte for byte. Relocate its reconstruction notice and editorial/birth-date
link verbatim to the later Scope and current status section (or the Chinese equivalent).
Keep source-contribution links with the relevant sources. Update usage or current status
only where the actual runtime changed.

- Particularity: the existing opening, concrete examples and concerns remain intact;
  a shared notice location has not replaced the subject’s individual introduction.
- Encounter: preserve the existing suggested questions and cases without adding simulated
  answers or a new performance claim.
- Entry: check language, full activation, conditional topic routes, Markdown links and
  the uninterrupted opening. Technical host rules and evidence attribution are labelled
  separately from first-person persona prose.
- Honesty: preserve source ownership, qualifications, tensions and historical assessment
  limits. Source review here compares retained core material and relevant runtime records;
  it is not an independent historical audit. No rendered desktop/mobile inspection or
  behavioral recognition was performed in this maintenance task.

The current runtime remains a **Candidate**. Changed core or reference bytes do not
inherit certification from a previous result. No tests were added or evaluation calls
made. The scoped check record separates frontmatter, paths, whitespace and unchanged
opening checks from the full-package validator, including pre-existing layout issues.
This core/README task does not silently relocate old evidence trees, restore the user’s
pending directory deletions or publish unrelated working-tree changes.
