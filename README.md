# Dashboard Analytics [EN] 
[🇷🇺](README_RU.md)
A configurable web dashboard for operational reporting with SQL data. Built with Python, FastAPI, and modern web technologies.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📋 Overview

Dashboard Analytics is a flexible, production-ready web application for creating operational dashboards with real-time data visualization. It supports multiple data domains including financial transactions and equipment monitoring, with easy customization for other use cases.

### Key Features

- 🔍 **Advanced Filtering**: Filter data by date ranges, categories, and custom parameters
- 📊 **Interactive Visualizations**: Dynamic charts powered by Plotly.js
- 📈 **Time Series Analysis**: Track trends over time with day/month grouping
- 📑 **Detailed Tables**: View and analyze detailed data records
- 🎯 **Key Metrics**: Monitor important KPIs at a glance
- 🔌 **SQL Integration**: Direct connection to SQLite or PostgreSQL databases
- 🎨 **Modern UI**: Clean, responsive interface built with Bootstrap 5
- ⚙️ **Highly Configurable**: Easy to adapt for different data domains
- 🌍 **Multi-language Support**: English and Russian interface (i18n ready)

## 🏗️ Architecture

```
dashboard-project/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── config.py               # Configuration management
│   ├── database.py             # Database connection and session
│   ├── models/                 # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   ├── transaction.py      # Financial transaction model
│   │   └── equipment_metric.py # Equipment monitoring model
│   ├── services/               # Business logic layer
│   │   ├── __init__.py
│   │   ├── transaction_service.py
│   │   └── equipment_service.py
│   ├── routers/                # API endpoints
│   │   ├── __init__.py
│   │   ├── dashboard.py        # HTML page routes
│   │   ├── transactions.py     # Transaction API
│   │   └── equipment.py        # Equipment API
│   ├── templates/              # Jinja2 HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── transactions_dashboard.html
│   │   └── equipment_dashboard.html
│   ├── static/                 # Static files (CSS, JS, images)
│   └── i18n.py                 # Internationalization (translations)
├── scripts/
│   ├── __init__.py
│   └── seed_data.py            # Demo data generation script
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variables template
├── .gitignore
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

### Installation

1. **Clone or download the repository**

```bash
git clone <repository-url>
cd dashboard-project
```

2. **Create and activate a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

```bash
# Copy the example file
copy .env.example .env  # Windows
cp .env.example .env    # Linux/Mac

# Edit .env file with your settings (optional)
```

5. **Initialize database and load demo data**

```bash
python scripts/seed_data.py
```

6. **Run the application**

```bash
python -m uvicorn app.main:app --reload
```

7. **Open your browser**

Navigate to: `http://localhost:8000`

**Language Selection:**
- English: `http://localhost:8000/?lang=en`
- Russian: `http://localhost:8000/?lang=ru`
- Or use the language switcher in the top-right corner of the navigation bar

## 📊 Data Models

### Transaction Model (Financial Data)

Used for tracking financial operations like revenue, payments, and orders.

```python
class Transaction:
    id: int                    # Primary key
    date: datetime             # Transaction date and time
    category: str              # Category (e.g., 'sales', 'refund', 'subscription')
    amount: float              # Transaction amount
    status: str                # Status (e.g., 'completed', 'pending', 'failed')
    description: str           # Optional description
    customer_id: str           # Optional customer identifier
```

**Example Use Cases:**
- E-commerce sales tracking
- Payment processing monitoring
- Subscription revenue analysis
- Refund management

### Equipment Metric Model (Technical Data)

Used for monitoring equipment performance and operational parameters.

```python
class EquipmentMetric:
    id: int                    # Primary key
    timestamp: datetime        # Measurement timestamp
    equipment_id: str          # Equipment identifier
    metric_name: str           # Metric name (e.g., 'temperature', 'load', 'pressure')
    value: float               # Metric value
    unit: str                  # Unit of measurement (e.g., 'celsius', 'percent')
    status: str                # Status (e.g., 'normal', 'warning', 'critical')
```

**Example Use Cases:**
- Industrial equipment monitoring
- IoT sensor data tracking
- Server performance monitoring
- Environmental condition tracking

## 🔧 Configuration

### Database Configuration

The application supports both SQLite and PostgreSQL databases.

**SQLite (Default):**
```env
DATABASE_URL=sqlite:///./dashboard.db
```

**PostgreSQL:**
```env
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```

### Application Settings

Edit the `.env` file to customize:

```env
# Database
DATABASE_URL=sqlite:///./dashboard.db

# Application
APP_NAME=Dashboard Analytics
DEBUG=True
```

## 🎨 Customization Guide

### Adding a New Data Domain

1. **Create a new model** in `app/models/`:

```python
# app/models/your_model.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database import Base

class YourModel(Base):
    __tablename__ = "your_table"
    
    id = Column(Integer, primary_key=True, index=True)
    # Add your columns here
```

2. **Create a service** in `app/services/`:

```python
# app/services/your_service.py
from sqlalchemy.orm import Session
from app.models.your_model import YourModel

class YourService:
    def __init__(self, db: Session):
        self.db = db
    
    # Add your business logic methods
```

3. **Create API endpoints** in `app/routers/`:

```python
# app/routers/your_router.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/your-endpoint", tags=["your-tag"])

@router.get("/metrics")
def get_metrics(db: Session = Depends(get_db)):
    # Your endpoint logic
    pass
```

4. **Create a dashboard template** in `app/templates/`:

```html
<!-- app/templates/your_dashboard.html -->
{% extends "base.html" %}
{% block content %}
<!-- Your dashboard HTML -->
{% endblock %}
```

5. **Register the router** in `app/main.py`:

```python
from app.routers import your_router
app.include_router(your_router.router, prefix="/api/v1")
```

## 📡 API Documentation

Once the application is running, access the interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Main Endpoints

#### Transaction Endpoints

- `GET /api/v1/transactions/metrics` - Get key metrics
- `GET /api/v1/transactions/time-series` - Get time series data
- `GET /api/v1/transactions/category-breakdown` - Get category breakdown
- `GET /api/v1/transactions/list` - Get filtered transaction list
- `GET /api/v1/transactions/filters` - Get available filter options

#### Equipment Endpoints

- `GET /api/v1/equipment/metrics` - Get key metrics
- `GET /api/v1/equipment/time-series` - Get time series data
- `GET /api/v1/equipment/equipment-breakdown` - Get equipment breakdown
- `GET /api/v1/equipment/list` - Get filtered metrics list
- `GET /api/v1/equipment/filters` - Get available filter options

## 🧪 Development

### Running in Development Mode

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Adding Test Data

```bash
python scripts/seed_data.py
```

### Database Migrations

For production use, consider using Alembic for database migrations:

```bash
# Initialize Alembic (first time only)
alembic init alembic

# Create a migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head
```

## 📦 Deployment

### Production Considerations

1. **Use PostgreSQL** instead of SQLite for better performance
2. **Set DEBUG=False** in production
3. **Use a production ASGI server** like Gunicorn with Uvicorn workers:

```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

4. **Set up environment variables** securely
5. **Use HTTPS** with a reverse proxy (nginx, Apache)
6. **Implement authentication** if needed
7. **Set up monitoring and logging**

### Docker Deployment (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t dashboard-analytics .
docker run -p 8000:8000 dashboard-analytics
```

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **Pandas** - Data manipulation and analysis
- **Uvicorn** - ASGI server implementation

### Frontend
- **Bootstrap 5** - CSS framework for responsive design
- **Plotly.js** - Interactive charting library
- **Jinja2** - Template engine

### Database
- **SQLite** - Default embedded database
- **PostgreSQL** - Recommended for production

## 📝 Use Cases

### Financial Analytics
- Revenue tracking and forecasting
- Payment processing monitoring
- Subscription management
- Sales performance analysis

### Equipment Monitoring
- Industrial equipment tracking
- IoT sensor data visualization
- Server performance monitoring
- Predictive maintenance

### Custom Domains
The architecture is designed to be easily adapted for:
- Customer analytics
- Inventory management
- Supply chain monitoring
- Quality control metrics
- HR analytics
- Marketing campaign tracking

## 🤝 Contributing

This is a demonstration project for portfolio purposes. Feel free to fork and adapt it for your needs.

## 📄 License

MIT License - feel free to use this project for learning and portfolio purposes.

## 👨‍💻 Author

Created as a demonstration project for Junior Python/ML/DS developer portfolio.

## 🔗 Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Plotly.js Documentation](https://plotly.com/javascript/)
- [Bootstrap Documentation](https://getbootstrap.com/)

## 📞 Support

For questions or issues, please open an issue in the repository.

---

**Note**: This is a demonstration project designed to showcase skills in:
- Python web development
- SQL and ORM usage
- Data aggregation and reporting
- Dashboard creation
- Clean code architecture
- Internationalization (i18n)
- Documentation

## 🌍 Internationalization

The project supports multiple languages out of the box. See [I18N_GUIDE.md](I18N_GUIDE.md) for detailed information on:
- How to switch languages
- Adding new languages
- Adding new translation strings
- Architecture and best practices
