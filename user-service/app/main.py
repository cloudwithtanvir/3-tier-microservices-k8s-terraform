from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to your frontend URL
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