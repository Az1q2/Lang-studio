from fastapi import FastAPI

app = FastAPI(
    title="Lang_studio",
    description="Local platform for language learning via video, manga, and reading",
    version="0.1.0",
)

@app.get("/api/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}