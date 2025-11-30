"""
Equipment metrics data service.
Handles data aggregation, filtering, and analysis for equipment monitoring.
"""
from datetime import datetime
from typing import Optional, List, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import func, and_
import pandas as pd

from app.models.equipment_metric import EquipmentMetric


class EquipmentService:
    """Service for equipment metrics data operations."""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_filtered_metrics(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        equipment_id: Optional[str] = None,
        metric_name: Optional[str] = None,
        status: Optional[str] = None,
        limit: int = 100
    ) -> List[EquipmentMetric]:
        """
        Get filtered equipment metrics based on criteria.
        
        Args:
            start_date: Filter by start date
            end_date: Filter by end date
            equipment_id: Filter by equipment ID
            metric_name: Filter by metric name
            status: Filter by status
            limit: Maximum number of records to return
            
        Returns:
            List of EquipmentMetric objects
        """
        query = self.db.query(EquipmentMetric)
        
        filters = []
        if start_date:
            filters.append(EquipmentMetric.timestamp >= start_date)
        if end_date:
            filters.append(EquipmentMetric.timestamp <= end_date)
        if equipment_id:
            filters.append(EquipmentMetric.equipment_id == equipment_id)
        if metric_name:
            filters.append(EquipmentMetric.metric_name == metric_name)
        if status:
            filters.append(EquipmentMetric.status == status)
        
        if filters:
            query = query.filter(and_(*filters))
        
        return query.order_by(EquipmentMetric.timestamp.desc()).limit(limit).all()
    
    def get_key_metrics(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        equipment_id: Optional[str] = None,
        metric_name: Optional[str] = None,
        status: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Calculate key metrics for equipment data.
        
        Returns:
            Dictionary with metrics: count, average, min, max
        """
        query = self.db.query(
            func.count(EquipmentMetric.id).label('count'),
            func.avg(EquipmentMetric.value).label('average'),
            func.min(EquipmentMetric.value).label('min'),
            func.max(EquipmentMetric.value).label('max')
        )
        
        filters = []
        if start_date:
            filters.append(EquipmentMetric.timestamp >= start_date)
        if end_date:
            filters.append(EquipmentMetric.timestamp <= end_date)
        if equipment_id:
            filters.append(EquipmentMetric.equipment_id == equipment_id)
        if metric_name:
            filters.append(EquipmentMetric.metric_name == metric_name)
        if status:
            filters.append(EquipmentMetric.status == status)
        
        if filters:
            query = query.filter(and_(*filters))
        
        result = query.first()
        
        return {
            'count': result.count if result.count else 0,
            'average': float(result.average) if result.average else 0.0,
            'min': float(result.min) if result.min else 0.0,
            'max': float(result.max) if result.max else 0.0
        }
    
    def get_time_series_data(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        equipment_id: Optional[str] = None,
        metric_name: Optional[str] = None,
        status: Optional[str] = None,
        group_by: str = 'day'
    ) -> List[Dict[str, Any]]:
        """
        Get time series data for charts.
        
        Args:
            start_date: Filter by start date
            end_date: Filter by end date
            equipment_id: Filter by equipment ID
            metric_name: Filter by metric name
            status: Filter by status
            group_by: Grouping period ('day' or 'month')
            
        Returns:
            List of dictionaries with date and aggregated values
        """
        metrics = self.get_filtered_metrics(
            start_date=start_date,
            end_date=end_date,
            equipment_id=equipment_id,
            metric_name=metric_name,
            status=status,
            limit=10000
        )
        
        if not metrics:
            return []
        
        # Convert to pandas DataFrame for easier aggregation
        df = pd.DataFrame([
            {
                'timestamp': m.timestamp,
                'value': m.value,
                'equipment_id': m.equipment_id
            }
            for m in metrics
        ])
        
        # Group by period
        if group_by == 'month':
            df['period'] = pd.to_datetime(df['timestamp']).dt.to_period('M')
        else:  # day
            df['period'] = pd.to_datetime(df['timestamp']).dt.date
        
        # Aggregate
        grouped = df.groupby('period').agg({
            'value': ['mean', 'min', 'max', 'count']
        }).reset_index()
        
        grouped.columns = ['period', 'avg_value', 'min_value', 'max_value', 'count']
        
        # Convert to list of dicts
        result = []
        for _, row in grouped.iterrows():
            result.append({
                'period': str(row['period']),
                'avg_value': float(row['avg_value']),
                'min_value': float(row['min_value']),
                'max_value': float(row['max_value']),
                'count': int(row['count'])
            })
        
        return result
    
    def get_equipment_breakdown(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        metric_name: Optional[str] = None,
        status: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get breakdown by equipment.
        
        Returns:
            List of dictionaries with equipment and aggregated values
        """
        query = self.db.query(
            EquipmentMetric.equipment_id,
            func.avg(EquipmentMetric.value).label('average'),
            func.count(EquipmentMetric.id).label('count')
        )
        
        filters = []
        if start_date:
            filters.append(EquipmentMetric.timestamp >= start_date)
        if end_date:
            filters.append(EquipmentMetric.timestamp <= end_date)
        if metric_name:
            filters.append(EquipmentMetric.metric_name == metric_name)
        if status:
            filters.append(EquipmentMetric.status == status)
        
        if filters:
            query = query.filter(and_(*filters))
        
        query = query.group_by(EquipmentMetric.equipment_id)
        results = query.all()
        
        return [
            {
                'equipment_id': r.equipment_id,
                'average_value': float(r.average),
                'count': r.count
            }
            for r in results
        ]
    
    def get_available_equipment(self) -> List[str]:
        """Get list of all available equipment IDs."""
        results = self.db.query(EquipmentMetric.equipment_id).distinct().all()
        return [r.equipment_id for r in results]
    
    def get_available_metrics(self) -> List[str]:
        """Get list of all available metric names."""
        results = self.db.query(EquipmentMetric.metric_name).distinct().all()
        return [r.metric_name for r in results]
    
    def get_available_statuses(self) -> List[str]:
        """Get list of all available statuses."""
        results = self.db.query(EquipmentMetric.status).distinct().all()
        return [r.status for r in results]
