# modern-python-example

An example project with the setup described in the blog post
[On modern Python development](https://lervag.github.io/posts/modern-python/):

- [uv](https://docs.astral.sh/uv/) for project and dependency management
- [mise](https://mise.jdx.dev/) to install `uv`, auto-activate the virtual environment, and define tasks
- [ruff](https://docs.astral.sh/ruff/) for formatting and linting
- [pyrefly](https://pyrefly.org/) for type checking
- GitHub Actions to run the checks and tests in CI

## Getting started

With `mise` installed:

```sh
mise trust && mise install
uv sync
mise run check
mise run test
```

## Tasks

- `mise run check` formats, lints (with auto-fix) and type checks the code.
- `mise run check --no-fix` does the same without modifying files, as in CI.
- `mise run test` runs the test suite.
