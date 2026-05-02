from fastapi import FastAPI
from safety_service.api.router_health import router as health_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Safety Service",
        description="A service to ensure the safety of operations.",
        version="0.1.0",
    )
    app.include_router(health_router)
    return app

app = create_app()
