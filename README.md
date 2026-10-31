# Think with Richard Feynman

I'm Richard Feynman (11 May 1918). You've got the formula, and it gives the right
answer, but the minus sign still bothers you. Good. Let's take one spring. Pull
it to the right. Which way does it pull your hand? Now let it move a little and
keep track of who is doing work on what. We can get somewhere with that. Saying
“restoring force” is useful once we understand what is being restored.

If my explanation doesn't help, tell me exactly where it stops helping. We can
change the example, or find an experiment where the two ideas give different
answers. You don't have to take a statement on my authority, and I don't get to
keep it because I like it. The interesting thing is what nature does.

And there is pleasure in finding out. Knowing something about a flower's cells
and the insects that visit it gives you more to see in the flower. I want to
leave you with something you can look at again, and a question you can work on
yourself.

The strongest support is for introductory scientific explanation in English.
This perspective does not supply Feynman's opinions on today's events or
authenticate quotations; its broader conversational resemblance remains unassessed.


Follow the connection between a physical example, the evidence that can change an explanation, and the pleasure of finding something out.

[Uses](#what-to-bring) · [Getting started](#getting-started) · [Files and loading](#files-and-loading) · [Sources](#sources-and-contributions) · [Scope and status](#scope-and-current-status) · [License](#license)

## What to bring

**Suggested first prompt:**

> Use the Feynman perspective. I can use F = −kx, but I keep forgetting the minus
> sign. If I stretch a spring to the right, whose force points which way—and how
> can the spring's stored energy increase? Help me work it out from one example.

The perspective is designed to keep the same spring in view: which way it pulls,
what the hand does, and whose work enters the energy account. If a step remains
unclear, bring that step back. The aim is to leave with a relation you can use
when the next problem looks different.

Other useful things to bring:

- **Two explanations of one result.** Work out where their predictions differ
  and what observation could separate them. A disagreement also calls for checking
  the apparatus and the calculation.
- **A claim that a system is reliable.** Examine the tested conditions, damage
  and missing evidence. A history of survival may leave the failure mechanism
  unexplained; a changed design deserves a fresh investigation.
- **A lesson that has become a vocabulary exercise.** Find something the learner
  can actually do with the idea. Keep a precise definition when it resolves a
  difficulty, and allow a correct route even when it is slow.
- **A conclusion you would like to believe.** Look for the awkward observation
  and give the favorable result the same scrutiny. Expect some resistance to
  reassurance that has not earned its confidence.

Questions about curiosity, learning and the pleasure of discovery fit here as
well. The approach can investigate consequences and clarify a choice; it cannot
derive what a life should be devoted to from a physical law.

## Getting started

```sh
git clone https://github.com/ariel-lee-1023/Feynman-perspective.git feynman-perspective
```

Open the cloned folder as an agent workspace. Its [AGENTS.md](AGENTS.md) activates
the local Feynman perspective; explicit requests to change voice or maintain the files
take precedence. For another skill host, install the root under `feynman-perspective`.
Invoke `feynman-perspective` through your host's skill selector, or ask it to use this perspective with one of the situations above.

Responses default to **English**. Explicitly request another language, for example
“Answer in Chinese for this conversation,” to change it for that scope. A message
written in another language alone does not change the default.

### Loading and manual configuration

Before the first substantive response, including a short answer, read the complete
[core](SKILL.md), [voice](references/voice.md) and [frameworks](references/frameworks.md).
The core alone is incomplete. Keep complete texts already in context and reload any
lost after compaction. Add relevant topic or work modules as the question requires.
For a chat without file access, supply those three complete texts and the relevant
module yourself. Maintenance and assessment records are not ordinary conversation inputs.

## Files and loading

These are file responsibilities and loading relationships, not a fixed sequence of thought.

| File or entry | What it provides | When it is used |
| --- | --- | --- |
| [Core](SKILL.md) | Perspective, language and operating instructions | Read in full at setup |
| [Voice](references/voice.md) | Expression, register and interaction | Read in full at setup |
| [Frameworks](references/frameworks.md) | Concepts, methods and conditional judgments | Read in full at setup |
| [Topic and source modules](references/clusters/) | Evidence, examples and work-specific distinctions | Load when relevant to the question |
| [Maintenance records](transworld-identity/) | Provenance, editorial history and assessment evidence | Outside the ordinary conversation prompt |
| [.agents/skills/feynman-perspective](.agents/skills/feynman-perspective) | Relative symlink to the repository root | Host discovery; not a second runtime copy |

## Sources and contributions

The record combines Richard Feynman's lectures, public statements, edited interviews
and memoirs. This table connects their contributions to questions you can bring;
repeated tellings of the same episode do not provide independent corroboration.

| Question or concern | Source and period | Contribution and working reference |
| --- | --- | --- |
| What would make an explanation wrong? | *The Character of Physical Law*, Cornell lectures (1964) | Guessing, deriving consequences and checking both calculation and experiment. [Physical law](references/clusters/c13-seeking-new-laws.md) |
| What does a formula let a learner do? | *Six Easy Pieces*, from the 1961–1963 teaching; *Feynman's Tips on Physics*, supplementary lectures of 1961–1962 | Physical signs, prerequisites and usable examples. [Problem solving](references/clusters/c16-problem-solving.md) |
| When does notation obscure the task? | “New Textbooks for the ‘New’ Mathematics” (1965) | Criticism of the inspected elementary materials, not a ban on formal mathematics. [Mathematics education](references/clusters/c17-newmath.md) |
| What has actually been inspected? | *Surely You're Joking, Mr. Feynman!* (1985); *What Do You Care What Other People Think?* (1988), recounting earlier events | Curiosity, prestige and the limits of endorsement. [Memoir](references/clusters/c01-c03-c05-memoir.md) |
| What must a reassuring report disclose? | Scientific-integrity address (1974), reprinted in *Surely You're Joking*; Challenger inquiry (1986), in *What Do You Care* and *The Pleasure of Finding Things Out* | Controls, contrary evidence and the difference between survival and explained safety. [Integrity](references/clusters/c04-cargo-cult.md); [Challenger](references/clusters/c06-c11-challenger.md) |
| Does understanding diminish wonder? | *The Pleasure of Finding Things Out*: 1955 address and 1979–1981 interview material | Beauty, motivation and uncertainty; reflection does not itself establish a separately calibrated conversational voice. [Interviews](references/clusters/c07-c10-interviews.md) |

Editors' remarks, student questions, Matthew Sands's memoir and the exercise authors'
contributions are distinguished from Feynman's speech. Exact editions and the source
inventory are in [provenance](transworld-identity/provenance.md). Contemporary uses of
these methods are applications, not new historical opinions.

## Scope and current status

*This introduction is a newly written, source-grounded persona reconstruction,
not a historical quotation. [Editorial and birth-date notes](transworld-identity/provenance.md#readme-editorial-review-2026-10-30).*

**The working version remains a Candidate.** Machine recognition has not been run.
Package checks establish structure and links; the bounded source checks for version 1.0
remain evidence for their original inputs. They do not certify the later full runtime.
Earlier comparisons did not establish improvement over a minimal Feynman prompt, and
broader conversational resemblance remains unassessed.

The represented public record spans 1955–1986, with teaching from 1961–1963 and memoirs
published in 1985 and 1988 about earlier events. English introductory scientific
explanation has the strongest voice support. Other languages can be requested, but
Chinese conversational resemblance has not been evaluated. Present-day factual
questions require current evidence; exact quotations require the relevant source.
Science can investigate consequences without deciding what a life should value.

See [reconstruction scope](transworld-identity/scope.md), the
[assessment record](transworld-identity/validation.json), [release history](CHANGELOG.md)
and [maintenance notes](transworld-identity/provenance.md#maintenance-checks).
Tag `1.0` preserves the published Candidate snapshot. The historical README reorganization renewed no assessment result; the current core
revision has separate applicability notes below.

**The revised runtime is a Candidate without a new recognition assessment.** This
maintenance preserves the existing material while aligning persona prose, host rules
and the placement of the introduction notice. See the [maintenance record](transworld-identity/provenance.md#skill-and-readme-alignment-2026-10-31)
for the checked scope and any pre-existing package issues. No new tests were added.

## License

The [MIT license](LICENSE) covers original repository material, not the source books
or scans, which are not distributed. See [NOTICE](NOTICE.md) for source-rights exclusions.
