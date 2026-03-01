from fastapi import FastAPI

app = FastAPI(title="Pyramide API")

@app.get("/")
def root():
    return {"service": "Pyramide", "status": "running"}

@app.get("/health")
def health():
    return {"ok": True}
