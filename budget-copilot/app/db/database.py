"""Database config file for Budget Copilot application"""

# Import necessary tools to set up the databases
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Read database URL from .env file by loading .env value
load_dotenv()

# Define the database URL, defaulting to a local SQLite database if not set in .env
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./budget_copilot.db")

# Create the SQLAlchemy engine using the database URL
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} #Only needed for SQLite
)

# Create a configured "Session" class
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create a base class for our models to inherit from
Base = declarative_base()