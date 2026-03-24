from typing import List, Optional
from sqlmodel import Session, select
from modules.trabajadores.models.trabajadores import Trabajadores
from modules.trabajadores.schemas.trabajadores import TrabajadorCreate, TrabajadorUpdate

class TrabajadorRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, trabajador_create: TrabajadorCreate) -> Trabajadores:
        db_trabajador = Trabajadores.model_validate(trabajador_create)
        self.session.add(db_trabajador)
        self.session.commit()
        self.session.refresh(db_trabajador)
        return db_trabajador

    def get_by_id(self, id_trabajador: int) -> Optional[Trabajadores]:
        return self.session.get(Trabajadores, id_trabajador)

    def get_all(self, offset: int = 0, limit: int = 100) -> List[Trabajadores]:
        return self.session.exec(select(Trabajadores).offset(offset).limit(limit)).all()

    def update(self, id_trabajador: int, trabajador_update: TrabajadorUpdate) -> Optional[Trabajadores]:
        db_trabajador = self.get_by_id(id_trabajador)
        if not db_trabajador:
            return None
        trabajador_data = trabajador_update.model_dump(exclude_unset=True)
        for key, value in trabajador_data.items():
            setattr(db_trabajador, key, value)
        self.session.add(db_trabajador)
        self.session.commit()
        self.session.refresh(db_trabajador)
        return db_trabajador

    def delete(self, id_trabajador: int) -> bool:
        db_trabajador = self.get_by_id(id_trabajador)
        if not db_trabajador:
            return False
        self.session.delete(db_trabajador)
        self.session.commit()
        return True
