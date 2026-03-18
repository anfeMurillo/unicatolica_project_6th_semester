from typing import Optional
from pydantic import BaseModel, EmailStr

class TrabajadorBase(BaseModel):
    id_local: Optional[int] = None
    nombre: str
    apellido: str
    cargo: str
    correo: EmailStr

class TrabajadorCreate(TrabajadorBase):
    clave_hash: str

class TrabajadorUpdate(BaseModel):
    id_local: Optional[int] = None
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    cargo: Optional[str] = None
    correo: Optional[EmailStr] = None
    clave_hash: Optional[str] = None

class TrabajadorRead(TrabajadorBase):
    id_trabajador: int

    class Config:
        from_attributes = True