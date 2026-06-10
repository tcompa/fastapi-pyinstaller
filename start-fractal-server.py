import os
import sys

import uvicorn

if __name__ == "__main__":
    os.environ["POSTGRES_DB"] = "fake"
    os.environ["JWT_SECRET_KEY"] = "fake"
    import fractal_server.main  # noqa: F401

    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        print("running in a PyInstaller bundle")
    else:
        print("running in a normal Python process")

    uvicorn.run("fractal_server.main:app", host="localhost", port=8000)
