from automation.src.config import load_settings
from automation.src.runbook import Runbook
from automation.src.report import write_json_report

def main():
    settings = load_settings()  # requires settings.json
    rb = Runbook()

    rb.mark("dr_drill_start", {"project": settings.get("project")})
    rb.mark("config_loaded", {"regions": settings.get("regions")})

    # Placeholder steps (no Azure calls yet)
    rb.mark("simulate_failover_trigger")
    rb.mark("simulate_validation_checks")
    rb.mark("dr_drill_end")

    report = {
        "project": settings.get("project"),
        "regions": settings.get("regions"),
        "targets": settings.get("targets"),
        "events": rb.events
    }

    out = write_json_report(report, "reports/dr_drill_report.json")
    print(f"Report written: {out}")

if __name__ == "__main__":
    main()
