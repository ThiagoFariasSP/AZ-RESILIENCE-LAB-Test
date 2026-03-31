"""
AZ-RESILIENCE-LAB-Test
DR Drill Orchestrator

Purpose:
- Orchestrate a DR Drill workflow (step-by-step runbook)
- Today: Failure simulation only
- Next: Add validation + reporting + real Azure actions (later phases)

This aligns with the project scope: "Automação de testes de DR (DR Drill)". 
"""

from datetime import datetime, timezone
from simulate_failure import simulate_application_failure


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def main():
    print("=== DR DRILL START ===")
    drill_start = utc_now()
    print(f"DR Drill start time (UTC): {drill_start}")

    # Step 1 - Trigger failure (logical)
    failure_time = simulate_application_failure()

    # Future steps (not implemented yet, by design)
    print("=== NEXT STEPS (PLACEHOLDERS) ===")
    print("- Post-failover validation (later)")
    print("- RTO/RPO measurement (later)")
    print("- Reporting (later)")

    drill_end = utc_now()
    print(f"DR Drill end time (UTC): {drill_end}")
    print("=== DR DRILL END ===")


if __name__ == "__main__":
    main()
``
