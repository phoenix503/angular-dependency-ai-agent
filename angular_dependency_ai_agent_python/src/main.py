import os
from dotenv import load_dotenv
import sys
from pathlib import Path

from parser.package_parser import read_package_json
from version.npm_registry import get_latest_versions
from ai.openai_gateway import ai_recommend
from output.reporter import print_report

load_dotenv()

def run():
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <path-to-angular-project>")
        sys.exit(1)

    angular_project_path = Path(sys.argv[1])
    package_json_path = angular_project_path / "package.json"

    if not package_json_path.exists():
        print(f"Error: package.json not found at {package_json_path}")
        sys.exit(1)

    pkg_json = read_package_json(package_json_path)
    dependencies = pkg_json.get("dependencies", {})

    results = []

    for pkg, current in dependencies.items():
        versions = get_latest_versions(pkg)

        if not versions or "latest" not in versions:
            recommendation = "REVIEW: Unable to fetch version info"
            latest = "N/A"
        else:
            latest = versions["latest"]
            recommendation = ai_recommend(pkg, current, latest)

        latest = versions.get("latest")

        recommendation = ai_recommend(pkg, current, latest)

        results.append({
            "package": pkg,
            "current": current,
            "latest": latest,
            "recommendation": recommendation
        })

    print_report(results)

if __name__ == "__main__":
    run()
