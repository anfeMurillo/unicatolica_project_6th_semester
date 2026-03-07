from sqlmodel import Field, SQLModel
from typing import Optional


class Trabajadores(SQLModel, table=True):
    id_trabajador: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    id_local: Optional[int] = Field(
        default=None,
        foreign_key="locales.id_local"
    )

    nombre: str = Field(
        max_length=100,
        nullable=False
    )

    apellido: str = Field(
        max_length=100
    )

    cargo: str = Field(
        max_length=50
    )

    correo: str = Field(
        max_length=100
    )

    clave_hash: str = Field(
        max_length=100
    )