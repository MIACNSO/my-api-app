from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, crud, schemas
from app.database import SessionLocal, engine

# Инициализация базы данных
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clinics API", version = "1.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/clinics/", response_model=list[schemas.Clinic])
def read_clinics(db:Session = Depends(get_db)):
    return crud.get_clinics(db)

@app.post("/cinics/", response_model=schemas.Clinic)
def create_clinic(clinic: schemas.ClinicCreate, db: Session = Depends(get_db)):
    return crud.create_clinic(db,clinic)