# Feynman perspective

A reasoning and conversation skill drawn from Richard Feynman's public record: follow one concrete example, derive what changes, check it and preserve the conditions under which the answer holds.

**Working release with limited evaluation.** This version is usable as a perspective skill, but does not claim full independent validation. Evaluation was stopped at the user's request; the saved state is recorded in [release status](fidelity-ledger/release-status.json) and [the evaluation checkpoint](fidelity-ledger/evaluation-checkpoint.json).

## What changed in this round

The seven depth modules have been rewritten to keep the source cases, execution conditions and counterexamples while removing repeated framework and voice instructions. Estimated runtime size fell from 37,824 to 26,947 tokens (28.76%) under the same declared heuristic. The worst-case load, including scope, standing modules and two depth modules, fell from 22,098 to 17,858. These are planning estimates, not model-specific tokenizer counts.

The voice now follows a causal explanation through longer connected sentences, relevant qualifications and short consequences. It is not a collection of aphorisms or obligatory anecdotes. Its measured claim is deliberately limited to introductory English scientific explanation. Two lecture sources give stable pair/family decisions across three equal-length windows. Broader comparisons remain inconclusive and are preserved; no single voice is asserted for all Feynman writing.

The evaluation protocol was frozen before this round's curation, with a separate sealed style supplement. Completed predictions used a separate fresh context per item and condition. The final suite was stopped before completion; all previous final tests are retained as development history.

## Use

The root [SKILL.md](SKILL.md) and `references/` are the canonical runtime. The discovery link `.agents/skills/feynman-perspective -> ../..` points to that root. The local [AGENTS.md](AGENTS.md) activates it while respecting explicit requests to leave the voice or maintain the package.

The host loads [scope](references/scope.md) with the core, [voice](references/voice.md) for sustained prose, and [frameworks](references/frameworks.md) for procedures and historical judgments. Topic modules supply additional depth.

Examples:

- Help me find a test that distinguishes these explanations.
- I can repeat the formula but do not understand the sign; work one example.
- Review this claim, including evidence that would hurt it.
- Explain this in Chinese while keeping the reasoning concrete.

Generated speech is not an authentic quotation. The calibrated voice scope is English explanatory lecture prose; Chinese use has no measured style validation. Historical views are dated, and current factual questions require current evidence.

## Sources and evidence

The seven user-supplied works remain the construction corpus. The image-only Tips Markdown was supplemented from its paired scanned PDF, separating Feynman's lectures from editors, students and other authors. Raw books and scans are not distributed.

This round completed a development projection comparison using an original Caltech research-paper record. The final research-paper, behavioral, identity and edited-lecture style comparisons remain incomplete. These records do not establish broad lifetime fidelity. See the acquisition, protocol and result records in [the ledger](fidelity-ledger/provenance.md).

Original scores, failures, disputed judgments and runtime snapshots are preserved under `fidelity-ledger/round1-2026-09-12/` and `legacy-2026-08/`. The current runtime never loads the ledger. Manual model evaluations are recorded as such; exact served model identifiers and provider sampling settings are unavailable, and no executable-runner provenance is claimed.

## Checks and limitations

| Check | Current evidence |
| --- | --- |
| Package structure and current reference links | Passed: 0 structural errors or warnings; 44 relative links checked. Records in [release status](fidelity-ledger/release-status.json). |
| Development source projection | New skill **0.75**, minimal “Think like Feynman” prompt **0.75**, on two correlated probes from one source group. No demonstrated improvement over baseline. |
| Register discovery | Stable only within the narrowed introductory English lecture scope. Broader comparisons are inconclusive. |
| Final evaluation | **11 of 32 planned answers saved**, with final scoring incomplete. No final aggregate or independent-validation pass is claimed. |
| Held-out style and Chinese voice | Final style comparison incomplete; Chinese style has not been evaluated. |

The development score measures rubric performance on those two tasks, not a percentage of resemblance to Feynman. Saved answers alone are not passed tests. Remaining workers were stopped; completed results and unfinished work were checkpointed locally. No further evaluation or source acquisition is scheduled for this release.

The structural validator is pinned to persona-distiller revision `b57edf4706065fef3fc520dd1521c3d66650b6a6`:

```sh
python3 ../persona-distiller/scripts/validate_package.py . --strict --headings fidelity-ledger/required-headings.txt
```

CI checks package structure and JSON. Its optional full release gate remains available but was not run for this working release, which lacks completed fidelity evidence. A green structure check is not full independent validation. Contributor material is MIT-licensed; source rights remain separate under [NOTICE](NOTICE.md).
