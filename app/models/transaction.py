"""
Transaction model for financial data.
Example use case: revenue, payments, orders tracking.
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
import enum

from app.database import Base


class TransactionStatus(enum.Enum):
    """Transaction status enumeration."""
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class Transaction(Base):
    """
    Transaction model for financial operations.
    
    Attributes:
        id: Primary key
        date: Transaction date and time
        category: Transaction category (e.g., 'sales', 'refund', 'subscription')
        amount: Transaction amount
        status: Transaction status
        description: Optional description
        customer_id: Optional customer identifier
    """
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    category = Column(String(50), nullable=False, index=True)
    amount = Column(Float, nullable=False)
    status = Column(String(20), nullable=False, default="completed", index=True)
    description = Column(String(255), nullable=True)
    customer_id = Column(String(50), nullable=True, index=True)
    
    def __repr__(self):
        return f"<Transaction(id={self.id}, date={self.date}, category={self.category}, amount={self.amount})>"
