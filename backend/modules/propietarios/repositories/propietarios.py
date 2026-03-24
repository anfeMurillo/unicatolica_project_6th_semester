from sqlmodel import Session, select
from typing import List, Optional
from modules.propietarios.models.propietarios import Propietario
from modules.propietarios.schemas.propietarios import PropietarioCreate, PropietarioUpdate

class PropietarioRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, propietario_data: PropietarioCreate) -> Propietario:
        propietario = Propietario(**propietario_data.model_dump())
        self.session.add(propietario)
        self.session.commit()
        self.session.refresh(propietario)
        return propietario

    def get_by_id(self, id_propietario: int) -> Optional[Propietario]:
        return self.session.get(Propietario, id_propietario)

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Propietario]:
        query = select(Propietario).offset(skip).limit(limit)
        return self.session.exec(query).all()

    def update(self, id_propietario: int, propietario_data: PropietarioUpdate) -> Optional[Propietario]:
        propietario = self.get_by_id(id_propietario)
        if not propietario:
            return None
        
        update_data = propietario_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(propietario, key, value)
            
        self.session.add(propietario)
        self.session.commit()
        self.session.refresh(propietario)
        return propietario

    def delete(self, id_propietario: int) -> bool:
        propietario = self.get_by_id(id_propietario)
        if not propietario:
            return False
            
        self.session.delete(propietario)
        self.session.commit()
        return True
