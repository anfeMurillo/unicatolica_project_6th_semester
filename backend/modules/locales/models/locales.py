from sqlmodel import Field, SQLModel
from typing import Optional

class Local(SQLModel, table=True):
    id_local: Optional[int] = Field(
        default=None, 
        primary_key=True
    )
    id_cadena: int = Field(foreign_key="cadenas.id_cadena")
    nombre: str = Field(max_length=100, nullable=False)
    direccion: str = Field(max_length=100, nullable=False)