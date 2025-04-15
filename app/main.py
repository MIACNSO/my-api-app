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

@app.get("/divisions/", response_model=list[schemas.DivisionsOut])
def read_clinics(db:Session = Depends(get_db)):
    return crud.get_divisions(db)

@app.get("/sites/", response_model=list[schemas.SitesOut])
def read_clinics(db:Session = Depends(get_db)):
    return crud.get_sites(db)

@app.get("/lpu/", response_model=list[schemas.LpuOut])
def read_clinics(db:Session = Depends(get_db)):
    return crud.get_lpu(db)

@app.get("/address/", response_model=list[schemas.AddressOut])
def read_clinics(db:Session = Depends(get_db)):
    return crud.get_address(db)

