from typing import List, Optional
from sqlmodel import Session, select
from modules.locales.models.locales import Local
from modules.locales.schemas.locales import LocalCreate, LocalUpdate

class LocalRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, local_create: LocalCreate) -> Local:
        db_local = Local.model_validate(local_create)
        self.session.add(db_local)
        self.session.commit()
        self.session.refresh(db_local)
        return db_local

    def get_by_id(self, id_local: int) -> Optional[Local]:
        return self.session.get(Local, id_local)

    def get_all(self, offset: int = 0, limit: int = 100) -> List[Local]:
        return self.session.exec(select(Local).offset(offset).limit(limit)).all()

    def update(self, id_local: int, local_update: LocalUpdate) -> Optional[Local]:
        db_local = self.get_by_id(id_local)
        if not db_local:
            return None
        local_data = local_update.model_dump(exclude_unset=True)
        for key, value in local_data.items():
            setattr(db_local, key, value)
        self.session.add(db_local)
        self.session.commit()
        self.session.refresh(db_local)
        return db_local

    def delete(self, id_local: int) -> bool:
        db_local = self.get_by_id(id_local)
        if not db_local:
            return False
        self.session.delete(db_local)
        self.session.commit()
        return True
