# ** Base Modules
import importlib


def setup_models():
    # Model Registery for app models to record it.
    importlib.import_module("app.models.user")
