from typing import List, Optional

from sqlalchemy import Boolean, CheckConstraint, Column, Date, DateTime, ForeignKeyConstraint, Index, Integer, PrimaryKeyConstraint, SmallInteger, String, Table, Text, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime

from app.database import Base


class Address(Base):
    __tablename__ = 'address'
    __table_args__ = (
        PrimaryKeyConstraint('aoid', name='address_pkey'),
        Index('address_aoid_c6d83c93_like', 'aoid'),
        {'schema': 'public'}
    )

    aoid: Mapped[str] = mapped_column(String(36), primary_key=True)
    aoguid: Mapped[Optional[str]] = mapped_column(String(36))
    aolevel: Mapped[Optional[int]] = mapped_column(Integer)
    offname: Mapped[Optional[str]] = mapped_column(String(120))
    parentguid: Mapped[Optional[str]] = mapped_column(String(36))
    shortname: Mapped[Optional[str]] = mapped_column(String(36))
    plaincode: Mapped[Optional[str]] = mapped_column(String(20))
    fulladdress: Mapped[Optional[str]] = mapped_column(String(500))
    parentscount: Mapped[Optional[int]] = mapped_column(Integer)


class Divisions(Base):
    __tablename__ = 'divisions'
    __table_args__ = (
        PrimaryKeyConstraint('div_id', name='divisions_pkey'),
        Index('divisions_div_id_fb3b4d1f_like', 'div_id'),
        {'schema': 'public'}
    )

    div_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    lpu_id: Mapped[Optional[str]] = mapped_column(String(36))
    phone: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    address: Mapped[Optional[str]] = mapped_column(String(255))
    name: Mapped[Optional[str]] = mapped_column(String(255))


class House(Base):
    __tablename__ = 'house'
    __table_args__ = (
        PrimaryKeyConstraint('houseid', name='house_pkey'),
        Index('house_houseid_3136636d_like', 'houseid'),
        {'schema': 'public'}
    )

    houseid: Mapped[str] = mapped_column(String(36), primary_key=True)
    aoguid: Mapped[Optional[str]] = mapped_column(String(36))
    houseguid: Mapped[Optional[str]] = mapped_column(String(36))
    eststatus: Mapped[Optional[int]] = mapped_column(Integer)
    housenum: Mapped[Optional[str]] = mapped_column(String(15))


class Site(Base):
    __tablename__ = 'site'
    __table_args__ = (
        PrimaryKeyConstraint('site_id', name='site_pkey'),
        Index('site_site_id_dd3a7ed2_like', 'site_id'),
        {'schema': 'public'}
    )

    site_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    division_id: Mapped[str] = mapped_column(String(20))
    kladr: Mapped[Optional[str]] = mapped_column(String(36))
    regpurpose: Mapped[Optional[int]] = mapped_column(Integer)
    house_range_begin: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    house_range_end: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    house: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    house_lit: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    block: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    building: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    house_range_begin_lit: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    house_range_end_lit: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    house_range_begin_block: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    house_range_end_block: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    house_even: Mapped[Optional[str]] = mapped_column(String(36))
    house_numbs: Mapped[Optional[str]] = mapped_column(String(10000))


class SplitHouse(Base):
    __tablename__ = 'split_house'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='split_house_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    division_id: Mapped[str] = mapped_column(String(20))
    kladr: Mapped[Optional[str]] = mapped_column(String(36))
    regpurpose: Mapped[Optional[int]] = mapped_column(Integer)
    house_numbs: Mapped[Optional[str]] = mapped_column(String(100))


class Lpu(Base):
    __tablename__ = 'lpu'
    __table_args__ = (
        PrimaryKeyConstraint('lpu_id', name='lpu_pkey'),
        Index('lpu_lpu_id_6bf922c2_like', 'lpu_id'),
        {'schema': 'public'}
    )

    lpu_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(255))
    shortname: Mapped[Optional[str]] = mapped_column(String(255))
    code: Mapped[Optional[str]] = mapped_column(String(20))


class Regpurpose(Base):
    __tablename__ = 'regpurpose'
    __table_args__ = (
        PrimaryKeyConstraint('code', name='regpurpose_pkey'),
        {'schema': 'public'}
    )

    code: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))


t_mainsite = Table(
    'mainsite', Base.metadata,
    Column('data_end', Date),
    Column('data_end_miac', String),
    Column('srok_in_mznso', String),
    Column('name', String),
    Column('otdel', String),
    Column('otdel_miac', String),
    Column('address', String),
    Column('mo', String),
    schema='public'
)

