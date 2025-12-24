# Angular Dependency AI Agent

AI-powered tool to analyze `package.json` and recommend safe minor upgrades
for Angular projects.

## Features

- Reads dependencies
- Fetches latest npm versions
- Angular-aware rules
- OpenAI-powered recommendations

## Run

```bash
npm install (in angular project)
cp .env.example .env (if required)
python -m pip install -r requirements.txt
python src/main.py /full/path/to/angular-project
```
## ✨ Key Features

- Parses Angular package.json
- Supports scoped npm packages (@angular/*, private scopes)
- Fetches latest versions from npm registry
- AI-powered upgrade risk classification:
- SAFE
- REVIEW
- UNSAFE
- Uses Azure OpenAI (Chat Completions) via secure gateway
- Environment-variable–based configuration (no secrets in code)
- Enterprise-safe error handling

## angular_dependency_ai_agent_python/
<img width="448" height="373" alt="Screenshot 2025-12-24 at 1 05 15 PM" src="https://github.com/user-attachments/assets/fc0791df-c25f-4302-afa7-0ed65d986257" />

## Configurations

- OPENAI_API_VERSION=2024-02-15-preview
- AZURE_OPENAI_ENDPOINT=https://<your-domain>/api/azureai
- AZURE_OPENAI_API_KEY=<your-secure-key>

## Dependencies

- python3 -m venv venv
- source venv/bin/activate
- python -m pip install -r requirements.txt
