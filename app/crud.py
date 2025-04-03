from sqlalchemy.orm import Session
from app import models, schemas

def get_lpu(db:Session):
    return db.query(models.Lpu).all()

def get_divisions(db:Session):
    return db.query(models.Divisions).all()

def get_sites(db:Session):
    return db.query(models.Site).all()

# def create_clinic(db:Session, clinic:schemas.ClinicCreate):
#     db_clinic = models.Clinic(**clinic.dict())
#     db.add(db_clinic)
#     db.commit()
#     db.refresh(db_clinic)
#     return db_clinic