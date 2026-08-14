# Contributing to VigilMesh

Thanks for helping improve this early-stage project. We value small,
reviewable changes and honest descriptions of current behavior.

## Before opening a change

1. Search existing issues and open a focused issue for a substantial design.
2. Do not include secrets, private datasets, account information, or code that
   requires undocumented credentials.
3. Keep providers and alert channels behind the public protocols in
   `src/vigilmesh/interfaces.py`.
4. Add or update tests for behavioral changes.

## Local workflow

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m unittest discover -s tests -v
python -m compileall -q src tests
```

Use a short branch name and explain what changed, why it changed, and how it
was tested in the pull request. Keep unrelated formatting changes out of the
same PR.

## Good first contributions

Documentation fixes, additional deterministic provider fixtures, tests for
edge cases, and improvements to error messages are excellent starting points.
Please discuss changes to public interfaces before implementing them.

## Community expectations

By participating, you agree to follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
Security problems should follow [SECURITY.md](SECURITY.md), not a public issue.

