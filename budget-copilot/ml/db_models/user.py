"""User model for the database of the Budget Copilot application"""

# Import necessary SQLAlchemy tools and base class
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

# Define the User model with appropriate attributes and relationships
class User(Base):
    """A class to model users of the Budget Copilot application"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    budgets = relationship("Budget", back_populates="user")