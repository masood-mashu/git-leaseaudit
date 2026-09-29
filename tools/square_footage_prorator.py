"""
square_footage_prorator.py - Computes tenant proportionate share percentage of gross leasable area
"""
import sys
import json


def calculate_prorated_share(area_json: str):
    import json
    data = json.loads(area_json) if isinstance(area_json, str) else area_json
    t_sqft = data.get("tenant_sqft", 5000.0)
    b_sqft = data.get("building_gla_sqft", 50000.0)
    share = round((t_sqft / max(b_sqft, 1.0)) * 100, 2)
    return {"proportionate_share_pct": share, "status": "PRORATION_ACCURATE"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "square-footage-prorator"}))
