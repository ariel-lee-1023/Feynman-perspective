# feynman-perspective

A distilled **perspective skill** for Claude: reason and explain in Richard Feynman's frame.

Check every claim against what actually happens rather than who says it. Work from a concrete
example you can picture. Translate inflated language back into plain words. Refuse false
certainty. Treat understanding a thing as adding to its wonder rather than subtracting from it.

---

## What this is

A [Claude Skill](https://docs.claude.com) — a `SKILL.md` plus a `references/` package that a host
agent loads on demand. The core file carries the persona in first-person voice at roughly 1.9k
tokens; the reference modules carry register-specific detail, worked argumentative procedures, and
the honesty ledger.

It was built by distilling ~444,000 words of Feynman's published work into 24 core elements scored
on projectibility, cost-bearing refusals, expressive match, interactional moves, and preoccupations.
The distillation method and the audit trail are documented in
[`fidelity-ledger/provenance.md`](fidelity-ledger/provenance.md).

## Installation

**Claude Code / Claude Desktop (personal skill):**

```bash
git clone https://github.com/ariel-lee-1023/feynman-perspective.git
mkdir -p ~/.claude/skills
cp -r feynman-perspective ~/.claude/skills/
```

**Project-scoped:** copy the folder into `.claude/skills/` inside your project.

**claude.ai:** zip the folder and upload it via Settings → Capabilities → Skills.

The skill directory name must match the `name` field in the `SKILL.md` frontmatter
(`feynman-perspective`).

## Usage

The skill triggers on its own when a task fits its description — scientific method, evaluating a
claim, explaining something to a beginner, auditing confident institutional language, cutting
jargon. You can also invoke it explicitly:

```
Use the feynman-perspective skill: our incident review says the system has 99.99% availability.
Pull that apart.
```

```
Explain gradient descent in the feynman-perspective frame — concrete case first, no jargon.
```

Good fits:

- **Auditing a confident claim.** Asymmetric-scrutiny check, demand the number rather than the
  methodology, read the wording for what temperature it stops being true at.
- **Risk under uncertainty.** A survived anomaly is a warning, not a reassurance.
- **Teaching and documentation.** Clear beats precise; added precision can *lower* clarity.
- **Research and analysis quality.** Leaning over backwards, replication before variation, naming
  the specific missing check rather than sneering "cargo cult."

## Repository layout

```
feynman-perspective/
├── SKILL.md                          # the core persona (always loaded)
├── references/                        # host-agent-facing, loaded at runtime, never contains
│   │                                #   provenance or episodic material
│   ├── frameworks.md                 # his named constructs, defined
│   └── clusters/                     # register modules, loaded on demand
│       ├── c01-c03-c05-memoir.md     #   narrative/storytelling voice
│       ├── c04-cargo-cult.md         #   scientific integrity, self-deception
│       ├── c06-c11-challenger.md     #   institutional critique, risk, dissent
│       ├── c07-c10-interviews.md     #   reflective spoken voice (doubt, wonder)
│       ├── c13-seeking-new-laws.md   #   method, authority vs. evidence
│       ├── c17-newmath.md            #   teaching, clarity, jargon
│       ├── manifest.json             #   17-cluster corpus segmentation
│       └── coverage_map.json         #   domain/temporal coverage
├── fidelity-ledger/                    # human-facing, never loaded by the host agent
│   ├── provenance.md                 # source map, fidelity gates, where to trust it less
│   ├── episodic.md                   # lower-priority colour + coverage limits
│   ├── extractions.json              #   the extracted elements
│   ├── scores.json                   #   scoring and core/reference decisions
│   └── fidelity.json                 #   projection, cost, and style gate results
├── CHANGELOG.md
├── LICENSE
├── NOTICE.md
└── .github/workflows/validate.yml    # frontmatter + JSON sanity check
```

Nothing in `fidelity-ledger/` is needed at runtime. It ships so the claims in the README are
checkable rather than asserted — which is rather the point of the skill.

## How faithful is it?

Measured, not asserted. Full numbers in [`fidelity-ledger/provenance.md`](fidelity-ledger/provenance.md);
the summary:

| Domain | Projection score |
|---|---|
| Epistemology / method / authority | 0.98 |
| Scientific integrity, not fooling yourself | 0.95 |
| Teaching, clarity, jargon | 0.92 |
| Institutional critique (risk, overconfidence) | 0.90 |
| Reflective personal philosophy (doubt, wonder) | 0.85 |
| Physics detail beyond the famous set-pieces | 0.55 |
| Politics, economics, social theory | out of scope |

The **projection gate** masks a fraction of the extracted stances and asks whether the remainder
predicts them; it scored 1.00 pre-assembly, 0.90 on the assembled core. The **cost gate** requires
that every attested case where Feynman paid a price for a commitment survives into the core; all
8 did. The **style gate** checks that sentence-length shape and register modulation match the
originals rather than flattening into one voice.

## Scope and limits

- **Strong on how he thinks and argues** — method, authority, integrity, clarity, risk, wonder.
- **Weak as a source of physics content** beyond the famous set-pieces. Don't use it as a textbook.
- **Silent on organized politics, economics, and social theory.** The corpus is silent there, and
  that silence is itself in character. Don't push it.
- **Memoir dialogue is reconstructed**, not verbatim transcript — faithful in spirit only.
- **No forged quotations.** The skill explicitly instructs against presenting invented statements as
  Feynman's real words. If you need a real quote, go to the source and cite it.

## Sources and copyright

The persona was distilled from seven published works: *Surely You're Joking, Mr. Feynman!*, *What Do
You Care What Other People Think?*, *The Pleasure of Finding Things Out*, *The Character of Physical
Law*, *Six Easy Pieces*, *Feynman's Tips on Physics*, and the 1965 essay "New Textbooks for the
'New' Mathematics."

**The corpus itself is not distributed here and never will be.** Those works remain in copyright.
This repository contains only original analytical description of patterns of reasoning, register,
and argumentative structure — the kind of thing a critical essay contains. Cluster modules
deliberately paraphrase rather than quote, and the memoir module states outright that its material
must not be used as a quotation source.

Richard Feynman's name and works are the property of their respective rights holders. This project
is unaffiliated with and unendorsed by the Feynman estate, Caltech, or any publisher.

## Contributing

Issues and pull requests are welcome. Two rules, both inherited from the subject:

1. **Say which check is missing.** A report that the persona sounds off should name the specific
   move it got wrong or the source it contradicts — not just "this doesn't feel like him."
2. **Lean over backwards.** If you propose an addition, include what argues against it: the cluster
   where he does the opposite, the register where it wouldn't apply.

Changes to `SKILL.md` should say which element in `fidelity-ledger/scores.json` they refine, and
whether any gate is affected.

## License

MIT © 2026 Ariel Lee. [See LICENSE](LICENSE).

This license covers the original text in this repository. It does not extend to any referenced source books, which remain the property of their respective copyright holders.

