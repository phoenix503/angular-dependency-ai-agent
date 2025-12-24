def is_angular_package(pkg_name: str) -> bool:
    return pkg_name.startswith("@angular/")

def is_minor_upgrade_safe(current: str, target: str) -> bool:
    return current.split(".")[0] == target.split(".")[0]
