from typing import Optional
from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None

class ProductoRead(ProductoBase):
    id_producto: int

    class Config:
        from_attributes = True