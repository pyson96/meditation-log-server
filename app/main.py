from fastapi import FastAPI
from app.routers import auth_routes
from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
import os

FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN")
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_ORIGIN],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # allow POST, OPTIONS, etc.
    allow_headers=["*"],  # allow Authorization, Content-Type, etc.
)