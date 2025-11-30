"""
Transaction data service.
Handles data aggregation, filtering, and analysis for financial transactions.
"""
from datetime import datetime
from typing import Optional, List, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import func, and_
import pandas as pd

from app.models.transaction import Transaction


class TransactionService:
    """Service for transaction data operations."""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_filtered_transactions(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        category: Optional[str] = None,
        status: Optional[str] = None,
        limit: int = 100
    ) -> List[Transaction]:
        """
        Get filtered transactions based on criteria.
        
        Args:
            start_date: Filter by start date
            end_date: Filter by end date
            category: Filter by category
            status: Filter by status
            limit: Maximum number of records to return
            
        Returns:
            List of Transaction objects
        """
        query = self.db.query(Transaction)
        
        filters = []
        if start_date:
            filters.append(Transaction.date >= start_date)
        if end_date:
            filters.append(Transaction.date <= end_date)
        if category:
            filters.append(Transaction.category == category)
        if status:
            filters.append(Transaction.status == status)
        
        if filters:
            query = query.filter(and_(*filters))
        
        return query.order_by(Transaction.date.desc()).limit(limit).all()
    
    def get_key_metrics(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        category: Optional[str] = None,
        status: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Calculate key metrics for transactions.
        
        Returns:
            Dictionary with metrics: total_amount, count, average, min, max
        """
        query = self.db.query(
            func.sum(Transaction.amount).label('total'),
            func.count(Transaction.id).label('count'),
            func.avg(Transaction.amount).label('average'),
            func.min(Transaction.amount).label('min'),
            func.max(Transaction.amount).label('max')
        )
        
        filters = []
        if start_date:
            filters.append(Transaction.date >= start_date)
        if end_date:
            filters.append(Transaction.date <= end_date)
        if category:
            filters.append(Transaction.category == category)
        if status:
            filters.append(Transaction.status == status)
        
        if filters:
            query = query.filter(and_(*filters))
        
        result = query.first()
        
        return {
            'total_amount': float(result.total) if result.total else 0.0,
            'count': result.count if result.count else 0,
            'average': float(result.average) if result.average else 0.0,
            'min': float(result.min) if result.min else 0.0,
            'max': float(result.max) if result.max else 0.0
        }
    
    def get_time_series_data(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        category: Optional[str] = None,
        status: Optional[str] = None,
        group_by: str = 'day'
    ) -> List[Dict[str, Any]]:
        """
        Get time series data for charts.
        
        Args:
            start_date: Filter by start date
            end_date: Filter by end date
            category: Filter by category
            status: Filter by status
            group_by: Grouping period ('day' or 'month')
            
        Returns:
            List of dictionaries with date and aggregated values
        """
        transactions = self.get_filtered_transactions(
            start_date=start_date,
            end_date=end_date,
            category=category,
            status=status,
            limit=10000
        )
        
        if not transactions:
            return []
        
        # Convert to pandas DataFrame for easier aggregation
        df = pd.DataFrame([
            {
                'date': t.date,
                'amount': t.amount,
                'category': t.category
            }
            for t in transactions
        ])
        
        # Group by period
        if group_by == 'month':
            df['period'] = pd.to_datetime(df['date']).dt.to_period('M')
        else:  # day
            df['period'] = pd.to_datetime(df['date']).dt.date
        
        # Aggregate
        grouped = df.groupby('period').agg({
            'amount': ['sum', 'count']
        }).reset_index()
        
        grouped.columns = ['period', 'total_amount', 'count']
        
        # Convert to list of dicts
        result = []
        for _, row in grouped.iterrows():
            result.append({
                'period': str(row['period']),
                'total_amount': float(row['total_amount']),
                'count': int(row['count'])
            })
        
        return result
    
    def get_category_breakdown(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        status: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get breakdown by category.
        
        Returns:
            List of dictionaries with category and aggregated values
        """
        query = self.db.query(
            Transaction.category,
            func.sum(Transaction.amount).label('total'),
            func.count(Transaction.id).label('count')
        )
        
        filters = []
        if start_date:
            filters.append(Transaction.date >= start_date)
        if end_date:
            filters.append(Transaction.date <= end_date)
        if status:
            filters.append(Transaction.status == status)
        
        if filters:
            query = query.filter(and_(*filters))
        
        query = query.group_by(Transaction.category)
        results = query.all()
        
        return [
            {
                'category': r.category,
                'total_amount': float(r.total),
                'count': r.count
            }
            for r in results
        ]
    
    def get_available_categories(self) -> List[str]:
        """Get list of all available categories."""
        results = self.db.query(Transaction.category).distinct().all()
        return [r.category for r in results]
    
    def get_available_statuses(self) -> List[str]:
        """Get list of all available statuses."""
        results = self.db.query(Transaction.status).distinct().all()
        return [r.status for r in results]
