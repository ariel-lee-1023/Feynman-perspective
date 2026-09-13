# Manual fresh-context development protocol

This is a manual development protocol, not the executable runner’s sealed final-release workflow. `defined_before_extraction=false` because the behavioral suite froze after construction began. Keep this qualification in any report.

1. Snapshot the candidate root SKILL.md and permitted references, compute runtime content hash with scripts/validate_package.py --print-hash, and save exact model, settings, tool permissions and a context manifest. Do not edit bytes while collecting a paired trial.
2. Each task-condition gets a new prediction context. Use fork_turns="none" for agent contexts. Provide only the exact task prompt and either the minimal baseline role or the candidate runtime and permitted reference files. Do not provide criteria, commitment metadata, target passages, grading keys, earlier predictions, reviewer commentary, or construction history. If a task context cannot be independent, label that limitation; do not claim it is fresh.
3. Candidate role: the candidate skill with only permitted runtime references. Baseline role: exactly `Think like Richard Feynman. Answer the task.` Use the same model/settings/task facts/tool restrictions. Identity neighbor roles: `Think like Carl Sagan. Answer the task.` and `Think like Karl Popper. Answer the task.` The target has a developed skill while neighbors have minimal roles; report this asymmetry.
4. Save unedited answers and metadata before any grading. Hash each answer file. Do not ask prediction contexts to score themselves.
5. Blind response condition names and randomize presentation to a separate evaluator context. Projection graders may receive the reserved source and rubric only after both answers are saved. Return criterion booleans, 0/1/2 score, rationale, and disputed status. Preserve failure, ambiguity and disagreement.
6. Identity requires at least two distinct reviewer contexts for each anonymous answer. Reviewers receive the same task facts, candidate list and anonymous answer, but never controller-held truth, generation condition, runtime files, or another reviewer’s judgment. Each returns a candidate choice and rationale. These are model reviewers, not a human panel; record model/settings and uncertainty.
7. Development feedback may revise construction. Repeat development only for useful changes, tagging exact new runtime bytes; do not reuse prior scores with new hashes. Final prompts and target collection remain reserved until bytes are stable, and final exposure count must be recorded. Final failure cannot become a pass after tuning against it; retire it if used for revision.
8. This suite supports actual observed manual comparisons, but because pre-extraction behavioral timing failed, do not make a machine-verified-release claim or set the false flag true merely to invoke the runner. Structural draft validation can still be reported honestly.

## Development coverage

- Two projection probes from one independent source episode (Atoms in Motion); report two items and ONE source group.
- Two new-situation reasoning tasks: diagnostic investigation and mathematical problem solving. Each tests concrete method and execution conditions.
- Two pressure tasks: textbook procurement independence and useful curriculum content under sponsor incentives. Each tests a costly choice and resistance to stated pressure.
- Three scope cases: supported-period judgment, earlier-period non-retrojection, and changed conditions with attribution limits.
- Three identity prompts, each answered by target candidate, target minimal baseline, Sagan minimal role and Popper minimal role. Two reviewers per answer. Report target baseline recognition separately.

A cautious rapid development run may select a disclosed subset for curation, but cannot be represented as completion of all required gates.
