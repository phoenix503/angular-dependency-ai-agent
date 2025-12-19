function recommend(pkg: string, current: string, latest: string) {
  if (current === latest) {
    return 'No update needed';
  }
  return `Upgrade recommended: ${current} → ${latest}`;
}