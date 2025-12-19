function checkAngularRules(pkg: string, version: string, angularVersion: string): boolean {
  if (pkg.startsWith('@angular/') && !version.startsWith(angularVersion)) {
    return false;
  }
  return true;
}