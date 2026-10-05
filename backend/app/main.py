from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CI/CD Demo API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Welcome to CI/CD Demo API"}


@app.get("/api/health")
def health():
    return {"status": "healthy"}


@app.get("/api/message")
def message():
    return {"message": "Hello from FastAPI Backend!"}
