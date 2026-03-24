from sqlmodel import Field, SQLModel
from typing import Optional


class Productos(SQLModel, table=True):
    id_producto: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    id_cadena: int = Field(foreign_key="cadenas.id_cadena")

    nombre: str = Field(
        max_length=100,
        nullable=False
    )

    descripcion: str

    precio: float = Field(
        nullable=False
    )