from typing import Optional
from pydantic import BaseModel

class CadenaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    id_propietario: int

class CadenaCreate(CadenaBase):
    pass

class CadenaUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    id_propietario: Optional[int] = None

class CadenaRead(CadenaBase):
    id_cadena: int

    class Config:
        from_attributes = True
