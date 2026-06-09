import uvicorn

if __name__ == "__main__":
    uvicorn.run("fastapi_bin.main:app", host="localhost", port=8000)
