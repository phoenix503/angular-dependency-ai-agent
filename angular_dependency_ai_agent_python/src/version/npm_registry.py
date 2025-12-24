import requests
from urllib.parse import quote

def get_latest_versions(package_name: str):
    encoded_name = quote(package_name, safe="")
    url = f"https://registry.npmjs.org/{encoded_name}"

    response = requests.get(url, timeout=5)

    if response.status_code == 404:
        return {}

    response.raise_for_status()
    return response.json().get("dist-tags", {})
