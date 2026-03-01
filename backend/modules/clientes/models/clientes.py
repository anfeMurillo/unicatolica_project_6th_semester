from sqlmodel import Field, SQLModel


class Cliente(SQLModel, table=True):
    id_cliente: int = Field(
        primary_key=True,
    )
    nombre: str
    correo: str
    clave_hash: str
