from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime


class Ventas(SQLModel, table=True):
    id_venta: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    id_cliente: Optional[int] = Field(
        default=None,
        foreign_key="clientes.id_cliente"
    )

    id_orden: Optional[int] = Field(
        default=None,
        foreign_key="ordenes.id_orden"
    )

    fecha: datetime = Field(
        default_factory=datetime.utcnow
    )

    valor: float = Field(
        nullable=False
    )