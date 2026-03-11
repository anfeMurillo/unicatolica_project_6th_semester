from typing import Optional
from sqlmodel import Field, SQLModel


class Cliente(SQLModel, table=True):
    id_cliente: Optional[int] = Field(
        default=None,
        primary_key=True,
    )
    nombre: str
    correo: str
    clave_hash: str
