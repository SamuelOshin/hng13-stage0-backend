Got it—here are ready-to-post versions for each platform with media prompts and captions to boost engagement.

## LinkedIn post (long-form + carousel-ready)

I built a tiny but resilient FastAPI service that returns my profile + a random Cat Fact from an external API—fast, typed, and fault-tolerant.

What it does:
- GET /me returns:
  - status, user { email, name, stack }
  - ISO 8601 UTC timestamp (Z)
  - a fun cat fact (with fallback if API is down)
- Async httpx with timeout
- Pydantic v2 models for schema + docs
- Clean structure: routes · schemas · services · config

Why it matters:
- Shows production-minded API patterns in a small project
- External failures don’t break the endpoint
- Ready-to-extend and easy to reason about

What I learned:
- Pydantic v2 + FastAPI keeps APIs crisp and explicit
- Timeouts + graceful fallbacks are non-negotiable
- ISO timestamps prevent parsing headaches downstream
- Small + well-structured > large + messy

Try it:
- Repo: https://github.com/SamuelOshin/hng13-stage0-backend
- Docs: http://localhost:8000/docs
- Endpoint: http://localhost:8000/me

Media (carousel/video ideas):
- Slide 1: Project overview + repo link
- Slide 2: Project structure
- Slide 3: /me endpoint JSON response
- Slide 4: Swagger UI screenshot
- Slide 5: Code snippet (cat fact service with timeout/fallback)
- Short 15–20s screen capture: run server → open /docs → call /me

If this is helpful, star the repo and drop feedback—always improving.

#HNGi13 #FastAPI #Python #Backend #APIs #Pydantic #DevCommunity

Suggested image captions/alt text:
- “Swagger UI showing GET /me” (alt: Swagger UI display of /me endpoint details)
- “Terminal running uvicorn” (alt: PowerShell showing uvicorn server startup)
- “JSON output from /me” (alt: Browser window with API response JSON)


## Dev.to / Hashnode / Medium article

Title: Building a tiny, resilient FastAPI service (Profile + Cat Facts)

TL;DR
I built a minimal FastAPI backend that exposes a single endpoint, /me, which returns my profile details, an ISO 8601 UTC timestamp, and a fun Cat Fact from an external API. It’s resilient (graceful fallbacks), typed (Pydantic v2), async (httpx), and documented (Swagger). This post covers the design, implementation, and lessons learned.

Repo: https://github.com/SamuelOshin/hng13-stage0-backend

What I built
- GET /me returns:
  - status: "success"
  - user: { email, name, stack }
  - timestamp: ISO 8601 UTC (Z)
  - fact: a random cat fact (with fallback)
- Pydantic v2 models for response schema + docs
- httpx.AsyncClient with timeout and error handling
- pydantic-settings for environment-driven config
- CORS enabled, OpenAPI at /docs

Architecture
- main.py (FastAPI app + routing + CORS)
- profile.py (GET /me)
- cat_facts.py (httpx client with timeout + fallback)
- profile.py (Pydantic models)
- config.py (settings with pydantic-settings)

Why these choices
- Clarity and separation of concerns
- Resilience to external API issues
- Strong typing for self-documenting APIs
- Easy local setup and extension

Run locally (Windows PowerShell)
- Create venv and install:
  - python -m venv venv
  - Activate.ps1
  - pip install -r requirements.txt
- Configure .env:
  - Copy-Item .env.example .env
  - Set USER_EMAIL, USER_NAME, USER_STACK
- Start:
  - uvicorn main:app --reload --port 8000
- Try:
  - curl http://localhost:8000/me
- Docs:
  - http://localhost:8000/docs

Sample response
{
  "status": "success",
  "user": { "email": "you@example.com", "name": "Your Name", "stack": "Python/FastAPI" },
  "timestamp": "2025-10-18T14:30:45.123Z",
  "fact": "Cats sleep for around 13 to 16 hours a day."
}

Testing
- Minimal pytest verifying /me shape and deterministic cat fact via mock
- Install + run:
  - pip install -r requirements-dev.txt
  - pytest -q

What this taught me
- Pydantic v2 + FastAPI is a great pairing for clear, validated APIs
- Timeouts and fallbacks keep endpoints reliable
- ISO timestamps avoid cross-timezone surprises
- A small project can showcase production thinking

What I’d add next
- CI with lint + tests
- Dockerfile and one-command run
- Health/metrics endpoints
- Tracing

Media (attach screenshots/videos)
- Swagger UI for /me
- Terminal with uvicorn running
- Browser showing /me response
- 15–20s screen recording: start → docs → call /me

If this resonates, star the repo and tell me what to improve next!
Tags: FastAPI, Python, Backend, APIs, Pydantic, httpx, Developer-Experience


## X (formerly Twitter) thread

1/ I built a tiny FastAPI backend that returns my profile + a random Cat Fact. Async httpx, Pydantic v2, timeouts, and graceful fallbacks. Docs + tests included. #HNGi13 #FastAPI #Python

2/ Endpoint: GET /me → status, user { email, name, stack }, ISO 8601 UTC timestamp, and a cat fact (fallback if API is down). Reliable by design.

3/ Stack: FastAPI, httpx.AsyncClient (5s timeout), Pydantic v2 models, pydantic-settings for env config, CORS, auto docs.

4/ Why: demonstrate production-minded patterns in a tiny repo: clear structure, typed contracts, resilience to external failures.

5/ Lessons: timeouts + fallbacks are essential; ISO timestamps reduce parsing pain; small + clean beats large + messy.

6/ Try it:
Repo: https://github.com/SamuelOshin/hng13-stage0-backend
Docs: http://localhost:8000/docs

7/ Media: Swagger UI, /me JSON response, and a short 15–20s screen recording (run → docs → call /me). Engagement > words.

8/ If useful, star the repo + share feedback. Always iterating. #Backend #APIs #DevCommunity


## quick media pack (attach with your posts)

Attach these (or similar) for better reach and clarity:
- Screenshot: Swagger UI showing GET /me (alt: Swagger UI for /me endpoint)
- Screenshot: Terminal with uvicorn running (alt: Terminal output of FastAPI server startup)
- Screenshot: JSON response from /me (alt: Browser window showing API response)
- Short 15–20s screen recording: starting server, opening docs, calling /me

If you want, I can also generate a trimmed “code snippet” image (dark theme) and a short voiceover script for a 20s clip.