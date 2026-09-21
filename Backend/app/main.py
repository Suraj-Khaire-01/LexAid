from fastapi import FastAPI

app = FastAPI(
    title="LexAid API",
    description="AI-Powered Multilingual Legal Aid Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "LexAid Backend is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }