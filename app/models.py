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


# class AuthGroup(Base):
#     __tablename__ = 'auth_group'
#     __table_args__ = (
#         PrimaryKeyConstraint('id', name='auth_group_pkey'),
#         UniqueConstraint('name', name='auth_group_name_key'),
#         Index('auth_group_name_a6ea08ec_like', 'name'),
#         {'schema': 'public'}
#     )
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String(150))
#
#     auth_user_groups: Mapped[List['AuthUserGroups']] = relationship('AuthUserGroups', back_populates='group')
#     auth_group_permissions: Mapped[List['AuthGroupPermissions']] = relationship('AuthGroupPermissions', back_populates='group')


# class AuthUser(Base):
#     __tablename__ = 'auth_user'
#     __table_args__ = (
#         PrimaryKeyConstraint('id', name='auth_user_pkey'),
#         UniqueConstraint('username', name='auth_user_username_key'),
#         Index('auth_user_username_6821ab7c_like', 'username'),
#         {'schema': 'public'}
#     )
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     password: Mapped[str] = mapped_column(String(128))
#     is_superuser: Mapped[bool] = mapped_column(Boolean)
#     username: Mapped[str] = mapped_column(String(150))
#     first_name: Mapped[str] = mapped_column(String(150))
#     last_name: Mapped[str] = mapped_column(String(150))
#     email: Mapped[str] = mapped_column(String(254))
#     is_staff: Mapped[bool] = mapped_column(Boolean)
#     is_active: Mapped[bool] = mapped_column(Boolean)
#     date_joined: Mapped[datetime.datetime] = mapped_column(DateTime(True))
#     last_login: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
#
#     auth_user_groups: Mapped[List['AuthUserGroups']] = relationship('AuthUserGroups', back_populates='user')
#     django_admin_log: Mapped[List['DjangoAdminLog']] = relationship('DjangoAdminLog', back_populates='user')
#     auth_user_user_permissions: Mapped[List['AuthUserUserPermissions']] = relationship('AuthUserUserPermissions', back_populates='user')


# class DjangoContentType(Base):
#     __tablename__ = 'django_content_type'
#     __table_args__ = (
#         PrimaryKeyConstraint('id', name='django_content_type_pkey'),
#         UniqueConstraint('app_label', 'model', name='django_content_type_app_label_model_76bd3d3b_uniq'),
#         {'schema': 'public'}
#     )
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     app_label: Mapped[str] = mapped_column(String(100))
#     model: Mapped[str] = mapped_column(String(100))
#
#     auth_permission: Mapped[List['AuthPermission']] = relationship('AuthPermission', back_populates='content_type')
#     django_admin_log: Mapped[List['DjangoAdminLog']] = relationship('DjangoAdminLog', back_populates='content_type')


# class DjangoMigrations(Base):
#     __tablename__ = 'django_migrations'
#     __table_args__ = (
#         PrimaryKeyConstraint('id', name='django_migrations_pkey'),
#         {'schema': 'public'}
#     )
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     app: Mapped[str] = mapped_column(String(255))
#     name: Mapped[str] = mapped_column(String(255))
#     applied: Mapped[datetime.datetime] = mapped_column(DateTime(True))


# class DjangoSession(Base):
#     __tablename__ = 'django_session'
#     __table_args__ = (
#         PrimaryKeyConstraint('session_key', name='django_session_pkey'),
#         Index('django_session_expire_date_a5c62663', 'expire_date'),
#         Index('django_session_session_key_c0390e0f_like', 'session_key'),
#         {'schema': 'public'}
#     )
#
#     session_key: Mapped[str] = mapped_column(String(40), primary_key=True)
#     session_data: Mapped[str] = mapped_column(Text)
#     expire_date: Mapped[datetime.datetime] = mapped_column(DateTime(True))


# class Regpurpose(Base):
#     __tablename__ = 'regpurpose'
#     __table_args__ = (
#         PrimaryKeyConstraint('code', name='regpurpose_pkey'),
#         {'schema': 'public'}
#     )
#
#     code: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String(50))


# class AuthPermission(Base):
#     __tablename__ = 'auth_permission'
#     __table_args__ = (
#         ForeignKeyConstraint(['content_type_id'], ['public.django_content_type.id'], deferrable=True, initially='DEFERRED', name='auth_permission_content_type_id_2f476e4b_fk_django_co'),
#         PrimaryKeyConstraint('id', name='auth_permission_pkey'),
#         UniqueConstraint('content_type_id', 'codename', name='auth_permission_content_type_id_codename_01ab375a_uniq'),
#         Index('auth_permission_content_type_id_2f476e4b', 'content_type_id'),
#         {'schema': 'public'}
#     )
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String(255))
#     content_type_id: Mapped[int] = mapped_column(Integer)
#     codename: Mapped[str] = mapped_column(String(100))
#
#     content_type: Mapped['DjangoContentType'] = relationship('DjangoContentType', back_populates='auth_permission')
#     auth_group_permissions: Mapped[List['AuthGroupPermissions']] = relationship('AuthGroupPermissions', back_populates='permission')
#     auth_user_user_permissions: Mapped[List['AuthUserUserPermissions']] = relationship('AuthUserUserPermissions', back_populates='permission')


# class AuthUserGroups(Base):
#     __tablename__ = 'auth_user_groups'
#     __table_args__ = (
#         ForeignKeyConstraint(['group_id'], ['public.auth_group.id'], deferrable=True, initially='DEFERRED', name='auth_user_groups_group_id_97559544_fk_auth_group_id'),
#         ForeignKeyConstraint(['user_id'], ['public.auth_user.id'], deferrable=True, initially='DEFERRED', name='auth_user_groups_user_id_6a12ed8b_fk_auth_user_id'),
#         PrimaryKeyConstraint('id', name='auth_user_groups_pkey'),
#         UniqueConstraint('user_id', 'group_id', name='auth_user_groups_user_id_group_id_94350c0c_uniq'),
#         Index('auth_user_groups_group_id_97559544', 'group_id'),
#         Index('auth_user_groups_user_id_6a12ed8b', 'user_id'),
#         {'schema': 'public'}
#     )
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     user_id: Mapped[int] = mapped_column(Integer)
#     group_id: Mapped[int] = mapped_column(Integer)
#
#     group: Mapped['AuthGroup'] = relationship('AuthGroup', back_populates='auth_user_groups')
#     user: Mapped['AuthUser'] = relationship('AuthUser', back_populates='auth_user_groups')


# class DjangoAdminLog(Base):
#     __tablename__ = 'django_admin_log'
#     __table_args__ = (
#         CheckConstraint('action_flag >= 0', name='django_admin_log_action_flag_check'),
#         ForeignKeyConstraint(['content_type_id'], ['public.django_content_type.id'], deferrable=True, initially='DEFERRED', name='django_admin_log_content_type_id_c4bce8eb_fk_django_co'),
#         ForeignKeyConstraint(['user_id'], ['public.auth_user.id'], deferrable=True, initially='DEFERRED', name='django_admin_log_user_id_c564eba6_fk_auth_user_id'),
#         PrimaryKeyConstraint('id', name='django_admin_log_pkey'),
#         Index('django_admin_log_content_type_id_c4bce8eb', 'content_type_id'),
#         Index('django_admin_log_user_id_c564eba6', 'user_id'),
#         {'schema': 'public'}
#     )
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     action_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
#     object_repr: Mapped[str] = mapped_column(String(200))
#     action_flag: Mapped[int] = mapped_column(SmallInteger)
#     change_message: Mapped[str] = mapped_column(Text)
#     user_id: Mapped[int] = mapped_column(Integer)
#     object_id: Mapped[Optional[str]] = mapped_column(Text)
#     content_type_id: Mapped[Optional[int]] = mapped_column(Integer)
#
#     content_type: Mapped[Optional['DjangoContentType']] = relationship('DjangoContentType', back_populates='django_admin_log')
#     user: Mapped['AuthUser'] = relationship('AuthUser', back_populates='django_admin_log')


# class AuthGroupPermissions(Base):
#     __tablename__ = 'auth_group_permissions'
#     __table_args__ = (
#         ForeignKeyConstraint(['group_id'], ['public.auth_group.id'], deferrable=True, initially='DEFERRED', name='auth_group_permissions_group_id_b120cbf9_fk_auth_group_id'),
#         ForeignKeyConstraint(['permission_id'], ['public.auth_permission.id'], deferrable=True, initially='DEFERRED', name='auth_group_permissio_permission_id_84c5c92e_fk_auth_perm'),
#         PrimaryKeyConstraint('id', name='auth_group_permissions_pkey'),
#         UniqueConstraint('group_id', 'permission_id', name='auth_group_permissions_group_id_permission_id_0cd325b0_uniq'),
#         Index('auth_group_permissions_group_id_b120cbf9', 'group_id'),
#         Index('auth_group_permissions_permission_id_84c5c92e', 'permission_id'),
#         {'schema': 'public'}
#     )
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     group_id: Mapped[int] = mapped_column(Integer)
#     permission_id: Mapped[int] = mapped_column(Integer)
#
#     group: Mapped['AuthGroup'] = relationship('AuthGroup', back_populates='auth_group_permissions')
#     permission: Mapped['AuthPermission'] = relationship('AuthPermission', back_populates='auth_group_permissions')


# class AuthUserUserPermissions(Base):
#     __tablename__ = 'auth_user_user_permissions'
#     __table_args__ = (
#         ForeignKeyConstraint(['permission_id'], ['public.auth_permission.id'], deferrable=True, initially='DEFERRED', name='auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm'),
#         ForeignKeyConstraint(['user_id'], ['public.auth_user.id'], deferrable=True, initially='DEFERRED', name='auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id'),
#         PrimaryKeyConstraint('id', name='auth_user_user_permissions_pkey'),
#         UniqueConstraint('user_id', 'permission_id', name='auth_user_user_permissions_user_id_permission_id_14a6b632_uniq'),
#         Index('auth_user_user_permissions_permission_id_1fbb5f2c', 'permission_id'),
#         Index('auth_user_user_permissions_user_id_a95ead1b', 'user_id'),
#         {'schema': 'public'}
#     )
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     user_id: Mapped[int] = mapped_column(Integer)
#     permission_id: Mapped[int] = mapped_column(Integer)
#
#     permission: Mapped['AuthPermission'] = relationship('AuthPermission', back_populates='auth_user_user_permissions')
#     user: Mapped['AuthUser'] = relationship('AuthUser', back_populates='auth_user_user_permissions')
