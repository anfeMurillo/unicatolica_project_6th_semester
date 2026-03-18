from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class OrdenBase(BaseModel):
    id_cliente: Optional[int] = None
    id_empleado: Optional[int] = None
    id_mesa: Optional[int] = None
    estado: Optional[str] = "pendiente"

class OrdenCreate(OrdenBase):
    pass

class OrdenUpdate(BaseModel):
    id_cliente: Optional[int] = None
    id_empleado: Optional[int] = None
    id_mesa: Optional[int] = None
    estado: Optional[str] = None

class OrdenRead(OrdenBase):
    id_orden: int
    fecha: datetime

    class Config:
        from_attributes = True
