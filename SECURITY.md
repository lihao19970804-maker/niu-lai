# Security policy

## Supported versions

VigilMesh is an early-stage prototype. Only the latest tagged release receives
security fixes; no version is currently claimed to be production-ready.

## Reporting a vulnerability

Please use GitHub's **Report a vulnerability** / private security advisory flow
for this repository. Do not include exploit details, credentials, personal
data, or sensitive logs in a public issue. If private reporting is temporarily
unavailable, contact the primary maintainer through their GitHub profile and
share only enough information to establish a private channel.

A useful report includes the affected version, impact, reproduction steps with
sanitized data, and a suggested mitigation when known. The maintainer will aim
to acknowledge reports within seven days; this is a best-effort target, not a
service-level agreement.

## Current prototype boundaries

- The scheduler is in-memory and does not provide durable or exactly-once
  execution.
- The reference provider consumes local deterministic input only.
- The console alerter is not an authenticated delivery channel.
- Configurations are trusted local input in v0.1.0.
- No automated remediation, shell execution, or credential store is included.

