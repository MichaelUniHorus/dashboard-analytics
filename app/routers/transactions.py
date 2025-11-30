"""
Transaction API endpoints.
"""
from datetime import datetime
from typing import Optional, List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.transaction_service import TransactionService

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.get("/metrics")
def get_transaction_metrics(
    start_date: Optional[datetime] = Query(None, description="Start date filter"),
    end_date: Optional[datetime] = Query(None, description="End date filter"),
    category: Optional[str] = Query(None, description="Category filter"),
    status: Optional[str] = Query(None, description="Status filter"),
    db: Session = Depends(get_db)
):
    """Get key metrics for transactions."""
    service = TransactionService(db)
    return service.get_key_metrics(
        start_date=start_date,
        end_date=end_date,
        category=category,
        status=status
    )


@router.get("/time-series")
def get_transaction_time_series(
    start_date: Optional[datetime] = Query(None, description="Start date filter"),
    end_date: Optional[datetime] = Query(None, description="End date filter"),
    category: Optional[str] = Query(None, description="Category filter"),
    status: Optional[str] = Query(None, description="Status filter"),
    group_by: str = Query("day", description="Group by period: day or month"),
    db: Session = Depends(get_db)
):
    """Get time series data for charts."""
    service = TransactionService(db)
    return service.get_time_series_data(
        start_date=start_date,
        end_date=end_date,
        category=category,
        status=status,
        group_by=group_by
    )


@router.get("/category-breakdown")
def get_transaction_category_breakdown(
    start_date: Optional[datetime] = Query(None, description="Start date filter"),
    end_date: Optional[datetime] = Query(None, description="End date filter"),
    status: Optional[str] = Query(None, description="Status filter"),
    db: Session = Depends(get_db)
):
    """Get breakdown by category."""
    service = TransactionService(db)
    return service.get_category_breakdown(
        start_date=start_date,
        end_date=end_date,
        status=status
    )


@router.get("/list")
def get_transaction_list(
    start_date: Optional[datetime] = Query(None, description="Start date filter"),
    end_date: Optional[datetime] = Query(None, description="End date filter"),
    category: Optional[str] = Query(None, description="Category filter"),
    status: Optional[str] = Query(None, description="Status filter"),
    limit: int = Query(100, description="Maximum number of records"),
    db: Session = Depends(get_db)
):
    """Get filtered list of transactions."""
    service = TransactionService(db)
    transactions = service.get_filtered_transactions(
        start_date=start_date,
        end_date=end_date,
        category=category,
        status=status,
        limit=limit
    )
    
    return [
        {
            'id': t.id,
            'date': t.date.isoformat(),
            'category': t.category,
            'amount': t.amount,
            'status': t.status,
            'description': t.description,
            'customer_id': t.customer_id
        }
        for t in transactions
    ]


@router.get("/filters")
def get_transaction_filters(db: Session = Depends(get_db)):
    """Get available filter options."""
    service = TransactionService(db)
    return {
        'categories': service.get_available_categories(),
        'statuses': service.get_available_statuses()
    }
