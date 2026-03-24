from typing import Optional
from sqlmodel import Field, SQLModel

class Cadena(SQLModel, table=True):
    __tablename__ = "cadenas"
    id_cadena: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    id_propietario: int = Field(foreign_key="usuarios_propietarios.id_propietario")
    nombre: str = Field(max_length=100, nullable=False)
    descripcion: Optional[str] = None
