# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitLeaseAudit** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitLeaseAudit Automation Engine`
* **Responsibilities**:
  * Extracts lease financial covenants, reconciles landlord CAM statements, and calculates escalations.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitLeaseAudit Verification & Policy Enforcer`
* **Responsibilities**:
  * Verifies that capital replacements (roof, HVAC modernization) are amortized rather than expensed.
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `Director of Commercial Real Estate / Asset Manager (Reserved for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
