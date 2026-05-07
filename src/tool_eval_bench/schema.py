"""Machine-readable argument schema for tool-eval-bench.

Consumed by external integrators (e.g. sparkrun recipe validation) to
validate ``benchmark.args`` without running the CLI.

Usage::

    from tool_eval_bench.api import ARGS_SCHEMA
    # or
    from tool_eval_bench.schema import ARGS_SCHEMA

The schema is a list of dicts, one per argument, with type, default,
choices, and description.  This is NOT JSON Schema — it's a lightweight
format optimized for recipe validation and CLI introspection.
"""

from __future__ import annotations

from typing import Any


# Argument schema version — bump when adding/removing/renaming args.
SCHEMA_VERSION = "1"

ARGS_SCHEMA: list[dict[str, Any]] = [
    # -- Connection --
    {
        "name": "backend",
        "type": "string",
        "default": "vllm",
        "choices": ["vllm", "litellm", "llamacpp"],
        "description": "Backend label for reports",
    },
    # -- Sampling --
    {
        "name": "temperature",
        "type": "float",
        "default": 0.0,
        "description": "Sampling temperature (0.0 = greedy)",
    },
    {
        "name": "no_think",
        "type": "bool",
        "default": False,
        "description": "Disable thinking/reasoning (sets enable_thinking=false)",
    },
    {
        "name": "top_p",
        "type": "float",
        "default": None,
        "description": "Top-p (nucleus) sampling",
    },
    {
        "name": "top_k",
        "type": "int",
        "default": None,
        "description": "Top-k sampling",
    },
    {
        "name": "min_p",
        "type": "float",
        "default": None,
        "description": "Min-p sampling threshold",
    },
    {
        "name": "repeat_penalty",
        "type": "float",
        "default": None,
        "description": "Repetition penalty",
    },
    {
        "name": "seed",
        "type": "int",
        "default": None,
        "description": "Random seed (passed to server)",
    },
    # -- Scenario selection --
    {
        "name": "scenarios",
        "type": "list[string]",
        "default": None,
        "description": "Specific scenario IDs to run (e.g. TC-01 TC-07)",
    },
    {
        "name": "categories",
        "type": "list[string]",
        "default": None,
        "choices": list("ABCDEFGHIJKLMNOP"),
        "description": "Run only specific categories (A–P)",
    },
    {
        "name": "short",
        "type": "bool",
        "default": False,
        "description": "Run only the core 15 scenarios",
    },
    {
        "name": "hardmode",
        "type": "bool",
        "default": False,
        "description": "Include Hard Mode scenarios (Category P)",
    },
    # -- Run control --
    {
        "name": "timeout",
        "type": "float",
        "default": 60.0,
        "description": "Request timeout in seconds",
    },
    {
        "name": "max_turns",
        "type": "int",
        "default": 8,
        "description": "Max turns per scenario",
    },
    {
        "name": "trials",
        "type": "int",
        "default": 1,
        "description": "Number of trial runs for statistical rigor",
    },
    {
        "name": "parallel",
        "type": "int",
        "default": 1,
        "description": "Run N scenarios concurrently (1 = sequential)",
    },
    {
        "name": "error_rate",
        "type": "float",
        "default": 0.0,
        "min": 0.0,
        "max": 1.0,
        "description": "Inject random tool errors at this rate for robustness testing",
    },
    {
        "name": "no_warmup",
        "type": "bool",
        "default": False,
        "description": "Skip server warm-up request",
    },
    {
        "name": "reference_date",
        "type": "string",
        "default": None,
        "description": "Override benchmark reference date (YYYY-MM-DD)",
    },
    # -- Output --
    {
        "name": "alpha",
        "type": "float",
        "default": 0.7,
        "min": 0.0,
        "max": 1.0,
        "description": "Quality/speed weight for deployability score",
    },
    {
        "name": "no_probe_engine",
        "type": "bool",
        "default": False,
        "description": "Skip inference engine probing",
    },
    {
        "name": "redact_url",
        "type": "bool",
        "default": False,
        "description": "Mask the server URL in reports",
    },
    # -- Context pressure --
    {
        "name": "context_pressure",
        "type": "float",
        "default": None,
        "min": 0.0,
        "max": 1.0,
        "description": "Fill context to this ratio before each scenario",
    },
    {
        "name": "context_size",
        "type": "int",
        "default": None,
        "description": "Override auto-detected context window size (tokens)",
    },
]


def get_schema() -> dict[str, Any]:
    """Return the full args schema with version metadata."""
    return {
        "schema_version": SCHEMA_VERSION,
        "args": ARGS_SCHEMA,
    }
