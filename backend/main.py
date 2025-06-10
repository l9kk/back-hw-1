from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.endpoints import tasks, auth

app = FastAPI()

# Database tables are now managed by Alembic migrations
# Run: docker-compose exec web alembic upgrade head

app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")

app.include_router(tasks.router, prefix="/api")
app.include_router(auth.router, prefix="/api")


@app.get("/hello")
async def read_root():
    return {"message": "Hello, World from Backend!"}


@app.get("/status")
async def get_status():
    return {"status": "ok"}
