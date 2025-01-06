# ** App Modules
from app.controller.base import router as base_router


def register_controller(app):
    app.include_router(base_router)
