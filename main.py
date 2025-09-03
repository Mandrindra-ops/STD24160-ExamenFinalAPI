from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.get("/health")
async def health():
    return {"texte": "ok"}

@app.post("/phone")
async def create_phone(id: str, brand: str, model: str, characteristics={
    "ram_memory": int,
    "rom_memory": int,
}):
    return {"id": id,
             "brand": brand,
             "model": model,
             "characteristics": characteristics}