"""A database model representing expenses of 
the Smart Budget & Expense Tracker application."""


from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base

# A class to model budgets in the database, inheriting from SQLAlchemy's Base
class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    budget_id = Column(Integer, ForeignKey("budgets.id"), nullable=True)
    title = Column(String(150), nullable=False)
    category = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    spent_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="expenses")
    budget = relationship("Budget", back_populates="expenses")