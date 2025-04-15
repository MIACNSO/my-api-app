from pydantic import BaseModel
from typing import List, Optional

class LpuOut(BaseModel):
    lpu_id: Optional[int] = None
    fullname: Optional[str] = None
    shortname: Optional[str] = None
    code: Optional[int] = None

    class Config:
        orm_mode = True

class DivisionsOut(BaseModel):
    div_id: Optional[str] = None
    lpu_id: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    sites: Optional[List['SitesOut']] = None

    class Config:
        orm_mode = True

class SitesOut(BaseModel):
    site_id: Optional[int] = None
    division_id: Optional[int] = None
    kladr: Optional[str] = None
    regpurpose: Optional[int] = None
    house_range_begin: Optional[str] = None
    house_range_end: Optional[str] = None
    house: Optional[str] = None
    house_lit: Optional[str] = None
    block: Optional[str] = None
    building: Optional[str] = None
    house_range_begin_lit: Optional[str] = None
    house_range_end_lit: Optional[str] = None
    house_range_begin_block: Optional[str] = None
    house_range_end_block: Optional[str] = None
    house_even: Optional[str] = None
    house_numbs: Optional[str] = None

    class Config:
        orm_mode = True


class AddressOut(BaseModel):
    aoid: Optional[str] = None
    aoguid: Optional[str] = None
    aolevel: Optional[int] = None
    offname: Optional[str] = None
    parentguid: Optional[str] = None
    shortname: Optional[str] = None
    plaincode: Optional[str] = None
    fulladdress: Optional[str] = None
    parentscount: Optional[int] = None

    class Config:
        orm_mode = True

# Если используются вложенные схемы, обновите ссылки:
DivisionsOut.update_forward_refs()