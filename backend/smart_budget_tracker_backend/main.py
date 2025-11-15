from fastapi import FastAPI

app = FastAPI(title="Smart Budget Tracker Backend")

@app.get("/")
def read_root():
    return {"message": "Backend is alive 🚀"}
