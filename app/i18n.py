"""
Internationalization (i18n) module.
Contains translations for all UI strings.
"""

TRANSLATIONS = {
    'en': {
        # Navigation
        'app_name': 'Dashboard Analytics',
        'nav_home': 'Home',
        'nav_transactions': 'Transactions',
        'nav_equipment': 'Equipment',
        
        # Home page
        'home_title': 'Dashboard Analytics',
        'home_subtitle': 'Configurable operational reporting dashboard with SQL data',
        'financial_transactions': 'Financial Transactions',
        'financial_desc': 'Track revenue, payments, and orders. Analyze financial metrics with customizable filters and time-based visualizations.',
        'equipment_monitoring': 'Equipment Monitoring',
        'equipment_desc': 'Monitor equipment metrics, track performance, and analyze operational parameters with real-time data visualization.',
        'open_dashboard': 'Open Dashboard',
        'key_features': 'Key Features',
        
        # Features
        'feature_filtering': 'Advanced Filtering',
        'feature_filtering_desc': 'Filter data by date ranges, categories, and custom parameters',
        'feature_charts': 'Interactive Charts',
        'feature_charts_desc': 'Visualize trends with dynamic time-series charts',
        'feature_tables': 'Detailed Tables',
        'feature_tables_desc': 'View and export detailed data tables',
        'feature_metrics': 'Key Metrics',
        'feature_metrics_desc': 'Track important KPIs at a glance',
        'feature_sql': 'SQL Integration',
        'feature_sql_desc': 'Direct connection to SQL databases',
        'feature_custom': 'Customizable',
        'feature_custom_desc': 'Easily adapt to different data domains',
        
        # Feature list items
        'revenue_tracking': 'Revenue tracking',
        'category_breakdown': 'Category breakdown',
        'time_series_analysis': 'Time series analysis',
        'status_filtering': 'Status filtering',
        'performance_metrics': 'Performance metrics',
        'equipment_comparison': 'Equipment comparison',
        'trend_analysis': 'Trend analysis',
        'status_monitoring': 'Status monitoring',
        
        # Transactions Dashboard
        'transactions_title': 'Financial Transactions Dashboard',
        'equipment_title': 'Equipment Monitoring Dashboard',
        
        # Filters
        'filters': 'Filters',
        'start_date': 'Start Date',
        'end_date': 'End Date',
        'category': 'Category',
        'all_categories': 'All Categories',
        'status': 'Status',
        'all_statuses': 'All Statuses',
        'group_by': 'Group By',
        'day': 'Day',
        'month': 'Month',
        'apply_filters': 'Apply Filters',
        'reset': 'Reset',
        'equipment': 'Equipment',
        'all_equipment': 'All Equipment',
        'metric': 'Metric',
        'all_metrics': 'All Metrics',
        
        # Metrics
        'total_amount': 'Total Amount',
        'transaction_count': 'Transaction Count',
        'average_amount': 'Average Amount',
        'max_amount': 'Max Amount',
        'measurement_count': 'Measurement Count',
        'average_value': 'Average Value',
        'min_value': 'Min Value',
        'max_value': 'Max Value',
        
        # Charts
        'time_series': 'Time Series',
        'category_breakdown_chart': 'Category Breakdown',
        'equipment_breakdown': 'Equipment Breakdown',
        
        # Tables
        'transaction_details': 'Transaction Details',
        'measurement_details': 'Measurement Details',
        'id': 'ID',
        'date': 'Date',
        'amount': 'Amount',
        'description': 'Description',
        'customer_id': 'Customer ID',
        'timestamp': 'Timestamp',
        'value': 'Value',
        'unit': 'Unit',
        
        # Messages
        'loading': 'Loading...',
        'no_data': 'No data available',
        'error_loading': 'Error loading data. Please try again.',
        
        # Equipment metric names
        'metric_temperature': 'Temperature',
        'metric_cpu_load': 'CPU Load',
        'metric_memory_usage': 'Memory Usage',
        'metric_vibration': 'Vibration',
        'metric_pressure': 'Pressure',
        'metric_rpm': 'RPM',
        'metric_power_consumption': 'Power Consumption',
        'metric_efficiency': 'Efficiency',
        'critical_events': 'Critical Events',
        'failure_count': 'Failure Count',
    },
    'ru': {
        # Навигация
        'app_name': 'Аналитическая Панель',
        'nav_home': 'Главная',
        'nav_transactions': 'Транзакции',
        'nav_equipment': 'Оборудование',
        
        # Главная страница
        'home_title': 'Аналитическая Панель',
        'home_subtitle': 'Настраиваемая панель оперативной отчётности с данными из SQL',
        'financial_transactions': 'Финансовые Транзакции',
        'financial_desc': 'Отслеживайте выручку, платежи и заказы. Анализируйте финансовые показатели с настраиваемыми фильтрами и визуализацией по времени.',
        'equipment_monitoring': 'Мониторинг Оборудования',
        'equipment_desc': 'Отслеживайте метрики оборудования, производительность и анализируйте операционные параметры с визуализацией данных в реальном времени.',
        'open_dashboard': 'Открыть Панель',
        'key_features': 'Ключевые Возможности',
        
        # Возможности
        'feature_filtering': 'Расширенная Фильтрация',
        'feature_filtering_desc': 'Фильтруйте данные по диапазонам дат, категориям и пользовательским параметрам',
        'feature_charts': 'Интерактивные Графики',
        'feature_charts_desc': 'Визуализируйте тренды с помощью динамических временных графиков',
        'feature_tables': 'Детальные Таблицы',
        'feature_tables_desc': 'Просматривайте и экспортируйте детальные таблицы данных',
        'feature_metrics': 'Ключевые Метрики',
        'feature_metrics_desc': 'Отслеживайте важные KPI с первого взгляда',
        'feature_sql': 'Интеграция с SQL',
        'feature_sql_desc': 'Прямое подключение к SQL базам данных',
        'feature_custom': 'Настраиваемость',
        'feature_custom_desc': 'Легко адаптируется под различные предметные области',
        
        # Элементы списка возможностей
        'revenue_tracking': 'Отслеживание выручки',
        'category_breakdown': 'Разбивка по категориям',
        'time_series_analysis': 'Анализ временных рядов',
        'status_filtering': 'Фильтрация по статусу',
        'performance_metrics': 'Метрики производительности',
        'equipment_comparison': 'Сравнение оборудования',
        'trend_analysis': 'Анализ трендов',
        'status_monitoring': 'Мониторинг статуса',
        
        # Панели
        'transactions_title': 'Панель Финансовых Транзакций',
        'equipment_title': 'Панель Мониторинга Оборудования',
        
        # Фильтры
        'filters': 'Фильтры',
        'start_date': 'Дата начала',
        'end_date': 'Дата окончания',
        'category': 'Категория',
        'all_categories': 'Все категории',
        'status': 'Статус',
        'all_statuses': 'Все статусы',
        'group_by': 'Группировка',
        'day': 'День',
        'month': 'Месяц',
        'apply_filters': 'Применить фильтры',
        'reset': 'Сбросить',
        'equipment': 'Оборудование',
        'all_equipment': 'Всё оборудование',
        'metric': 'Метрика',
        'all_metrics': 'Все метрики',
        
        # Метрики
        'total_amount': 'Общая Сумма',
        'transaction_count': 'Количество Транзакций',
        'average_amount': 'Средняя Сумма',
        'max_amount': 'Максимальная Сумма',
        'measurement_count': 'Количество Измерений',
        'average_value': 'Среднее Значение',
        'min_value': 'Минимальное Значение',
        'max_value': 'Максимальное Значение',
        
        # Графики
        'time_series': 'Временной Ряд',
        'category_breakdown_chart': 'Разбивка по Категориям',
        'equipment_breakdown': 'Разбивка по Оборудованию',
        
        # Таблицы
        'transaction_details': 'Детали Транзакций',
        'measurement_details': 'Детали Измерений',
        'id': 'ID',
        'date': 'Дата',
        'amount': 'Сумма',
        'description': 'Описание',
        'customer_id': 'ID Клиента',
        'timestamp': 'Время',
        'value': 'Значение',
        'unit': 'Единица',
        
        # Сообщения
        'loading': 'Загрузка...',
        'no_data': 'Нет данных',
        'error_loading': 'Ошибка загрузки данных. Попробуйте снова.',
        
        # Названия метрик оборудования
        'metric_temperature': 'Температура',
        'metric_cpu_load': 'Загрузка ЦП',
        'metric_memory_usage': 'Использование памяти',
        'metric_vibration': 'Вибрация',
        'metric_pressure': 'Давление',
        'metric_rpm': 'Обороты',
        'metric_power_consumption': 'Потребление энергии',
        'metric_efficiency': 'Эффективность',
        'critical_events': 'Критические события',
        'failure_count': 'Количество отказов',
    }
}


def get_translation(lang: str = 'en') -> dict:
    """
    Get translation dictionary for specified language.
    
    Args:
        lang: Language code ('en' or 'ru')
        
    Returns:
        Dictionary with translations
    """
    return TRANSLATIONS.get(lang, TRANSLATIONS['en'])


def get_available_languages() -> list:
    """Get list of available language codes."""
    return list(TRANSLATIONS.keys())
