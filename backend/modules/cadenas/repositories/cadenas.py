from sqlmodel import Session, select
from typing import List, Optional
from modules.cadenas.models.cadenas import Cadena
from modules.cadenas.schemas.cadenas import CadenaCreate, CadenaUpdate

class CadenaRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, cadena_data: CadenaCreate) -> Cadena:
        cadena = Cadena(**cadena_data.model_dump())
        self.session.add(cadena)
        self.session.commit()
        self.session.refresh(cadena)
        return cadena

    def get_by_id(self, id_cadena: int) -> Optional[Cadena]:
        return self.session.get(Cadena, id_cadena)

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Cadena]:
        query = select(Cadena).offset(skip).limit(limit)
        return self.session.exec(query).all()

    def update(self, id_cadena: int, cadena_data: CadenaUpdate) -> Optional[Cadena]:
        cadena = self.get_by_id(id_cadena)
        if not cadena:
            return None
        
        update_data = cadena_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(cadena, key, value)
            
        self.session.add(cadena)
        self.session.commit()
        self.session.refresh(cadena)
        return cadena

    def delete(self, id_cadena: int) -> bool:
        cadena = self.get_by_id(id_cadena)
        if not cadena:
            return False
            
        self.session.delete(cadena)
        self.session.commit()
        return True
