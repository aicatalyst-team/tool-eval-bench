# PoC Plan: tool-eval-bench

## Project Classification
- **Type:** llm-app (evaluation/benchmarking tool for LLM serving stacks)
- **Key Technologies:** Python, httpx, rich, OpenAI-compatible API
- **ODH Relevance:** Validates tool-calling quality of model serving endpoints, directly relevant to Red Hat AI Inference Server and vLLM evaluation workflows

## PoC Objectives
1. Prove that tool-eval-bench can be containerized with UBI images and run on OpenShift
2. Validate that the CLI tool installs correctly and produces help output in a containerized environment
3. Demonstrate the benchmark can be packaged as a Kubernetes Job for batch evaluation workflows

## Infrastructure Requirements
- **Resource Profile:** small (256Mi RAM, 250m CPU)
- **GPU Required:** no
- **Persistent Storage:** none
- **Sidecar Containers:** none
- **Deployment Model:** job (CLI tool, runs to completion)
- **Listens on Port:** false
- **Needs LLM API:** false (for basic validation; production use requires an OpenAI-compatible endpoint)

## Test Scenarios

### Scenario 1: help-output
- **Description:** Verify the CLI tool installs correctly and shows usage information
- **Type:** cli
- **Input:** `tool-eval-bench --help`
- **Expected:** Exits 0, shows usage info with scenario categories and options
- **Timeout:** 30 seconds

### Scenario 2: version-check
- **Description:** Verify the package version is accessible
- **Type:** cli
- **Input:** `python -c "from tool_eval_bench import __version__; print(__version__)"`
- **Expected:** Exits 0, prints version string (e.g., "2.0.6")
- **Timeout:** 15 seconds

### Scenario 3: module-import
- **Description:** Verify all core modules can be imported without errors
- **Type:** cli
- **Input:** `python -c "from tool_eval_bench.api import run_benchmark; from tool_eval_bench.evals.scenarios import ALL_SCENARIOS; print(f'{len(ALL_SCENARIOS)} scenarios loaded')"`
- **Expected:** Exits 0, prints scenario count
- **Timeout:** 15 seconds

## Dockerfile Considerations
- Use `registry.access.redhat.com/ubi9/python-312` base image
- Install from pyproject.toml using pip
- Set ENTRYPOINT to `tool-eval-bench`
- No port exposure needed (CLI tool)
- No GPU packages required

## Deployment Considerations
- Deploy as a Kubernetes Job (not Deployment) since this is a CLI tool
- Each test scenario runs as a separate Job
- No Service resource needed (no network port)
- No LLM endpoint required for basic validation tests
