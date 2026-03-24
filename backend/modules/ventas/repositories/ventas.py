from typing import List, Optional
from sqlmodel import Session, select
from modules.ventas.models.ventas import Ventas
from modules.ventas.schemas.ventas import VentaCreate, VentaUpdate

class VentaRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, venta_create: VentaCreate) -> Ventas:
        db_venta = Ventas.model_validate(venta_create)
        self.session.add(db_venta)
        self.session.commit()
        self.session.refresh(db_venta)
        return db_venta

    def get_by_id(self, id_venta: int) -> Optional[Ventas]:
        return self.session.get(Ventas, id_venta)

    def get_all(self, offset: int = 0, limit: int = 100) -> List[Ventas]:
        return self.session.exec(select(Ventas).offset(offset).limit(limit)).all()

    def update(self, id_venta: int, venta_update: VentaUpdate) -> Optional[Ventas]:
        db_venta = self.get_by_id(id_venta)
        if not db_venta:
            return None
        venta_data = venta_update.model_dump(exclude_unset=True)
        for key, value in venta_data.items():
            setattr(db_venta, key, value)
        self.session.add(db_venta)
        self.session.commit()
        self.session.refresh(db_venta)
        return db_venta

    def delete(self, id_venta: int) -> bool:
        db_venta = self.get_by_id(id_venta)
        if not db_venta:
            return False
        self.session.delete(db_venta)
        self.session.commit()
        return True
