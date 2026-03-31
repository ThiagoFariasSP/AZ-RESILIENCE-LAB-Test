"""
AZ-RESILIENCE-LAB-Test
Failure Simulation Script

Purpose:
- Simulate an application failure
- Act as the trigger point for a Disaster Recovery drill
- Record when the failure occurred
"""

from datetime import datetime, timezone
import sys


def simulate_application_failure():
    """
    Simulates a critical application failure.
    No Azure resources are touched.
    This represents the moment an incident starts.
    """

    failure_time = datetime.now(timezone.utc)

    print("=== FAILURE SIMULATION STARTED ===")
    print("Simulating critical application failure...")
    print(f"Failure time (UTC): {failure_time.isoformat()}")

    # Logical failure signal
    failure_detected = True

    if not failure_detected:
        print("Failure simulation failed to trigger.")
        sys.exit(1)

    print("Failure successfully simulated.")
    print("This would trigger the Disaster Recovery process.")

    return failure_time


def main():
    print("Starting DR drill - failure simulation phase")
    simulate_application_failure()
    print("Failure simulation phase completed")


if __name__ == "__main__":
    main()
``
