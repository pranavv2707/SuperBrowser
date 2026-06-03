# Contributing to SuperBrowser

SuperBrowser is an AI-powered browser that aggregates search results, AI answers, and community discussions (StackOverflow, Reddit, HackerNews, Dev.to) into one interface. It's built with a FastAPI backend and a React + Electron frontend.

We're part of **GSSoC 2026** (15 May → 14 August 2026). Welcome.

---

## Read this before anything else

We don't assign issues on a first-come-first-served basis.

**The contributor with the strongest proposed approach gets assigned.**

To claim an issue:
1. Read the issue fully.
2. Write up your approach — which files you'd touch, your design decisions, edge cases you've considered, any tradeoffs.
3. Post it as a comment on the issue **or** email it to **jeetpandya2006@gmail.com**.
4. Wait for assignment. Don't start coding before you're assigned.

Don't comment "I'd like to work on this" without an approach. Those comments will be ignored.

---

## Local setup

### Prerequisites
- Python 3.10+
- Node.js 18+
- A [Groq API key](https://console.groq.com/keys) (free)
- A [SerpAPI key](https://serpapi.com/manage-api-key) (free tier available)

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Open .env and fill in GROQ_API_KEY and SERPAPI_API_KEY
uvicorn main:app --reload
```

Backend runs at `http://localhost:8000`. API docs at `http://localhost:8000/docs`.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`.

### Verify it works

Open the frontend, type any search query in SuperSEO mode, and confirm results appear. If you see a raw error string like `"Groq API key not configured"`, your `.env` is missing a key.

---

## How to contribute

### 1. Find an issue

Browse [open issues](https://github.com/PandyaJeet/SuperBrowser/issues). Issues labelled `good first issue` are the best starting point if this is your first contribution.

### 2. Propose your approach

Comment on the issue or email **jeetpandya2006@gmail.com** with:
- Which files you'd modify or create
- Your design approach (key decisions, not just "I'll use React state")
- Edge cases you'd handle
- Any dependencies or blockers you spotted

The more specific your proposal, the better your chances.

### 3. Get assigned

Once your approach is approved, you'll be assigned the issue. Start coding only after assignment.

### 4. Branch naming

```
feat/issue-N-short-description
fix/issue-N-short-description
```

Examples:
```
feat/issue-12-dark-mode
fix/issue-3-friendly-error-states
```

### 5. Submit a PR

- Title format: `feat: short description (#N)` or `fix: short description (#N)`
- Link the issue in the PR body: `Closes #N`
- Describe what you changed and why
- Add screenshots for any UI changes
- Make sure the app runs without errors before submitting

---

## GSSoC points

Every merged and approved PR earns points based on its labels.

| Label | Points |
|---|---|
| `gssoc:approved` | +50 (base, every merged PR) |
| `level:beginner` | +20 |
| `level:intermediate` | +35 |
| `level:advanced` | +55 |
| `level:critical` | +80 |
| `quality:clean` | ×1.2 |
| `quality:exceptional` | ×1.5 |
| `type:bug` | +10 |
| `type:feature` | +10 |
| `type:docs` | +5 |
| `type:security` | +20 |
| `type:performance` | +15 |
| `type:accessibility` | +15 |
| `type:testing` | +10 |
| `type:refactor` | +10 |

Labels are set by maintainers after review, not by contributors.

PRs labelled `gssoc:invalid` or `gssoc:spam` earn zero points and may result in disqualification. Contribute genuinely.

---

## Code style

**Backend (Python)**
- Follow PEP 8
- Use `async def` for all endpoint and scraper functions (the project uses `httpx` + `asyncio` throughout — keep it consistent)
- Handle errors explicitly — don't add bare `except: pass` blocks (there are already too many)
- Add a docstring to any new function

**Frontend (React)**
- Functional components with hooks only
- Keep components small — `App.jsx` is already 916 lines and a problem; don't make it bigger. If your change touches `App.jsx`, try to extract related logic into a component or hook instead
- No inline styles — use the existing CSS classes or add to the relevant stylesheet

---

## What not to do

- Don't open a PR without being assigned first
- Don't modify unrelated files to pad your diff
- Don't submit AI-generated code without reviewing, testing, and understanding it — PRs that are clearly unreviewed AI output will be labelled `gssoc:spam`
- Don't DM the maintainer for status updates — comment on your issue instead

---

## Need help?

- Comment on the relevant issue
- Email **jeetpandya2006@gmail.com** for approach reviews or blockers

Thanks for contributing.
