from fastapi import FastAPI
from backend.app.config import settings
app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)

@app.get("/api/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}