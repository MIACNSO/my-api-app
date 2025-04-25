from fastapi import FastAPI, Depends, Query
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

@app.get("/search/", response_model=list[schemas.AddressResponse])
def search_lpu(fulladdress: str = Query(..., description="Имя или часть имени ЛПУ"), db: Session = Depends(get_db)):
    return crud.get_address_by_address(db, fulladdress)

@app.get("/divisions/", response_model=list[schemas.DivisionsOut])
def read_divisions(db:Session = Depends(get_db)):
    return crud.get_divisions(db)

@app.get("/sites/", response_model=list[schemas.SitesOut])
def read_sites(db:Session = Depends(get_db)):
    return crud.get_sites(db)

@app.get("/lpu/", response_model=list[schemas.LpuOut])
def read_lpu(db:Session = Depends(get_db)):
    return crud.get_lpu(db)

@app.get("/address/", response_model=list[schemas.AddressOut])
def read_address(db:Session = Depends(get_db)):
    return crud.get_address(db)
