"""
Equipment Metric model for technical/operational data.
Example use case: equipment monitoring, temperature, load, failures tracking.
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime

from app.database import Base


class EquipmentMetric(Base):
    """
    Equipment Metric model for technical operations monitoring.
    
    Attributes:
        id: Primary key
        timestamp: Measurement timestamp
        equipment_id: Equipment identifier
        metric_name: Name of the metric (e.g., 'temperature', 'load', 'pressure')
        value: Metric value
        unit: Unit of measurement (e.g., 'celsius', 'percent', 'bar')
        status: Equipment status (e.g., 'normal', 'warning', 'critical')
    """
    __tablename__ = "equipment_metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    equipment_id = Column(String(50), nullable=False, index=True)
    metric_name = Column(String(50), nullable=False, index=True)
    value = Column(Float, nullable=False)
    unit = Column(String(20), nullable=True)
    status = Column(String(20), nullable=False, default="normal", index=True)
    
    def __repr__(self):
        return f"<EquipmentMetric(id={self.id}, equipment={self.equipment_id}, metric={self.metric_name}, value={self.value})>"
