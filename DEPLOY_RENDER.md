# Deploy on Render

This repo includes a [Render Blueprint](https://render.com/docs/infrastructure-as-code) file: `render.yaml`.

## What gets deployed

1. **ai-demand-inventory-api** — Python web service: FastAPI + `uvicorn`, SQLite seeded from `data/sales.csv` during build (`init_db.py`).
2. **ai-demand-inventory-ui** — Static site: Vite production build from `frontend/`.

## Steps

1. Push the repository to GitHub (or GitLab/Bitbucket supported by Render).
2. In [Render Dashboard](https://dashboard.render.com) → **New** → **Blueprint**.
3. Connect the repo and confirm `render.yaml` is detected; apply the blueprint.
4. Wait for the **API** service to go live; open its URL and check `/docs` or `/`.
5. Open the **static site** service → **Environment** → add:
   - `VITE_API_URL` = your API origin, e.g. `https://ai-demand-inventory-api.onrender.com` (no trailing slash).
6. **Manual Deploy** → **Clear build cache & deploy** on the static site so the build picks up `VITE_API_URL`.

`render.yaml` already configures an SPA **rewrite** (`/*` → `/index.html`) so React Router paths like `/dashboard` work.

## Large model files

`models/demand_model_advanced.pkl` is large. If Git rejects the push (>100 MB), use [Git LFS](https://git-lfs.com/) for that file or host the artifact in object storage and download it in `buildCommand` (advanced).

## Local parity

- Backend: `uvicorn main:app --host 0.0.0.0 --port 8000`
- Frontend: `cd frontend && npm run dev` (uses `http://localhost:8000` when `VITE_API_URL` is unset)
