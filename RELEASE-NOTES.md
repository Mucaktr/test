# 0.1.0-rc2 — Canonical package text

The first publication CI failed because LICENSE and the package README had Windows CRLF bytes inside the ZIP while Git stored LF source bytes. The skill core itself already matched.

RC2 adds an explicit LF package builder with fixed ZIP metadata, rebuilds the package, and keeps the exact source/archive check. This is a packaging correction, not a new skill behavior acceptance.

The original failed CI is preserved: https://github.com/Mucaktr/prompt-architect-executor/actions/runs/41209596532 . RC1 tag/assets remain unchanged.

# 0.1.0-rc1 — Packaging prerelease

- Public identity changes from `test` to `prompt-architect-executor`.
- Add English/Turkish overviews, MIT licensing, contribution and security guidance.
- Preserve the current `SKILL.md` bytes; no instruction behavior change.
- Rebuild the ZIP from the current source, including the license and package README.
- Add an offline source/archive parity check.

## Source and archive verification

Git's committed SKILL.md and SKILL.md inside the old ZIP both had SHA-256
`7ae4475856c6ca4de82c1ef3eec31e1e1942a952bc63e6a6aee18d1bc803513b`.
The first comparison used a Windows checkout with CRLF line endings (SHA-256
`6d44776d0b86b477fc85ec1827d964106bee38ba4052e8957feb13b925f7f085`);
it was a representation difference, not a different skill version. Canonical Git
bytes and the previous ZIP matched exactly. This update enforces LF for text and
adds the MIT license and package overview. The checker requires exact byte parity.

## Evidence boundary

Package checks verify archive integrity, required files and exact source parity.
No native host discovery, model execution, approval UI, behavior acceptance, or
production-security test is claimed by this release.
