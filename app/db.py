# ** Base Modules
import os
# ** External Modules
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


# def register_database():
# Establish a connection to the database
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(
    os.getenv('DATABASE_USERNAME'),
    os.getenv('DATABASE_PASSWORD'),
    # Default Host
    os.getenv('DATABASE_HOST', 'localhost'),
    # Port name should same as Docker's exposed port
    os.getenv('DATABASE_PORT', 5433),
    os.getenv('DATABASE_NAME')
)

engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_timeout=60,
    pool_recycle=300,
    pool_pre_ping=True
)
global session
# Set the DB Session
session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

# Define the base model class
Base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
