# Lab 10 — Jenkins CI/CD for Python

**Student:** Mohammad Kourani  
**Work:** Individual lab

This project automates a Python greeting application's checks and local deployment through Jenkins. The greeting is `Hello, World from Mohammad Kourani!`.

## Pipeline

`Checkout → Setup → Lint → Test → Coverage → Security Scan → Deploy`

- **Setup:** creates an isolated Python environment and installs the pinned tools.
- **Lint:** checks the application, tests, and deployment script with flake8.
- **Test:** runs five tests and publishes JUnit results.
- **Coverage:** measures the application and its command-line process, requires 100% coverage, and generates XML and HTML reports.
- **Security Scan:** runs Bandit on the application; findings fail the build.
- **Deploy:** copies the application into a numbered release under `JENKINS_HOME/deployments/Python-CI-CD`, executes the deployed copy, checks its output, and writes a SHA-256 manifest. Deployment runs only after all checks pass.

Reports are archived before workspace cleanup. Releases are stored outside the workspace and survive cleanup. No remote server or SSH credentials are needed for this lab's local deployment option.

## Jenkins setup

1. Install Jenkins with Java 21 and make Python 3.10 or newer and Git available to the Jenkins process.
2. Unlock Jenkins and create an administrator account.
3. Install **Git**, **Pipeline**, **SSH Agent**, **JUnit**, and **Workspace Cleanup**. SSH Agent is installed for the lab prerequisite; local deployment does not use it.
4. Create a Pipeline job named **Python-CI-CD**.
5. Choose **Pipeline script from SCM**, select **Git**, and use `https://github.com/mhmdko/jenkins_project_lab10.git`.
6. Set the branch to `*/main` and Script Path to `Jenkinsfile_Mohammad_Kourani`.
7. Save and select **Build Now**. Review the stage results, test report, and archived artifacts.

The pipeline supports Windows and Unix agents and calls the environment's Python directly, so shell activation is unnecessary.

## Run locally

```text
python -m venv .venv
```

On Windows use `.venv\Scripts\python.exe`; on Unix use `.venv/bin/python` for `PYTHON` below:

```text
PYTHON -m pip install -r requirements.txt
PYTHON -m flake8 app.py tests scripts
PYTHON -m pytest -v
PYTHON -m coverage erase
PYTHON -m coverage run -m pytest -v
PYTHON -m coverage combine
PYTHON -m coverage report --fail-under=100
PYTHON -m coverage xml
PYTHON -m coverage html
PYTHON -m bandit -r app.py
PYTHON scripts/deploy.py --destination ../lab10-deployment --build 1
```

Create `reports` before generating reports locally. See [LAB_REPORT.md](LAB_REPORT.md) and [evidence](evidence/) for the recorded Jenkins execution.

## Files

| File | Purpose |
| --- | --- |
| `app.py` | Personalized greeting and command-line entry point |
| `tests/test_app.py` | Unit and command-line tests |
| `Jenkinsfile_Mohammad_Kourani` | Complete graded pipeline |
| `requirements.txt` | Pinned lint, test, coverage, and security tools |
| `.coveragerc` | Application coverage including subprocess execution |
| `scripts/deploy.py` | Local release deployment and smoke test |
| `jenkins/job-config.xml` | Reusable SCM job configuration |

## References

- [Jenkins WAR installation](https://www.jenkins.io/doc/book/installing/war-file/)
- [Using a Jenkinsfile](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/)
- [Recording tests and artifacts](https://www.jenkins.io/doc/pipeline/tour/tests-and-artifacts/)

Repository access is shared with NourSN2004, HusseinMoukalled, and RanimTahmoush for review.
