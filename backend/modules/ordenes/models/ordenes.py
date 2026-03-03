from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime

class Ordenes(SQLModel, table=True):
    id_orden: Optional[int] = Field(
        default=None, 
        primary_key=True
    )
    fecha: datetime = Field(
        default_factory=datetime.utcnow
    )
    id_cliente: Optional[int] = Field(
        default=None,
        foreign_key="clientes.id_cliente" 
    )
    id_empleado: Optional[int] = Field(
        default=None,
        foreign_key="trabajadores.id_trabajador"
    )
    id_mesa: Optional[int] = Field(
        default=None,
        foreign_key="mesas.id_mesa"
    )
    estado: str = Field(
        default="pendiente", 
        max_length=50
    )