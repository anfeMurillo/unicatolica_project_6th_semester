from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class VentaBase(BaseModel):
    id_cliente: Optional[int] = None
    id_orden: Optional[int] = None
    valor: float

class VentaCreate(VentaBase):
    pass

class VentaUpdate(BaseModel):
    id_cliente: Optional[int] = None
    id_orden: Optional[int] = None
    valor: Optional[float] = None

class VentaRead(VentaBase):
    id_venta: int
    fecha: datetime

    class Config:
        from_attributes = True