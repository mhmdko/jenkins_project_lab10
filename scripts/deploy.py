"""Copy the application to a persistent local release and smoke-test it."""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path


def deploy(destination, build):
    source = Path(__file__).resolve().parents[1] / "app.py"
    release = destination.resolve() / f"build-{build}"
    release.mkdir(parents=True, exist_ok=True)
    target = release / "app.py"
    shutil.copy2(source, target)
    result = subprocess.run([sys.executable, str(target)], check=True,
                            capture_output=True, text=True)
    expected = "Hello, World from Mohammad Kourani!"
    if result.stdout.strip() != expected:
        raise RuntimeError("Deployment smoke test failed")
    manifest = {"build": build, "release": str(release),
                "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
                "output": result.stdout.strip(), "status": "deployed"}
    (release / "manifest.json").write_text(json.dumps(manifest, indent=2),
                                           encoding="utf-8")
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "current.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8")
    reports = source.parent / "reports"
    reports.mkdir(exist_ok=True)
    (reports / "deployment.json").write_text(json.dumps(manifest, indent=2),
                                             encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--build", type=int, default=0)
    args = parser.parse_args()
    deploy(args.destination, args.build)
