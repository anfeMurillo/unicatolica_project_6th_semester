from typing import Optional
from pydantic import BaseModel, EmailStr

class PropietarioBase(BaseModel):
    nombre: str
    correo: EmailStr

class PropietarioCreate(PropietarioBase):
    clave_hash: str

class PropietarioUpdate(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    clave_hash: Optional[str] = None

class PropietarioRead(PropietarioBase):
    id_propietario: int

    class Config:
        from_attributes = True
