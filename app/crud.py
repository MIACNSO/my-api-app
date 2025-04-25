from sqlalchemy.orm import Session
from app import models, schemas

def get_lpu(db:Session):
    return db.query(models.Lpu).all()

def get_divisions(db:Session):
    return db.query(models.Divisions).all()

def get_sites(db:Session):
    return db.query(models.Site).all()

def get_address_by_address(db:Session, fulladdress: str):
    return db.query(models.Address).filter(models.Address.fulladdress.ilike(f"%{fulladdress}%")).all()

