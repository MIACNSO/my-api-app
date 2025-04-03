from pydantic import BaseModel
from typing import List, Optional

class LpuOut(BaseModel):
    id: int
    code_lpu: int
    fullname: str
    name: str

    class Config:
        orm_mode = True

class DivisionsOut(BaseModel):
    id: int
    lpu_id: int
    phones: str
    div_address: str
    div_name: str
    # При необходимости можно добавить вложенные объекты, например список сайтов:
    sites: Optional[List['SitesOut']] = None

    class Config:
        orm_mode = True

class SitesOut(BaseModel):
    id: int
    division_id: int
    rp_code: str
    kladr_code: str
    house_range_begin: int
    house_range_end: int
    house: str
    houselit: str
    block: int
    building: str
    house_range_begin_lit: str
    house_range_end_lit: str
    house_range_begin_block: int
    house_range_end_block: int
    house_even: int
    house_numbs: str

    class Config:
        orm_mode = True

# Если используются вложенные схемы, обновите ссылки:
DivisionsOut.update_forward_refs()