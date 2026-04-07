from fastapi import FastAPI
from app.api import auth
from api import users

app = FastAPI(title="WealthWise Backend")

@app.get("/")
def root():
    return {"status": "Backend is running"}

app.include_router(auth.router)
app.include_router(users.router)
