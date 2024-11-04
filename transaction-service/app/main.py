import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routes import router  # Ensure you have your router set up in routes.py
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

# Include your router for other API routes
app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Transaction Service is up and running!"}

@app.get("/api/health")  # Corrected the route method to use @app.get
def health_check():
    return JSONResponse(content={"status": "Transaction Service is running!"}, status_code=200)
