from typing import List, Optional
from sqlmodel import Session, select
from modules.ordenes.models.ordenes import Ordenes
from modules.ordenes.schemas.ordenes import OrdenCreate, OrdenUpdate

class OrdenRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, orden_create: OrdenCreate) -> Ordenes:
        db_orden = Ordenes.model_validate(orden_create)
        self.session.add(db_orden)
        self.session.commit()
        self.session.refresh(db_orden)
        return db_orden

    def get_by_id(self, id_orden: int) -> Optional[Ordenes]:
        return self.session.get(Ordenes, id_orden)

    def get_all(self, offset: int = 0, limit: int = 100) -> List[Ordenes]:
        return self.session.exec(select(Ordenes).offset(offset).limit(limit)).all()

    def update(self, id_orden: int, orden_update: OrdenUpdate) -> Optional[Ordenes]:
        db_orden = self.get_by_id(id_orden)
        if not db_orden:
            return None
        orden_data = orden_update.model_dump(exclude_unset=True)
        for key, value in orden_data.items():
            setattr(db_orden, key, value)
        self.session.add(db_orden)
        self.session.commit()
        self.session.refresh(db_orden)
        return db_orden

    def delete(self, id_orden: int) -> bool:
        db_orden = self.get_by_id(id_orden)
        if not db_orden:
            return False
        self.session.delete(db_orden)
        self.session.commit()
        return True
