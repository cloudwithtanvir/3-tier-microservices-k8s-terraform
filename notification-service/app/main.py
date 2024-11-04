# notification-service/main.py
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
@app.post("/send-notification")
async def send_notification(message: str):
    # Logic to send a notification (e.g., email, SMS)
    return {"message": "Notification sent", "content": message}

@app.get("/api/health")  # Changed to @app.get for the health check endpoint
async def health_check():
    return JSONResponse(content={"status": "Notification Service is running!"}, status_code=200)

