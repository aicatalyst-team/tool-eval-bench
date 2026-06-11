#!/usr/bin/env python3
"""AutoPoC Test Script for tool-eval-bench (CLI/Job-based testing)."""
import json
import os
import subprocess
import sys
import time

NAMESPACE = os.environ.get("POC_NAMESPACE", "poc-tool-eval-bench")
results = []


def run_job_test(scenario_name, job_name, expected_content=None, timeout=120):
    """Check if a Kubernetes Job completed successfully and validate its output."""
    start = time.time()
    try:
        # Check job status
        status_cmd = [
            "kubectl", "get", "job", job_name, "-n", NAMESPACE,
            "-o", "jsonpath={.status.succeeded}"
        ]
        status_result = subprocess.run(status_cmd, capture_output=True, text=True, timeout=30)
        succeeded = status_result.stdout.strip()

        # Get logs
        logs_cmd = ["kubectl", "logs", f"job/{job_name}", "-n", NAMESPACE]
        logs_result = subprocess.run(logs_cmd, capture_output=True, text=True, timeout=30)
        output = logs_result.stdout[:2000]

        if succeeded == "1":
            if expected_content and expected_content not in output:
                r = {
                    "scenario_name": scenario_name,
                    "status": "fail",
                    "output": output,
                    "error_message": f"Expected '{expected_content}' not in output",
                    "duration_seconds": round(time.time() - start, 2),
                }
            else:
                r = {
                    "scenario_name": scenario_name,
                    "status": "pass",
                    "output": output,
                    "error_message": None,
                    "duration_seconds": round(time.time() - start, 2),
                }
        else:
            r = {
                "scenario_name": scenario_name,
                "status": "fail",
                "output": output,
                "error_message": f"Job did not succeed. Status: {status_result.stdout}",
                "duration_seconds": round(time.time() - start, 2),
            }
    except Exception as e:
        r = {
            "scenario_name": scenario_name,
            "status": "error",
            "output": "",
            "error_message": str(e),
            "duration_seconds": round(time.time() - start, 2),
        }

    results.append(r)
    return r


# === SCENARIOS ===

# Scenario 1: Help output
print("Testing help-output...", file=sys.stderr)
run_job_test("help-output", "tool-eval-bench-help", expected_content="tool-eval-bench")

# Scenario 2: Version check
print("Testing version-check...", file=sys.stderr)
run_job_test("version-check", "tool-eval-bench-version", expected_content="2.0.6")

# Scenario 3: Module import
print("Testing module-import...", file=sys.stderr)
run_job_test("module-import", "tool-eval-bench-import", expected_content="scenarios loaded")

# === END SCENARIOS ===

print(json.dumps({"results": results}, indent=2))
sys.exit(1 if any(r["status"] in ("fail", "error") for r in results) else 0)
