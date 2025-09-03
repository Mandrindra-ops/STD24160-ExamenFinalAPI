from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.get("/health")
async def health():
    return {"texte": "ok"}

@app.post("/phones")
async def create_phone(id: str, brand: str, model: str, characteristics={
    "ram_memory": int,
    "rom_memory": int,
}):
    return {"id": id,
             "brand": brand,
             "model": model,
             "characteristics": characteristics}

@app.get("/phones")
async def get_phones():
    return {"liste_phones": [create_phone]}


@app.get("/phones/{id}")
async def get_phone(id: str):
    phone = next((phone for phone in get_phones()["liste_phones"] if phone["id"] == id), None)
    if phone:
        return {"phone": phone}
    return {"error": "Phone not found"}, 404

@app.put("PUT /phones/{id}/characteristics")
async def update_characteristics(id: str, characteristics={
    "ram_memory": int,
    "rom_memory": int,
}):
    phone = next((phone for phone in get_phones()["liste_phones"] if phone["id"] == id), None)
    if phone:
        phone["characteristics"] = characteristics
        return {"phone": phone}
    return {"error": "Phone not found"}, 404

    
