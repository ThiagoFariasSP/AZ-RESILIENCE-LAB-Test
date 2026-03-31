# AZ-RESILIENCE-LAB-Test
Enterprise-grade Azure Disaster Recovery and Resilience lab focusing on multi-region design, RTO/RPO, failover automation, and Python-based operational scripting.

. Project Overview
AZ-RESILIENCE-LAB-Test is a hands-on, enterprise-focused lab designed to explore Disaster Recovery (DR) and Resilience engineering on Microsoft Azure.
The project simulates a critical production workload deployed in Azure and focuses on regional failure scenarios, service continuity, and operational automation. It combines architectural design with scripting and Infrastructure as Code to reflect how Disaster Recovery is implemented and operated in real-world enterprise environments.

2. Project Objectives
The main objectives of this project are:

Design a multi-region Azure architecture resilient to regional outages
Define and validate RTO (Recovery Time Objective) and RPO (Recovery Point Objective)
Implement Disaster Recovery strategies using native Azure services
Automate DR operations to reduce manual intervention during incidents
Simulate real failure scenarios and execute controlled DR drills
Demonstrate operational readiness through validation and monitoring


3. Enterprise Scenario
The lab represents an enterprise-critical application composed of:

A customer-facing web frontend
Backend APIs supporting business operations
A managed database service containing transactional data

The primary deployment runs in Brazil South, with a secondary recovery region in Brazil Southeast. The application must remain available during regional outages with minimal data loss and predictable recovery times.

4. In Scope
The following components and activities are included in the project scope:

Multi-region Azure architecture design
Azure Site Recovery (ASR) for workload replication
Azure Backup and data protection strategies
Traffic failover using Azure Front Door or Traffic Manager
RTO and RPO definition per workload component
Automated failover and failback processes
Disaster Recovery drills (planned and unplanned scenarios)
Automation using:

Python (Azure SDK)
Azure CLI
Infrastructure as Code (Bicep)




5. Out of Scope
The following items are intentionally excluded:

Application code development
End-user functional testing
Third-party DR tools
On-premises recovery scenarios
Cost optimization beyond DR-related design decisions


6. Assumptions and Constraints

The environment represents a production-like enterprise workload
Azure native services are preferred whenever possible
Security and identity are assumed to be pre-established
The project prioritizes resilience and recoverability over cost minimization
All automation is designed to be repeatable and auditable


7. Success Criteria
The project is considered successful when:

Regional failover can be executed within defined RTO targets
Data loss remains within defined RPO thresholds
Failover and failback processes are automated and repeatable
DR drills can be executed without manual infrastructure changes
Post-failover validation confirms application and data health
Architecture and automation reflect real enterprise DR practices
