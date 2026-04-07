# Axiom Yield Backend — Flask API

SAP v3.0 server-side scoring engine for Axiom Yield Broker.

## Setup (local)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env       # then edit .env with your keys
python app.py
```

API runs at `http://localhost:5000`

## Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/api/health` | Confirm backend is live |
| POST | `/api/calculate` | Run SAP yield score, store result |
| GET | `/api/recent?limit=20` | Last N calculations |
| GET | `/api/stats` | Dashboard summary stats |

## Deploy to Render

1. Push this repo to GitHub
2. Sign up at [render.com](https://render.com)
3. New Web Service → connect repo → Render detects `render.yaml` automatically
4. Add `FLASK_SECRET_KEY` and any API keys in Render's environment settings
5. Your backend URL: `https://axiom-yield-backend.onrender.com`

Then update the `fetch()` URL in `index.html` to point to your Render URL.

## Security

- `.env` is gitignored — never commit it
- CORS is restricted to your GitHub Pages domain
- Scoring logic lives server-side only (`scoring.py`)

---

Copyright © 2026 Richard Leroy Stanfield Jr. — Meridian Axiom Alignment Technologies
