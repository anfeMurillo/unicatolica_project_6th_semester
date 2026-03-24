from typing import Optional
from sqlmodel import Field, SQLModel

class Propietario(SQLModel, table=True):
    __tablename__ = "usuarios_propietarios"
    id_propietario: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    nombre: str = Field(max_length=100, nullable=False)
    correo: str = Field(max_length=100, nullable=False)
    clave_hash: str = Field(max_length=100, nullable=False)
