# AZ-RESILIENCE-LAB-Test
Enterprise-grade Azure Disaster Recovery and Resilience lab focusing on multi-region design, RTO/RPO, failover automation, and Python-based operational scripting.

# AZ-RESILIENCE-LAB-Test

Enterprise-grade Azure Disaster Recovery and Resilience lab focusing on multi-region design, RTO/RPO, failover automation, and Python-based operational scripting.

---

## Part 1 – Project Overview

AZ-RESILIENCE-LAB-Test is a hands-on, enterprise-focused lab designed to explore Disaster Recovery (DR) and Resilience engineering on Microsoft Azure.

The project simulates a critical production workload deployed in Azure and focuses on regional failure scenarios, service continuity, and operational automation using Python, Azure CLI, and Infrastructure as Code.

---

## Part 2 – Architecture & Disaster Recovery Strategy

### Regions
- Primary Region: Brazil South  
- Secondary Region: Brazil Southeast  

### Workload Tiering

**Tier 1 – Business Critical**
- Backend APIs  
- Azure SQL Database  
- Identity dependencies  

**Tier 2 – Important**
- Web Frontend  
- Supporting services  

---

## Part 3 – RTO and RPO Definition

### RTO Targets by Component

| Component               | Tier   | RTO Target |
|------------------------|--------|------------|
| Backend APIs            | Tier 1 | ≤ 10 min   |
| Azure SQL Database      | Tier 1 | ≤ 15 min   |
| Identity Dependencies   | Tier 1 | ≤ 5 min    |
| Web Frontend            | Tier 2 | ≤ 20 min   |
| Supporting Services     | Tier 2 | ≤ 30 min   |

### RPO Targets by Data Component

| Data Component            | Protection Method                     | RPO Target |
|--------------------------|----------------------------------------|------------|
| Azure SQL Database       | Geo-Replication                        | ≤ 5 min    |
| VM Disks                 | Azure Site Recovery                    | ≤ 15 min   |
| Storage Accounts         | GRS / Backup                           | ≤ 15 min   |
| Configuration / Metadata | Infrastructure as Code (Bicep)         | 0          |

---

## Part 4 – Automation Strategy

Automation is a core principle of this project.

### Tooling
- Python (Azure SDK)
- Azure CLI
- Bicep (Infrastructure as Code)

### Automation Goals
- Automated failover and failback
- DR drills using real workflows
- RTO/RPO measurement
- Post-failover validation
- Evidence generation

---

## Part 5 – Disaster Recovery Scenarios

### Scenario 1 – Full Regional Outage
- Trigger ASR failover
- Execute database geo-failover
- Redirect traffic
- Validate services
- Capture RTO/RPO

### Scenario 2 – Partial Compute Failure
- Recover affected services
- No global traffic failover

### Scenario 3 – Data Corruption
- Point-in-time restore
- Data validation

### Scenario 4 – Planned DR Drill
- Same automation as real incidents
- Metrics collected

### Scenario 5 – Failback
- Controlled return to primary region
- Post-failback validation

---

## Next Phase

The next phase focuses on **real Python implementation**, starting with:
- Authentication
- Azure Site Recovery failover
- Timestamp capture
- Validation hooks





























