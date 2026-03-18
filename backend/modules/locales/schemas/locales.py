from typing import Optional
from pydantic import BaseModel

class LocalBase(BaseModel):
    nombre: str
    direccion: str

class LocalCreate(LocalBase):
    pass

class LocalUpdate(BaseModel):
    nombre: Optional[str] = None
    direccion: Optional[str] = None

class LocalRead(LocalBase):
    id_local: int

    class Config:
        from_attributes = True
