from tool_eval_bench.utils.ids import build_run_id


def test_run_id_format() -> None:
    run_id = build_run_id({"a": 1, "b": 2})
    ts, suffix = run_id.split("_", maxsplit=1)
    assert ts.endswith("Z")
    assert len(suffix) == 8  # 8-char hex digest


def test_run_id_unique() -> None:
    """Two calls with identical payload should produce different IDs (random nonce)."""
    id1 = build_run_id({"model": "test", "scenarios": ["TC-01"]})
    id2 = build_run_id({"model": "test", "scenarios": ["TC-01"]})
    assert id1 != id2
