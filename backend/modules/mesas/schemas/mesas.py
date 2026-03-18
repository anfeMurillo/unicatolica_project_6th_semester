from typing import Optional
from pydantic import BaseModel

class MesaBase(BaseModel):
    numero: int
    id_local: int

class MesaCreate(MesaBase):
    pass

class MesaUpdate(BaseModel):
    numero: Optional[int] = None
    id_local: Optional[int] = None

class MesaRead(MesaBase):
    id_mesa: int

    class Config:
        from_attributes = True
