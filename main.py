# ** Base Modules
from fastapi import FastAPI
from fastapi.testclient import TestClient
# ** App Modules
from app.db import Base, engine
from app.app_middleware import register_middleware
from app.app_controller import register_controller
from app.app_models import setup_models
from app.app_service import register_logger
from app.helper.scheduler import register_scheduler
# ** External Modules
from dotenv import load_dotenv


# Load Environment variables
load_dotenv()

# Register the Models
setup_models()

# Initialize the database
Base.metadata.create_all(bind=engine)

# Initialize the APP
app = FastAPI()

# Base Component Registers
register_middleware(app)
register_logger()
register_controller(app)
register_scheduler(app)

# Unittest Client
testClient = TestClient(app)
