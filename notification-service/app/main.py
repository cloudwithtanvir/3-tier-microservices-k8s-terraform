# notification-service/main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to your frontend URL
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

