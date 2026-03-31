from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

@dataclass
class Runbook:
    """
    Records DR drill / failover steps with timestamps.
    This becomes the basis for RTO measurement.
    """
    events: list[dict[str, Any]] = field(default_factory=list)

    def mark(self, name: str, details: dict[str, Any] | None = None) -> None:
        self.events.append({
            "event": name,
            "time_utc": utc_now(),
            "details": details or {}
        })
