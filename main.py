import uvicorn

from fastapi import FastAPI
from cache_fastapi.cacheMiddleware import CacheMiddleware
from cache_fastapi.Backends.memory_backend import MemoryBackend
from cache_fastapi.Backends.redis_backend import RedisBackend
from core.settings import settings
from api.v1.role import role_router
# from api.v1.auth import auth_router
# from api.v1.background import back_router


app = FastAPI(title="my_api")

# backend = MemoryBackend()
backend = RedisBackend()
cache_endpoints = ["/api"]

# app.add_middleware(
#     CacheMiddleware,
#     cached_endpoints=cache_endpoints,
#     backend=backend
#     )


app.include_router(role_router, prefix="/api/v1/roles")
# app.include_router(auth_router, prefix="/api/v1/authservice")
# app.include_router(back_router, prefix="/api/v1/back")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.app_port,
        reload=True
    )
    