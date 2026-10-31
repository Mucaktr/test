# Prompt Architect & Executor

An agent skill for turning unclear requests into bounded plans, carrying out authorized work, and checking the result.

**Understand → plan → execute → verify.** Keep simple tasks simple; keep consequential actions within the user's authority.

[Read the skill](skills/prompt-architect-executor/SKILL.md) · [Download the package](skills/prompt-architect-executor.zip) · [Türkçe](README.tr.md)

## When to use it

- A request is ambiguous or missing practical acceptance criteria.
- A multi-step task needs a short, verifiable plan.
- You want a reusable instruction workflow, or explicitly ask for a prompt-only result.

## Quick start

1. Read [SKILL.md](skills/prompt-architect-executor/SKILL.md), including its authority and verification limits.
2. Download the ZIP or copy the complete `skills/prompt-architect-executor/` directory.
3. Install it only in a skill location supported by your chosen host, then confirm actual discovery and invocation there. This release does not establish host compatibility.
4. Try a small, read-only task:

```text
Use prompt-architect-executor to clarify this request and review the supplied plan.
Keep the plan short, do not edit files or contact external services, and explain
which acceptance criteria can and cannot be checked from the supplied material.
```

## What is included

| File | Purpose |
|---|---|
| `skills/prompt-architect-executor/SKILL.md` | The unchanged instruction-based workflow. |
| `skills/prompt-architect-executor/README.md` | Package installation overview. |
| `skills/prompt-architect-executor/LICENSE` | MIT license included in the package. |
| `scripts/check_package.py` | Offline ZIP/source parity and packaging checks. |

## Status and limits

**0.1.0-rc2 is a packaging prerelease.** The original repository was named `test`.
The skill instructions were not changed in this publication update. The previously
checked-in ZIP already matched Git's committed `SKILL.md`; an initial working-tree
comparison differed only because of Windows line endings. The new package adds
the license and installation overview. [Release notes](RELEASE-NOTES.md) record this distinction.

The offline checker verifies packaging, not task quality, safe execution, model behavior,
host discovery, or production readiness. Those need separate evidence. Instruction text
does not replace the host's system rules, permission controls, or sandbox.

## Validate the package locally

```text
python -X utf8 scripts/build_package.py
python -X utf8 scripts/check_package.py
```

Questions and improvements: [open an issue](https://github.com/Mucaktr/prompt-architect-executor/issues).
See [contribution guidance](CONTRIBUTING.md) and [security reporting](SECURITY.md).
Licensed under [MIT](LICENSE). The [original installation note](docs/INSTALLATION-NOTE.original.md)
is retained as historical context, not current compatibility evidence.
