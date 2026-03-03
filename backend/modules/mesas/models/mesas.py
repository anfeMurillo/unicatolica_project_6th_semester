from sqlmodel import Field, SQLModel
from typing import Optional

class Mesas(SQLModel, table=True):
    id_mesa: Optional[int] = Field(
        default=None, 
        primary_key=True
    )
    numero: int = Field(
        nullable=False 
    )
    id_local: Optional[int] = Field(
        default=None,
        foreign_key="locales.id_local" 
    )