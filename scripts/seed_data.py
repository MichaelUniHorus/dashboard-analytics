"""
Demo data seeding script.
Populates the database with sample data for both transactions and equipment metrics.
"""
import sys
import os
from datetime import datetime, timedelta
import random

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import SessionLocal, init_db
from app.models.transaction import Transaction
from app.models.equipment_metric import EquipmentMetric


def seed_transactions(db, num_records=200):
    """
    Seed transaction data.
    
    Args:
        db: Database session
        num_records: Number of records to create
    """
    print(f"Seeding {num_records} transaction records...")
    
    categories = ['sales', 'refund', 'subscription', 'service', 'product']
    statuses = ['completed', 'pending', 'failed', 'cancelled']
    
    # Generate data for the last 90 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)
    
    transactions = []
    for i in range(num_records):
        # Random date within range
        days_offset = random.randint(0, 90)
        transaction_date = start_date + timedelta(days=days_offset)
        
        # Random amount (weighted towards lower values)
        amount = round(random.lognormvariate(4, 1.5), 2)
        
        # Random category and status
        category = random.choice(categories)
        status = random.choices(
            statuses,
            weights=[70, 15, 10, 5]  # Most are completed
        )[0]
        
        # Customer ID (some are None)
        customer_id = f"CUST{random.randint(1000, 9999)}" if random.random() > 0.2 else None
        
        # Description
        descriptions = [
            f"{category.capitalize()} transaction",
            f"Monthly {category}",
            f"One-time {category}",
            None
        ]
        description = random.choice(descriptions)
        
        transaction = Transaction(
            date=transaction_date,
            category=category,
            amount=amount,
            status=status,
            description=description,
            customer_id=customer_id
        )
        transactions.append(transaction)
    
    db.bulk_save_objects(transactions)
    db.commit()
    print(f"✓ Created {num_records} transaction records")


def seed_equipment_metrics(db, num_records=1000):
    """
    Seed equipment metrics data with realistic industrial monitoring data.
    
    Args:
        db: Database session
        num_records: Number of records to create
    """
    print(f"Seeding {num_records} equipment metric records...")
    
    # Реалистичные названия оборудования
    equipment_ids = [
        'PUMP-A1', 'PUMP-A2', 'PUMP-B1',
        'COMPRESSOR-01', 'COMPRESSOR-02',
        'TURBINE-T1', 'TURBINE-T2',
        'MOTOR-M1', 'MOTOR-M2', 'MOTOR-M3'
    ]
    
    # Расширенный набор метрик
    metric_names = [
        'temperature',      # Температура
        'cpu_load',        # Загруженность CPU/процессора
        'memory_usage',    # Использование памяти
        'vibration',       # Вибрация
        'pressure',        # Давление
        'rpm',             # Обороты в минуту
        'power_consumption', # Потребление энергии
        'efficiency'       # Эффективность
    ]
    
    units = {
        'temperature': '°C',
        'cpu_load': '%',
        'memory_usage': '%',
        'vibration': 'mm/s',
        'pressure': 'bar',
        'rpm': 'об/мин',
        'power_consumption': 'kW',
        'efficiency': '%'
    }
    
    # Нормальные диапазоны для каждой метрики
    normal_ranges = {
        'temperature': (35, 75),      # Рабочая температура
        'cpu_load': (20, 85),          # Загрузка процессора
        'memory_usage': (30, 80),      # Использование памяти
        'vibration': (0.5, 4.0),       # Вибрация
        'pressure': (2.5, 8.5),        # Давление
        'rpm': (1200, 3000),           # Обороты
        'power_consumption': (15, 95), # Потребление энергии
        'efficiency': (70, 95)         # Эффективность
    }
    
    # Generate data for the last 30 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    
    # Счётчик отказов для каждого оборудования
    failure_counts = {eq_id: 0 for eq_id in equipment_ids}
    
    metrics = []
    for i in range(num_records):
        # Random timestamp within range
        hours_offset = random.randint(0, 30 * 24)
        timestamp = start_date + timedelta(hours=hours_offset)
        
        # Random equipment and metric
        equipment_id = random.choice(equipment_ids)
        metric_name = random.choice(metric_names)
        unit = units[metric_name]
        
        # Generate value within normal range with occasional outliers
        min_val, max_val = normal_ranges[metric_name]
        
        # 15% вероятность аномальных значений
        if random.random() > 0.85:
            # Аномальное значение
            if random.random() > 0.5:
                value = random.uniform(max_val * 1.05, max_val * 1.25)
            else:
                value = random.uniform(min_val * 0.5, min_val * 0.9)
        else:
            # Нормальное значение с небольшим разбросом
            value = random.uniform(min_val, max_val)
        
        # Округление в зависимости от типа метрики
        if metric_name in ['rpm']:
            value = round(value, 0)
        else:
            value = round(value, 2)
        
        # Determine status based on value
        if value > max_val * 1.1 or value < min_val * 0.8:
            status = 'critical'
            failure_counts[equipment_id] += 1
        elif value > max_val * 0.95 or value < min_val * 0.9:
            status = 'warning'
        else:
            status = 'normal'
        
        metric = EquipmentMetric(
            timestamp=timestamp,
            equipment_id=equipment_id,
            metric_name=metric_name,
            value=value,
            unit=unit,
            status=status
        )
        metrics.append(metric)
    
    db.bulk_save_objects(metrics)
    db.commit()
    
    # Вывод статистики по отказам
    print(f"✓ Created {num_records} equipment metric records")
    print("\n📊 Статистика по критическим событиям:")
    for eq_id, count in sorted(failure_counts.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            print(f"   {eq_id}: {count} критических событий")


def main():
    """Main seeding function."""
    print("=" * 60)
    print("Dashboard Analytics - Demo Data Seeding")
    print("=" * 60)
    
    # Initialize database
    print("\nInitializing database...")
    init_db()
    print("✓ Database initialized")
    
    # Create session
    db = SessionLocal()
    
    try:
        # Check if data already exists
        existing_transactions = db.query(Transaction).count()
        existing_metrics = db.query(EquipmentMetric).count()
        
        if existing_transactions > 0 or existing_metrics > 0:
            print(f"\nWarning: Database already contains data:")
            print(f"  - Transactions: {existing_transactions}")
            print(f"  - Equipment Metrics: {existing_metrics}")
            
            response = input("\nDo you want to add more data? (y/n): ")
            if response.lower() != 'y':
                print("Seeding cancelled.")
                return
        
        # Seed data
        print("\nSeeding data...")
        seed_transactions(db, num_records=200)
        seed_equipment_metrics(db, num_records=1000)
        
        # Summary
        total_transactions = db.query(Transaction).count()
        total_metrics = db.query(EquipmentMetric).count()
        
        print("\n" + "=" * 60)
        print("Seeding completed successfully!")
        print("=" * 60)
        print(f"Total Transactions: {total_transactions}")
        print(f"Total Equipment Metrics: {total_metrics}")
        print("\nYou can now start the application with:")
        print("  python -m uvicorn app.main:app --reload")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Error during seeding: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
