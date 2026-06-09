from fastapi import FastAPI

app = FastAPI()


@app.get("/hello/")
async def read_root():
    return "ciao"


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

