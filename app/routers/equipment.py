"""
Equipment metrics API endpoints.
"""
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.equipment_service import EquipmentService

router = APIRouter(prefix="/equipment", tags=["equipment"])


@router.get("/metrics")
def get_equipment_metrics(
    start_date: Optional[datetime] = Query(None, description="Start date filter"),
    end_date: Optional[datetime] = Query(None, description="End date filter"),
    equipment_id: Optional[str] = Query(None, description="Equipment ID filter"),
    metric_name: Optional[str] = Query(None, description="Metric name filter"),
    status: Optional[str] = Query(None, description="Status filter"),
    db: Session = Depends(get_db)
):
    """Get key metrics for equipment data."""
    service = EquipmentService(db)
    return service.get_key_metrics(
        start_date=start_date,
        end_date=end_date,
        equipment_id=equipment_id,
        metric_name=metric_name,
        status=status
    )


@router.get("/time-series")
def get_equipment_time_series(
    start_date: Optional[datetime] = Query(None, description="Start date filter"),
    end_date: Optional[datetime] = Query(None, description="End date filter"),
    equipment_id: Optional[str] = Query(None, description="Equipment ID filter"),
    metric_name: Optional[str] = Query(None, description="Metric name filter"),
    status: Optional[str] = Query(None, description="Status filter"),
    group_by: str = Query("day", description="Group by period: day or month"),
    db: Session = Depends(get_db)
):
    """Get time series data for charts."""
    service = EquipmentService(db)
    return service.get_time_series_data(
        start_date=start_date,
        end_date=end_date,
        equipment_id=equipment_id,
        metric_name=metric_name,
        status=status,
        group_by=group_by
    )


@router.get("/equipment-breakdown")
def get_equipment_breakdown(
    start_date: Optional[datetime] = Query(None, description="Start date filter"),
    end_date: Optional[datetime] = Query(None, description="End date filter"),
    metric_name: Optional[str] = Query(None, description="Metric name filter"),
    status: Optional[str] = Query(None, description="Status filter"),
    db: Session = Depends(get_db)
):
    """Get breakdown by equipment."""
    service = EquipmentService(db)
    return service.get_equipment_breakdown(
        start_date=start_date,
        end_date=end_date,
        metric_name=metric_name,
        status=status
    )


@router.get("/list")
def get_equipment_list(
    start_date: Optional[datetime] = Query(None, description="Start date filter"),
    end_date: Optional[datetime] = Query(None, description="End date filter"),
    equipment_id: Optional[str] = Query(None, description="Equipment ID filter"),
    metric_name: Optional[str] = Query(None, description="Metric name filter"),
    status: Optional[str] = Query(None, description="Status filter"),
    limit: int = Query(100, description="Maximum number of records"),
    db: Session = Depends(get_db)
):
    """Get filtered list of equipment metrics."""
    service = EquipmentService(db)
    metrics = service.get_filtered_metrics(
        start_date=start_date,
        end_date=end_date,
        equipment_id=equipment_id,
        metric_name=metric_name,
        status=status,
        limit=limit
    )
    
    return [
        {
            'id': m.id,
            'timestamp': m.timestamp.isoformat(),
            'equipment_id': m.equipment_id,
            'metric_name': m.metric_name,
            'value': m.value,
            'unit': m.unit,
            'status': m.status
        }
        for m in metrics
    ]


@router.get("/filters")
def get_equipment_filters(db: Session = Depends(get_db)):
    """Get available filter options."""
    service = EquipmentService(db)
    return {
        'equipment_ids': service.get_available_equipment(),
        'metric_names': service.get_available_metrics(),
        'statuses': service.get_available_statuses()
    }
