---
name: cold-start-strategy
description: >
  Provides cold start launch strategy for new social media accounts going
  from zero to organic growth. Use when planning a first-30-days content
  cadence, seeding audiences, defining engagement tactics, or setting
  growth measurement targets.
---

# Cold Start Strategy

## Core Workflow

1. Assess the current phase of the account launch (Foundation, Iteration, or Growth)
2. Apply the phase-specific playbook from `references/phase-playbooks.md`
3. Set metrics targets appropriate to the current phase
4. Integrate with the content production pipeline described below
5. Monitor risk signals and apply mitigations as needed

## Content Production Pipeline

Follow this sequence for each content cycle:

1. Detect a CHANGELOG update
2. Use `changelog-content` to extract the brief
3. Use `content-strategy` to adapt per platform
4. Adjust cadence and format for the current cold-start phase
5. Use `requirements-handoff` to send to platform-engineering
6. Platform-engineering generates video via Higgsfield and uploads
7. Use `ab-experiment-measurement` to track performance

## Risk Mitigation

Monitor and respond to these risks throughout the launch:

- **Shadow-ban detection**: Watch reach-to-follower ratio for sudden drops
- **Content fatigue**: Rotate content pillars weekly
- **Platform algorithm changes**: Diversify presence across all three platforms
- **Account security**: Enable 2FA on all accounts; use separate email per platform

## Phase Reference

Refer to `references/phase-playbooks.md` for detailed day-by-day plans, seeding tactics, engagement loops, and Day 30 metrics targets for each phase:

- Phase 1: Foundation (Days 1-7)
- Phase 2: Iteration (Days 8-14)
- Phase 3: Growth (Days 15-30)
