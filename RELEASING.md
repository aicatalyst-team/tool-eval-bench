# Releasing tool-eval-bench

Checklist for publishing a new release.

## Pre-release

1. **Update version strings** (all three MUST match):
   ```bash
   # pyproject.toml → version = "X.Y.Z"
   # src/tool_eval_bench/__init__.py → __version__ = "X.Y.Z"
   # CHANGELOG.md → ## [X.Y.Z] — YYYY-MM-DD
   ```

2. **Lint and test**:
   ```bash
   ruff check .
   .venv/bin/python -m pytest tests/ --ignore=tests/test_llama_benchy.py
   ```

3. **Build wheel and sdist**:
   ```bash
   pip install build
   python -m build
   ```

4. **Install smoke test**:
   ```bash
   pip install dist/tool_eval_bench-*.whl
   tool-eval-bench --version
   tool-eval-bench --help
   ```

5. **Verify pip check**:
   ```bash
   pip check
   ```

## Tagging

```bash
git add -A
git commit -m "release: vX.Y.Z"
git tag vX.Y.Z
git push origin main --tags
```

## Publishing (optional)

```bash
pip install twine
twine upload dist/*
```

## Post-release

- Add a new `## [Unreleased]` section at the top of `CHANGELOG.md`
- Bump version to next dev version if desired (e.g. `X.Y.Z+1.dev0`)

## Live Certification (recommended before major releases)

Run the full benchmark against at least one backend to verify deployment
compatibility:

```bash
# vLLM
tool-eval-bench --backend vllm --base-url http://localhost:8000

# llama.cpp
tool-eval-bench --backend llamacpp --base-url http://localhost:8080

# LiteLLM
tool-eval-bench --backend litellm --base-url http://localhost:4000
```
