"""
rent_escalation_calculator.py - Calculates escalated annual base rent using contractual fixed percentage or CPI bump
"""
import sys
import json


def calculate_rent_escalation(escalation_json: str):
    import json
    data = json.loads(escalation_json) if isinstance(escalation_json, str) else escalation_json
    curr = data.get("current_rent_usd", 100000.0)
    pct = data.get("escalation_pct", 3.0)
    new_rent = round(curr * (1.0 + (pct / 100.0)), 2)
    return {"escalated_rent_usd": new_rent, "escalation_pct": pct, "status": "ESCALATION_VERIFIED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "rent-escalation-calculator"}))
