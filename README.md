# AZ-RESILIENCE-LAB-Test

## 1. Project Overview

AZ-RESILIENCE-LAB-Test is a portfolio-focused project designed to demonstrate the design and implementation of a complete **Disaster Recovery (DR) solution on Microsoft Azure**, combining architectural decisions with **automation using Python**.

The project simulates a **critical enterprise environment** that requires high availability, predictable recovery times, and reduced manual intervention during incidents. It focuses on protecting a multi-tier application composed of a web frontend, backend APIs, and a managed database, deployed across two Azure regions.

In addition to core Disaster Recovery concepts, this project emphasizes **operational readiness and automation**, leveraging Python, Azure CLI, and Infrastructure as Code to support failover, failback, DR drills, and recovery validation. The goal is to reflect how Disaster Recovery is planned, executed, tested, and documented in real-world Azure enterprise environments.

## 2. Business and Technical Scenario

This project is based on a **critical enterprise web application** used by end customers. The solution represents a common real-world scenario where service availability and data integrity are essential for business continuity.

The application is composed of three main layers:
- A **web frontend** that serves customer requests
- A set of **backend APIs** responsible for business logic
- A **managed database** that stores transactional and operational data

The primary environment is deployed in the **Azure Brazil South** region. To address regional outage risks, a **secondary recovery environment** is defined in the **Azure Brazil Southeast** region, which will be used for Disaster Recovery purposes.

This scenario assumes that a **regional failure** can occur and that recovery must be executed in a controlled and predictable way, respecting defined RTO and RPO targets while minimizing manual intervention. The environment is designed to support both **planned Disaster Recovery drills** and **unplanned outage scenarios**.


## 3. Disaster Recovery Objectives

## 4. RTO and RPO Requirements

## 5. Azure Architecture Overview

## 6. Disaster Recovery Strategy

## 7. Automation Strategy

## 8. Planned Scripts and Automation Phases

## 9. Validation, Testing, and DR Drills

## 10. Next Steps and Project Evolution
