import pandas as pd
import os
import database

# Подключение к БД в Docker
DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
DB_NAME = os.getenv("POSTGRES_DB", "clinics")
DB_HOST = os.getenv("DB_HOST", "clinics_db")  # Имя контейнера БД в Docker Compose
DB_PORT = os.getenv("DB_PORT", "5432")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создаём подключение
engine = database.engine

for tablename in ['lpu', 'divisions', 'site']:
    # Читаем CSV
    csv_file = f"app/{tablename}.csv"
    df = pd.read_csv(csv_file, delimiter=";")

    # Записываем в таблицу
    df.to_sql(tablename, con=engine, if_exists="append", index=False)

    print(f"Данные успешно загружены в таблицу {tablename}.")