# fastapi-pyinstaller

```console
$ uv run pyinstaller -D ./src/fastapi_bin/__init__.py
[...]

$ ./dist/__init__/__init__ 
Traceback (most recent call last):
  File "__init__.py", line 4, in <module>
  File "uvicorn/main.py", line 617, in run
  File "uvicorn/server.py", line 75, in run
  File "asyncio/runners.py", line 195, in run
  File "asyncio/runners.py", line 118, in run
  File "asyncio/base_events.py", line 691, in run_until_complete
  File "uvicorn/server.py", line 79, in serve
  File "uvicorn/server.py", line 86, in _serve
  File "uvicorn/config.py", line 449, in load
  File "uvicorn/importer.py", line 22, in import_from_string
  File "uvicorn/importer.py", line 19, in import_from_string
  File "importlib/__init__.py", line 90, in import_module
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1310, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1324, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'fastapi_bin'
[PYI-616710:ERROR] Failed to execute script '__init__' due to unhandled exception!
```

