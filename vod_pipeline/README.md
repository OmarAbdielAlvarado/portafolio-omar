# vod-pipeline — multi-platform VOD publishing (2026, personal project)
Automated pipeline that ran 3 adult-VOD platforms in production from one machine:
- Content pulled from a remote Windows server (SMB/rsync) to local storage.
- Per-platform publisher scripts: each site had its own size specs, SEO rules
  and API parameters (Flask/Selenium automation, Dockerized).
- Compliance layer: rewrites ES/EN metadata to enforce Visa & Mastercard
  prohibited-content policies before publishing (rules-as-data, in this folder).
- Operator workload reduced from hours/day (9-to-5 manual publishing) to minutes.

## Contents
- compliance_rewriter.py + banned_terms.json + app.py + Dockerfile
  -> card-network policy enforcement (Blueprint, Dockerized Flask).
