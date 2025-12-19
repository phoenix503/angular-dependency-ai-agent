import 'dotenv/config';
import { readPackageJson } from './parser/packageParser.js';
import { getLatestVersions } from './version/npmRegistry.js';
import { aiRecommend } from './ai/openaiRecommender.js';

async function run() {
  const pkgJson = readPackageJson('./package.json');
  const dependencies = pkgJson.dependencies as Record<string, string>;

  const results = [];

  for (const [pkg, current] of Object.entries(dependencies)) {
    const tags = await getLatestVersions(pkg);
    const latest = tags.latest;

    const recommendation = await aiRecommend(
      pkg,
      current,
      latest
    );

    results.push({
      package: pkg,
      current,
      latest,
      recommendation
    });
  }

  console.table(results);
  console.log('API key loaded:', !!process.env.OPENAI_API_KEY);
}


run();
