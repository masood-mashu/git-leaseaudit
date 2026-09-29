# Explainability, Auditability & Decision Logic: GitLeaseAudit

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitLeaseAudit**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitLeaseAudit** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Executed**: Executed commercial real estate lease agreements and commencement exhibits.
- **Annual**: Annual landlord CAM operating expense statements and general ledger backups.
- **Bureau**: Bureau of Labor Statistics Consumer Price Index (CPI-U) historical series.
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **audit_cam_reconciliation**: Uses `cam-reconciliation-auditor` to calculate audits landlord operating expenses against contractual caps and excluded items.
   - **calculate_rent_escalation**: Uses `rent-escalation-calculator` to calculate calculates escalated annual base rent using contractual fixed percentage or cpi bump.
   - **calculate_prorated_share**: Uses `square-footage-prorator` to calculate computes tenant proportionate share percentage of gross leasable area.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When an annual CAM statement or lease amendment is audited, the agent executes cam_reconciliation_auditor, rent_escalation_calculator, and square_footage_prorator. If all expense categories are permitted and proration is exact, it issues APPROVED. If questionable administrative charges (> 10% fee) are present, it issues NEEDS_REVIEW. If unallowable capital renovations are billed directly to tenant, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) based on contractual mathematical accounting.
- **Assumes**: Assumes building square footage is measured under standard BOMA 2017 standards.
- **Does**: Does not render binding arbitration rulings in landlord-tenant judicial disputes.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
