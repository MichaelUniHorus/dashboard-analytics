"""
Dashboard page routes.
Serves HTML templates for the web interface.
"""
from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.transaction_service import TransactionService
from app.services.equipment_service import EquipmentService
from app.i18n import get_translation

router = APIRouter(tags=["dashboard"])
templates = Jinja2Templates(directory="app/templates")


def get_language(request: Request) -> str:
    """Get language from query parameter or cookie, default to 'en'."""
    lang = request.query_params.get('lang')
    if not lang:
        lang = request.cookies.get('lang', 'en')
    return lang if lang in ['en', 'ru'] else 'en'


@router.get("/", response_class=HTMLResponse)
def dashboard_home(request: Request):
    """Main dashboard page with domain selection."""
    lang = get_language(request)
    t = get_translation(lang)
    
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "t": t, "lang": lang}
    )


@router.get("/transactions", response_class=HTMLResponse)
def transactions_dashboard(request: Request, db: Session = Depends(get_db)):
    """Transactions dashboard page."""
    lang = get_language(request)
    t = get_translation(lang)
    service = TransactionService(db)
    
    # Get filter options
    categories = service.get_available_categories()
    statuses = service.get_available_statuses()
    
    return templates.TemplateResponse(
        "transactions_dashboard.html",
        {
            "request": request,
            "t": t,
            "lang": lang,
            "categories": categories,
            "statuses": statuses
        }
    )


@router.get("/equipment", response_class=HTMLResponse)
def equipment_dashboard(request: Request, db: Session = Depends(get_db)):
    """Equipment metrics dashboard page."""
    lang = get_language(request)
    t = get_translation(lang)
    service = EquipmentService(db)
    
    # Get filter options
    equipment_ids = service.get_available_equipment()
    metric_names = service.get_available_metrics()
    statuses = service.get_available_statuses()
    
    return templates.TemplateResponse(
        "equipment_dashboard.html",
        {
            "request": request,
            "t": t,
            "lang": lang,
            "equipment_ids": equipment_ids,
            "metric_names": metric_names,
            "statuses": statuses
        }
    )
