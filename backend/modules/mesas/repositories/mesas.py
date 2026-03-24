from typing import List, Optional
from sqlmodel import Session, select
from modules.mesas.models.mesas import Mesas
from modules.mesas.schemas.mesas import MesaCreate, MesaUpdate

class MesaRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, mesa_create: MesaCreate) -> Mesas:
        db_mesa = Mesas.model_validate(mesa_create)
        self.session.add(db_mesa)
        self.session.commit()
        self.session.refresh(db_mesa)
        return db_mesa

    def get_by_id(self, id_mesa: int) -> Optional[Mesas]:
        return self.session.get(Mesas, id_mesa)

    def get_all(self, offset: int = 0, limit: int = 100) -> List[Mesas]:
        return self.session.exec(select(Mesas).offset(offset).limit(limit)).all()

    def update(self, id_mesa: int, mesa_update: MesaUpdate) -> Optional[Mesas]:
        db_mesa = self.get_by_id(id_mesa)
        if not db_mesa:
            return None
        mesa_data = mesa_update.model_dump(exclude_unset=True)
        for key, value in mesa_data.items():
            setattr(db_mesa, key, value)
        self.session.add(db_mesa)
        self.session.commit()
        self.session.refresh(db_mesa)
        return db_mesa

    def delete(self, id_mesa: int) -> bool:
        db_mesa = self.get_by_id(id_mesa)
        if not db_mesa:
            return False
        self.session.delete(db_mesa)
        self.session.commit()
        return True
