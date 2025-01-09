from typing import Optional

from pydantic import BaseModel

class Car(BaseModel):
    ten_xe: str
    nam_san_xuat: int
    tinh_trang: str
    so_km_da_di: int
    xuat_xu: str
    kieu_dang: str
    hop_so: str
    dong_co: str
    mau_ngoai_that: str
    mau_noi_that: str
    so_cua: int
    so_cho_ngoi: int
    dan_dong: str