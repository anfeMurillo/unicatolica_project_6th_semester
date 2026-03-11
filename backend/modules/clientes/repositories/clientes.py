from typing import List, Optional
from sqlmodel import Session, select
from modules.clientes.models.clientes import Cliente
from modules.clientes.schemas.clientes import ClienteCreate, ClienteUpdate

class ClienteRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, cliente_create: ClienteCreate) -> Cliente:
        db_cliente = Cliente.model_validate(cliente_create)
        self.session.add(db_cliente)
        self.session.commit()
        self.session.refresh(db_cliente)
        return db_cliente

    def get_by_id(self, id_cliente: int) -> Optional[Cliente]:
        return self.session.get(Cliente, id_cliente)

    def get_all(self, offset: int = 0, limit: int = 100) -> List[Cliente]:
        return self.session.exec(select(Cliente).offset(offset).limit(limit)).all()

    def update(self, id_cliente: int, cliente_update: ClienteUpdate) -> Optional[Cliente]:
        db_cliente = self.get_by_id(id_cliente)
        if not db_cliente:
            return None
        cliente_data = cliente_update.model_dump(exclude_unset=True)
        for key, value in cliente_data.items():
            setattr(db_cliente, key, value)
        self.session.add(db_cliente)
        self.session.commit()
        self.session.refresh(db_cliente)
        return db_cliente

    def delete(self, id_cliente: int) -> bool:
        db_cliente = self.get_by_id(id_cliente)
        if not db_cliente:
            return False
        self.session.delete(db_cliente)
        self.session.commit()
        return True
