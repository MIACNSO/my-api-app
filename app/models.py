from sqlalchemy import Column, Integer, String, Index, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Lpu(Base):
    __tablename__ = "lpu"
    id = Column(Integer, primary_key=True, index=True)
    code_lpu = Column(Integer, index=True)
    fullname = Column(String, index=True)
    name = Column(String, index=True)

    divisions = relationship("Divisions", back_populates="lpu")


class Divisions(Base):
    __tablename__ = "divisions"

    id = Column(Integer, primary_key=True, index=True)
    lpu_id = Column(Integer, ForeignKey("lpu.id"), index=True)
    phones = Column(String, index=True)
    div_address = Column(String, index=True)
    div_name = Column(String, index=True)

    lpu = relationship("Lpu", back_populates="divisions")
    sites = relationship("Site", back_populates="division")


class Site(Base):
    __tablename__ = "site"

    id = Column(Integer, primary_key=True, index=True)
    division_id = Column(Integer, ForeignKey("divisions.id"), index=True)
    rp_code = Column(String, index=True)
    kladr_code = Column(String, index=True)
    house_range_begin = Column(Integer, index=True)
    house_range_end = Column(Integer, index=True)
    house = Column(String, index=True)
    houselit = Column(String, index=True)
    block = Column(Integer, index=True)
    building = Column(String, index=True)
    house_range_begin_lit = Column(String, index=True)
    house_range_end_lit = Column(String, index=True)
    house_range_begin_block = Column(Integer, index=True)
    house_range_end_block = Column(Integer, index=True)
    house_even = Column(Integer, index=True)
    house_numbs = Column(String, index=True)

    division = relationship("Divisions", back_populates="sites")