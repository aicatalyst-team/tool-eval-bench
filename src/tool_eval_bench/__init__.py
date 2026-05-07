"""tool_eval_bench package."""

__all__ = ["__version__", "run_benchmark"]
__version__ = "1.5.1"


def run_benchmark(**kwargs):
    """Convenience re-export — see :func:`tool_eval_bench.api.run_benchmark`."""
    from tool_eval_bench.api import run_benchmark as _run

    return _run(**kwargs)

