# Blog Abstract: tool-eval-bench on OpenShift

## Thesis
Deploying tool-eval-bench on OpenShift proves that Python-based LLM evaluation tools can be containerized with UBI images and run as batch workloads alongside the models they evaluate, enabling standardized model quality gates in enterprise AI platforms.

## Target Audience
Platform engineers and ML engineers evaluating model serving quality on Red Hat OpenShift AI.

## Blog Type
Red Hat Developer Blog

## Key Points
1. tool-eval-bench provides 69 deterministic test scenarios for LLM tool-calling quality, filling a critical gap in model validation workflows
2. Containerizing with UBI9 and deploying as Kubernetes Jobs demonstrates the batch evaluation pattern for OpenShift AI
3. Integrating benchmarks into the deployment pipeline creates automated quality gates for model serving endpoints

## Products/Projects
- Red Hat OpenShift AI
- Open Data Hub
- Red Hat AI Inference Server (vLLM)
- UBI9 container images

## CTA
Try deploying tool-eval-bench against your own model serving endpoint on OpenShift AI.

## Proposed Section Outline
1. What is tool-eval-bench?
2. Why tool-calling quality matters for enterprise AI
3. Containerizing for OpenShift with UBI
4. Deploying as batch evaluation Jobs
5. Test results and what they tell us
6. Building automated model quality gates
7. Try it yourself
