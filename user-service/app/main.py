import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Fetch the allowed origins from an environment variable, with a default fallback
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Use the environment variable here
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def read_root():
    return {"message": "User Service is up and running!"}

@app.get("/api/health")
def health_check():
    return JSONResponse(content={"status": "User Service is running!"}, status_code=200)