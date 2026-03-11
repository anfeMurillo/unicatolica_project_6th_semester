from typing import Optional
from pydantic import BaseModel, EmailStr

class ClienteBase(BaseModel):
    nombre: str
    correo: EmailStr

class ClienteCreate(ClienteBase):
    clave_hash: str

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    clave_hash: Optional[str] = None

class ClienteRead(ClienteBase):
    id_cliente: int

    class Config:
        from_attributes = True
