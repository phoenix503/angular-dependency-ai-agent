import semver from 'semver';
import axios from 'axios';

export async function getPackageInfo(pkg: string) {
  const res = await axios.get(`https://registry.npmjs.org/${pkg}`);
  return res.data['dist-tags'];
}

export function isMinorUpgrade(current: string, latest: string) {
  return semver.minor(latest) > semver.minor(current);
}

export async function getLatestVersions(pkg: string) {
  const url = `https://registry.npmjs.org/${pkg}`;
  const res = await axios.get(url);
  return res.data['dist-tags'];
}