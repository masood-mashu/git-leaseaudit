"""
cam_reconciliation_auditor.py - Audits landlord operating expenses against contractual caps and excluded items
"""
import sys
import json


def audit_cam_reconciliation(cam_data_json: str):
    import json
    data = json.loads(cam_data_json) if isinstance(cam_data_json, str) else cam_data_json
    claimed = data.get("claimed_cam_usd", 50000.0)
    cap = data.get("cap_usd", 60000.0)
    excluded = data.get("excluded_costs_usd", 0.0)
    net_allowed = claimed - excluded
    is_approved = net_allowed <= cap
    return {"net_allowed_usd": net_allowed, "status": "CAM_APPROVED" if is_approved else "CAM_EXCEEDED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "cam-reconciliation-auditor"}))
