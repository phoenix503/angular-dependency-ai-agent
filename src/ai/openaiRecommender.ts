import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

export async function aiRecommend(
  pkg: string,
  current: string,
  latest: string
): Promise<string> {

  if (current === latest) {
    return 'No upgrade required';
  }

  const prompt = `
Package: ${pkg}
Current version: ${current}
Target version: ${latest}

Is upgrading safe within the same minor version? 
Respond with SAFE, REVIEW, or UNSAFE and a short reason.
`;

  const response = await client.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [{ role: 'user', content: prompt }]
  });

  return response.choices[0]?.message.content ?? 'No response';
}
