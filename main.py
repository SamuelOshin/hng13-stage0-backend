from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import profile

app = FastAPI(
    title="Profile API",
    description="API endpoint with cat facts integration",
    version="1.0.0"
)

# CORS middleware (optional but good practice)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(profile.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Profile API. Visit /me for profile info."}

@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    from app.config import settings

    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=False,
        log_level="info",
        access_log=True
    )
