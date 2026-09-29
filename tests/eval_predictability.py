"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitLeaseAudit.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.cam_reconciliation_auditor import *
from tools.rent_escalation_calculator import *
from tools.square_footage_prorator import *

class TestGitLeaseAuditPredictability(unittest.TestCase):
    def test_cam_reconciliation_auditor(self):
        res = audit_cam_reconciliation('{"claimed_cam_usd": 45000.0, "cap_usd": 50000.0, "excluded_costs_usd": 0.0}')
        self.assertEqual(res["status"], "CAM_APPROVED")

    def test_rent_escalation_calculator(self):
        res = calculate_rent_escalation('{"current_rent_usd": 120000.0, "escalation_pct": 3.0}')
        self.assertEqual(res["escalated_rent_usd"], 123600.0)
        self.assertEqual(res["status"], "ESCALATION_VERIFIED")

    def test_square_footage_prorator(self):
        res = calculate_prorated_share('{"tenant_sqft": 10000.0, "building_gla_sqft": 100000.0}')
        self.assertEqual(res["proportionate_share_pct"], 10.0)
        self.assertEqual(res["status"], "PRORATION_ACCURATE")


if __name__ == "__main__":
    unittest.main()
