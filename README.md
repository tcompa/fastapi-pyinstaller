# fastapi-pyinstaller

Run
```bash
uv run pyinstaller --onefile ./start-fractal-server.py --noconfirm --clean
```
and then
```bash
$ ./dist/start-fractal-server 
running in a PyInstaller bundle
INFO:     Started server process [686715]
INFO:     Waiting for application startup.
2026-06-10 09:35:50,823 - lifespan.startup - INFO - START (fractal-server 2.23.2)
2026-06-10 09:35:50,824 - lifespan.startup - INFO - END
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
2026-06-10 09:35:54,832 - uvicorn.access - INFO - 127.0.0.1:38612 - "GET / HTTP/1.1" 404
2026-06-10 09:35:54,903 - uvicorn.access - INFO - 127.0.0.1:38618 - "GET /favicon.ico HTTP/1.1" 404
2026-06-10 09:35:58,981 - uvicorn.access - INFO - 127.0.0.1:38612 - "GET /docs/ HTTP/1.1" 307
2026-06-10 09:35:58,997 - uvicorn.access - INFO - 127.0.0.1:38612 - "GET /docs HTTP/1.1" 200
2026-06-10 09:35:59,942 - uvicorn.access - INFO - 127.0.0.1:38612 - "GET /openapi.json HTTP/1.1" 200
2026-06-10 09:36:29,760 - uvicorn.access - INFO - 127.0.0.1:57910 - "GET /api/alive/ HTTP/1.1" 200
[...]
```

