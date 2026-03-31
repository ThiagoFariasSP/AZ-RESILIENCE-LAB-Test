"""
AZ-RESILIENCE-LAB-Test
Failure Simulation Script

Purpose:
- Simulate an application failure (logical trigger only)
- No Azure resources are touched
"""

from datetime import datetime, timezone


def simulate_application_failure():
    failure_time = datetime.now(timezone.utc)

    print("=== FAILURE SIMULATION ===")
    print("Simulating critical application failure (logical trigger only)")
    print(f"Failure time (UTC): {failure_time.isoformat()}")

    # Logical failure signal
    failure_detected = True

    if not failure_detected:
        raise RuntimeError("Failure simulation did not trigger as expected.")

    print("Failure successfully simulated.")
    return failure_time
