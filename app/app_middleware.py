# ** Base Modules
import time
from fastapi import Request


def register_middleware(app):
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start_time = time.perf_counter()
        response = await call_next(request)
        process_time = time.perf_counter() - start_time + 3
        response.headers["X-Process-Time2"] = str(process_time)
        return response
