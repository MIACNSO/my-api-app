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

@app.get("/Divisions/", response_model=list[schemas.DivisionsOut])
def read_clinics(db:Session = Depends(get_db)):
    return crud.get_divisions(db)

@app.get("/Sites/", response_model=list[schemas.SitesOut])
def read_clinics(db:Session = Depends(get_db)):
    return crud.get_sites(db)

@app.get("/Lpu/", response_model=list[schemas.LpuOut])
def read_clinics(db:Session = Depends(get_db)):
    return crud.get_lpu(db)




# @app.post("/clinics/", response_model=schemas.Clinic)
# def create_clinic(clinic: schemas.ClinicCreate, db: Session = Depends(get_db)):
#     return crud.create_clinic(db,clinic)