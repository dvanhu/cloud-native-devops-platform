from fastapi import FastAPI

app = FastAPI(
    title="Cloud Native DevOps Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Cloud Native DevOps Platform Backend Running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
