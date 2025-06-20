from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.palindrome import router as palindrome_router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "API running"}

app.include_router(palindrome_router, prefix="/api")
