from sqlalchemy.orm import Session
from app import models, schemas

def get_clinics(db:Session):
    return db.query(models.Clinic).all()

def create_clinic(db:Session, clinic:schemas.ClinicCreate):
    db_clinic = models.Clinic(**clinic.dict())
    db.add(db_clinic)
    db.commit()
    db.refresh(db_clinic)
    return db_clinic