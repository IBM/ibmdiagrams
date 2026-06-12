# Contributing

Found a bug or need an additional feature? File an issue in this repository with the following information and they will be responded to in a timely manner.

## Bugs

- A detailed title describing the issue with the current release and the tag `[BUG]`. For sprint one, filing a bug would have the title `[0.1.0][BUG] <issue title>`
- Steps to recreate said bug (including non-sensitive variables)
- (optional) Corresponding output logs **as text or as part of a code block**
- Tag bug issues with the `bug` label
- If you come across a vulnerability that needs to be addressed immediately, use the `vulnerability` label


## Features

- A detailed title describing the desired feature that includes the current release. For sprint one, a feature would have the title `[0.1.0] <feature name>`
- A detailed description including the user story
- A checkbox list of needed features
- Tag the issue with the `enhancement` label

Want to work on an issue? Be sure to assign it to yourself and branch from main. When you're done making the required changes, create a pull request.

## Pull requests

## Development Setup

### Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality and security. The hooks run automatically before each commit.

**Installation:**

```bash
# Install pre-commit (if not already installed)
pip install pre-commit

# Or with uv
uv pip install pre-commit

# Install the git hooks
pre-commit install
```

**Configured Hooks:**

1. **Ruff** - Fast Python linter and formatter
   - Automatically fixes issues when possible
   - Enforces code style consistency

2. **Detect Secrets** - Prevents committing sensitive information
   - Scans for API keys, passwords, tokens, etc.
   - Uses baseline file (`.secrets.baseline`) for known false positives

**Manual Execution:**

```bash
# Run all hooks on all files
pre-commit run --all-files

# Run specific hook
pre-commit run ruff --all-files
pre-commit run detect-secrets --all-files

# Skip hooks for a commit (use sparingly)
git commit --no-verify
```

**Updating Secrets Baseline:**

If detect-secrets flags a false positive:

```bash
# Regenerate the baseline
detect-secrets scan > .secrets.baseline

# Or update with new findings
detect-secrets scan --baseline .secrets.baseline
```

## Testing

Before submitting a pull request:

1. **Run visual regression tests**: Ensure diagram rendering hasn't changed unintentionally
   ```bash
   pytest tests/test_visual_regression.py -v
   pytest tests/test_complete_diagrams.py -v
   ```

2. **Run all tests**: Verify all test suites pass
   ```bash
   pytest tests/ -v
   ```

3. **Update baselines if needed**: If you've intentionally changed diagram rendering
   ```bash
   # Update element baselines
   pytest tests/test_visual_regression.py --update-baselines
   
   # Update complete diagram baselines
   pytest tests/test_complete_diagrams.py --update-baselines

   # Update specific diagram baseline
   pytest tests/test_complete_diagrams.py::test_slzpowervs_diagram --update-baselines -v
   ```

4. **Commit baseline changes**: Include updated baseline files with clear explanation
   ```bash
   git add tests/baselines/
   git commit -m "Update visual regression baselines: [describe changes]"
   ```

See [docs/testing.md](docs/testing.md) for detailed testing documentation.

**Do not merge directly to main**. Pull requests should reference the corresponding issue filed in this repository. Please be sure to maintain **code coverage** before merging.

At least **two** reviews are required to merge a pull request. When creating a pull request, please ensure that details about unexpected changes to the codebase are provided in the description.
