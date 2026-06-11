# RHOAI Evaluation: tool-eval-bench

## Project Summary
A tool-calling quality benchmark for evaluating LLM tool-use in agentic workflows across open-weight model serving stacks (vLLM, LiteLLM, llama.cpp). Runs 69 deterministic scenarios through OpenAI-compatible /chat/completions endpoints.

## Strategy Alignment
- **Primary Strategy Area:** agentic-ai (tool-calling evaluation)
- **Secondary Strategy Area:** model-inference (validates serving quality)
- **Relationship:** validates-platform-story

## Impact Dimensions

| Dimension | Score (0-20) | Rationale |
|---|---|---|
| audience_value | 16 | ML engineers and platform teams evaluating model serving quality need standardized benchmarks. Strong developer audience. |
| strategic_alignment | 15 | Directly validates tool-calling quality of inference servers, a key differentiator for Red Hat AI Inference Server. |
| strategy_fit | 14 | Maps to agentic-ai capability labels (tool-calling) and model-inference (vllm, serving, model-validation). |
| platform_leverage | 12 | CLI tool that can run against any OpenAI-compatible endpoint. Moderate platform leverage - validates platform capabilities. |
| demo_potential | 13 | Clear benchmark output with scores and categories. Visual report generation. Good for demos. |

**Impact Score:** 14.0

## Feasibility Dimensions

| Dimension | Score (0-20) | Rationale |
|---|---|---|
| container_readiness | 16 | Pure Python, standard pip dependencies (httpx, rich, python-dotenv). No Dockerfile but straightforward to containerize. |
| dependency_profile | 17 | Minimal dependencies: httpx, rich, python-dotenv. No ML frameworks, no GPU required. |
| reproduction_confidence | 15 | Well-structured project with tests, CI, clear entry points. Easy to reproduce. |
| complexity_sweet_spot | 14 | Single component CLI tool. Needs an LLM endpoint to benchmark against, but that's the whole point. |

**Feasibility Score:** 15.5

## Strengths
- Clean Python package with well-defined entry points
- Minimal dependencies, no GPU required
- Tests LLM tool-calling quality - directly relevant to RHOAI inference story
- MIT license - no restrictions
- Active development with comprehensive test suite

## Risks
- CLI tool, not a web service - needs to be run as a Job, not a Deployment
- Requires an external LLM endpoint to benchmark against
- No existing Dockerfile
