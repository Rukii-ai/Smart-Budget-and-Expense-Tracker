"""A database model representing a user of 
the Smart Budget & Expense Tracker application."""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base


# A class to model Users in the database, inheriting from SQLAlchemy's Base
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    budgets = relationship(
        "Budget", back_populates="user", cascade="all, delete-orphan"
        )
    
    expenses = relationship(
        "Expense", back_populates="user", cascade="all, delete-orphan"
        )