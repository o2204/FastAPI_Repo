from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routes.questions import router as api_router

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(api_router, prefix="/api", tags=["Questions"])
