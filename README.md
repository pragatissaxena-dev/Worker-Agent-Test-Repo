# Worker-Agent-Test-Repo

# CI-Security-Test-Repo

# Harness CI Security Test Repo

A tiny, intentionally insecure repository for testing a Harness CI pipeline and security scans.

## Intentionally planted issues
1. **Exposed dummy secret** — `config.py` contains a fake API key. It is not a real credential.
2. **Insecure dependency pin** — `requirements.txt` pins an old Flask version for dependency scanning.
3. **Insecure container configuration** — `Dockerfile` runs the application as root.

Use this repository only for scanner testing. Do not add real credentials. Run scans with the Worker Agent step skipped first, then check whether findings appear in the Harness Vulnerabilities tab.
