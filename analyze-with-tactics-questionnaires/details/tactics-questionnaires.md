# Tactics-Based Questionnaires (Examples)

Use these questionnaires to evaluate an architecture against specific Quality Attributes. 

## Availability Questionnaire
*Focus: Fault detection, recovery, and prevention.*

1. **Detect Faults:** How does the system detect failures (e.g., ping/echo, heartbeat, exceptions)?
2. **Recover - Preparation & Repair:** How does the system recover from failure (e.g., active/passive redundancy, spare nodes, rollback)?
3. **Recover - Reintroduction:** How does a failed component safely rejoin the cluster (e.g., state synchronization, shadowing)?
4. **Prevent Faults:** How does the system prevent failures from escalating (e.g., removal from service, transactions, predictive monitors)?

## Modifiability Questionnaire
*Focus: Cost and risk of making changes.*

1. **Reduce Module Size:** Are modules kept small and focused (high cohesion)?
2. **Increase Cohesion:** Do components only do one thing?
3. **Reduce Coupling:** How is coupling minimized (e.g., encapsulate, use intermediaries/interfaces, restrict dependencies)?
4. **Defer Binding:** When are decisions bound (e.g., compile-time, load-time, runtime configuration)?

## Security Questionnaire
*Focus: Protecting against unauthorized access and maintaining data integrity.*

1. **Detect Attacks:** How are attacks identified (e.g., intrusion detection, logging)?
2. **Resist Attacks:** How does the system defend itself (e.g., authenticate users, authorize access, encrypt data, limit access)?
3. **React to Attacks:** What happens when an attack succeeds (e.g., lock accounts, revoke access, alert admins)?
4. **Recover from Attacks:** How does the system restore integrity (e.g., audit trails, restore from backup)?

## Performance Questionnaire
*Focus: Response time and throughput.*

1. **Control Resource Demand:** How does the system handle high load (e.g., sample rates, limit event response, manage sampling)?
2. **Manage Resources:** How are resources optimized (e.g., concurrency, multiple copies, increase available resources, scheduling)?
