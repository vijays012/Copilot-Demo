# Responsible AI Guidelines

This checklist provides practical, minimal rules for responsibly using AI-generated code and outputs in this repository.

## Checklist

- Reviewing and validating AI-generated code
  - [ ] Run existing unit tests and add tests for any new behavior introduced by AI-generated code.
  - [ ] Run static analysis and linters (e.g., flake8, mypy) where applicable.
  - [ ] Manually read and understand the AI-suggested changes before merging: check for logic errors, edge cases, and security issues.
  - [ ] Require at least one human reviewer to approve AI-contributed code. Treat AI output as a draft, not authoritative.

- Handling sensitive data securely
  - [ ] Never include secrets, credentials, or personal data in prompts to external AI services.
  - [ ] Use synthetic or anonymized data for reproduction and tests when possible.
  - [ ] Store AI-generated artifacts that contain potentially sensitive information in protected locations; apply encryption and access controls as required by project policy.
  - [ ] Log and audit data exposures related to AI usage; enforce retention and deletion policies.

- Acknowledging AI contributions ethically
  - [ ] Document AI assistance in commit messages or pull request descriptions (e.g., "Generated with [model/service] for initial draft").
  - [ ] Do not claim authorship for text or code that was substantially produced by an AI model; be transparent about the role of AI.
  - [ ] Verify licensing and usage terms of the AI model/service and ensure compliance with third-party license obligations.

## Quick actions (when using AI assistance)

1. Before sending any code or data to an AI service, strip or redact secrets and personal identifiers.
2. After receiving AI output, run tests and linters immediately and perform a focused manual review for correctness and safety.
3. Record a short note in the PR describing what the AI was asked to do and what parts of the output were accepted, modified, or rejected.

## Acceptance criteria

- AI-generated changes are accepted only after tests pass and a human reviewer signs off.
- No sensitive data is exposed to external services during development or review.
- AI assistance is documented in version control and compliant with the model/service license.

## References

- Follow this project's general contribution and security policies for additional guidance.
