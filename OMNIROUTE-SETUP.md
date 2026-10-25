# OmniRoute setup guide (local machine)

OmniRoute is a local gateway that exposes one OpenAI-compatible endpoint
(`http://localhost:20128/v1`) and routes requests to the providers you connect.

## 1. Prerequisites

- Node.js **22.22.2+** (22.x LTS) or **24.0.0+**. Check with `node -v`.
  Older 22.x builds start but print a security warning and may break `better-sqlite3`.
- Or Docker, if you prefer containers (see "Docker alternative").

## 2. Install and start

```bash
npm install -g omniroute
omniroute --version
omniroute
```

On start it prints:

- Dashboard: http://localhost:20128
- API base: http://localhost:20128/v1

If SQLite errors appear, run `omniroute runtime repair` (or `npm rebuild better-sqlite3`).

## 3. Connect a provider

1. Open http://localhost:20128 and set a dashboard password if prompted.
2. Go to the **Providers** page and pick a provider.
   - API-key providers (OpenAI, Anthropic, OpenRouter, Groq, etc.): paste your key.
   - Account/OAuth providers: follow the browser login flow.
   - Free-tier providers: see `docs/getting-started/FREE-TIERS-GUIDE.md` in the repo
     (https://github.com/cheaper-inference/OmniRoute) before choosing one.
3. Use the connection test button to confirm it works.

Never commit provider keys. Keep them in the dashboard or in environment variables.

## 4. Get your OmniRoute key

Dashboard → **Endpoints** → copy your OmniRoute API key.

## 5. Test the endpoint

```bash
curl http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer YOUR_OMNIROUTE_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"auto","messages":[{"role":"user","content":"Hello!"}]}'
```

`auto` needs at least one eligible connected provider; otherwise the request fails.

## 6. Point your tools at it

For Cursor, Cline, Codex, or any OpenAI-compatible client:

- Base URL: `http://localhost:20128/v1`
- API key: your OmniRoute key
- Model: `auto`, or a specific model name from the dashboard

## 7. Keep it running

- Foreground: leave `omniroute` running in a terminal (Ctrl+C stops it).
- Background (macOS/Linux): `nohup omniroute > ~/omniroute.log 2>&1 &`
- Or use a process manager such as `pm2 start omniroute`.

## Docker alternative

```bash
git clone https://github.com/cheaper-inference/OmniRoute
cd OmniRoute
docker compose up -d
```

The repo also ships `docker-compose.prod.yml` and `docker-compose.selfhost.yml`.
Check the README's install section for the current image name and options.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Node version warning | Upgrade to Node 22.22.2+ or 24+ |
| SQLite / native module error | `omniroute runtime repair` |
| Port 20128 in use | Stop the other process or change the port per `docs/reference/ENVIRONMENT.md` |
| `auto` returns no route | Connect at least one provider and test it in the dashboard |
