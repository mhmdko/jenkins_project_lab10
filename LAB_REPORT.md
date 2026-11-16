# Lab 10 Jenkins CI/CD Report

**Student:** Mohammad Kourani  
**Work:** Individual  
**Repository:** https://github.com/mhmdko/jenkins_project_lab10

## Result

Jenkins job **Python-CI-CD**, build **#2**, completed with **SUCCESS** on 16 November 2026 at 13:20:37 Beirut time. The build checked out commit `232ca83d91394ebeeb2a7bd18003716ece0b170b` from GitHub. It ran on Windows with Jenkins 2.528.1, Java 21, and Python 3.14. The recorded duration was 90.0 seconds.

| Stage | Result | Output |
| --- | --- | --- |
| Checkout | Passed | GitHub main branch checked out |
| Setup | Passed | Virtual environment created; pinned dependencies installed |
| Lint | Passed | flake8 accepted app.py, tests, and deployment script |
| Test | Passed | 5 passed, 0 failed, 0 skipped; JUnit report published |
| Coverage | Passed | 100% statement and branch coverage; XML and HTML reports generated |
| Security Scan | Passed | Bandit reported 0 findings in app.py |
| Deploy | Passed | Numbered local release copied, executed, and verified |

## Changes to the original pipeline

The greeting and expected test output use my name. The project declares pytest, coverage, and Bandit alongside flake8 so all pipeline commands have their dependencies. Windows agents use batch commands with Windows paths; Unix agents use shell commands. Calling the virtual environment's Python directly avoids shell-specific activation problems.

The **Coverage** stage runs the tests under coverage.py and measures the command-line subprocess too. The build requires 100% application coverage. Reports include missing-line information, branch coverage, XML, and HTML.

The **Security Scan** stage checks app.py with Bandit and saves a JSON report. A finding returns a nonzero status and stops the pipeline before deployment. This is a static scan of the lab application, not a dependency vulnerability audit or a guarantee that all vulnerabilities are absent.

The **Deploy** stage replaces the handout's placeholder with a real local deployment, which is an allowed option in the lab. It copies app.py to `JENKINS_HOME/deployments/Python-CI-CD/build-2`, runs the copied file, verifies its output, and writes a manifest plus `current.json`. The deployment directory is outside the workspace, so cleanup preserves the release. No remote host was used.

JUnit results and build artifacts are published before Workspace Cleanup runs. A failed lint, test, coverage threshold, security scan, copy, or smoke test prevents a successful build.

## Deployment output

```text
Hello, World from Mohammad Kourani!
```

Application SHA-256: `ea6f6d0a6a3e08d2159dc9ceba2d8f71b7a443b3f374aead078e133a9883c7a8`.

## Recorded evidence

- [Jenkins console](evidence/jenkins-console.txt): actual output ending in `Finished: SUCCESS`.
- [Build metadata](evidence/jenkins-build.json): result, duration, build number, artifacts, and source revision.
- [Test summary](evidence/test-summary.json) and [JUnit XML](evidence/tests.xml): five successful tests.
- [Coverage XML](evidence/coverage.xml): full application statement and branch coverage.
- [Bandit report](evidence/bandit.json): no findings in the scanned application.
- [Deployment manifest](evidence/deployment.json): copied release, hash, and verified output.
- [Archived artifacts](evidence/jenkins-artifacts.zip): Jenkins's archive including the HTML coverage report.
- [Plugin versions](evidence/jenkins-plugins.json): active Git, Pipeline, SSH Agent, JUnit, and Workspace Cleanup plugins.

The local build URL is `http://127.0.0.1:8081/job/Python-CI-CD/2/`. It is accessible only on the computer running Jenkins; the checked-in evidence is available through GitHub for review. Documentation and evidence commits after the recorded build do not change the tested application or pipeline.
