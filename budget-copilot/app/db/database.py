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


def get_db():
    """Get a database session for use when requests are made.

    Yields a database session and ensures it is properly closed after use.
    Used with FastAPI dependency injection to provide database access.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Create all database tables based on defined models.
    
    This should be called once on application startup to ensure
    all required tables exist in the connected database.
    """
    Base.metadata.create_all(bind=engine)