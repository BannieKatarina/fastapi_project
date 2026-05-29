from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.api.base import router as base_router
from src.api.base import router_user


def create_app() -> FastAPI:
    app = FastAPI(root_path="/api/v1")
    app.add_middleware(
        CORSMiddleware,  # type: ignore
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(base_router)
    app.include_router(router_user)

    return app
