import csv
from app.database import SessionLocal
from app.models import Lpu  # или нужную вам модель

def import_lpu_from_csv(file_path: str):
    session = SessionLocal()
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        # Преобразование строк CSV в словари, соответствующие полям модели
        data = []
        for row in reader:
            print(row)
            data.append({
                "id": int(row["id"]),
                "code_lpu": int(row["code_lpu"]),
                "fullname": row["fullname"],
                "lpu_name": row["lpu_name"],
            })
    # Для ускорения можно использовать bulk_insert_mappings
    session.bulk_insert_mappings(Lpu, data)
    session.commit()
    session.close()

if __name__ == "__main__":
    import_lpu_from_csv("lpu.csv")