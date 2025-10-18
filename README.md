# HNG13 Stage 0 Backend — Profile API with Cat Facts

A FastAPI application that provides a `/me` profile endpoint integrated with the Cat Facts API. It’s async, validated with Pydantic models, and resilient with graceful fallbacks.

• Blog write-up: see `blog/blog.md` for a social-ready post with context, lessons, and media placeholders.
    • GitHub repo: [github.com/SamuelOshin/hng13-stage0-backend](https://github.com/SamuelOshin/hng13-stage0-backend)

## Project Structure

```
.
├── main.py                      # Application entry point
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
└── app/
    ├── __init__.py
    ├── config.py                # Configuration settings
    ├── api/
    │   ├── __init__.py
    │   └── routes/
    │       ├── __init__.py
    │       └── profile.py       # Profile endpoint
    ├── schemas/
    │   ├── __init__.py
    │   └── profile.py           # Pydantic models
    └── services/
        ├── __init__.py
        └── cat_facts.py         # Cat Facts API integration
```

## Setup Instructions

### 1. Create a virtual environment (optional)

```powershell
python -m venv venv
./venv/Scripts/Activate.ps1
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy `.env.example` to `.env` and update with your information:

```powershell
Copy-Item .env.example .env
```

Edit `.env`:
```
USER_EMAIL=your.email@example.com
USER_NAME=Your Full Name
USER_STACK=Python/FastAPI
```

### 4. Run the Application

```powershell
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### GET /me

Returns profile information with a random cat fact.

**Response:**
```json
{
  "status": "success",
  "user": {
    "email": "your.email@example.com",
    "name": "Your Full Name",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-18T14:30:45.123Z",
  "fact": "Cats sleep for around 13 to 16 hours a day."
}
```

## Features

- ✅ Clean project structure following FastAPI best practices
- ✅ Pydantic models for request/response validation
- ✅ Async HTTP client for external API calls
- ✅ Error handling with fallback mechanism
- ✅ Environment-based configuration
- ✅ CORS middleware support
- ✅ Automatic API documentation at `/docs`
- ✅ ISO 8601 timestamp format

## Testing

Visit the interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

Or use curl:
```powershell
curl http://localhost:8000/me
```

Run minimal tests (optional):
```powershell
pip install pytest
pytest -q
```

## Error Handling

If the Cat Facts API is unavailable, the endpoint returns a fallback message instead of failing, ensuring the endpoint remains functional.

## References

- GitHub: [github.com/SamuelOshin/hng13-stage0-backend](https://github.com/SamuelOshin/hng13-stage0-backend)

- Blog: `blog/blog.md`
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`