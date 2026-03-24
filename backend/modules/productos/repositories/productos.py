from typing import List, Optional
from sqlmodel import Session, select
from modules.productos.models.productos import Productos
from modules.productos.schemas.productos import ProductoCreate, ProductoUpdate

class ProductoRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, producto_create: ProductoCreate) -> Productos:
        db_producto = Productos.model_validate(producto_create)
        self.session.add(db_producto)
        self.session.commit()
        self.session.refresh(db_producto)
        return db_producto

    def get_by_id(self, id_producto: int) -> Optional[Productos]:
        return self.session.get(Productos, id_producto)

    def get_all(self, offset: int = 0, limit: int = 100) -> List[Productos]:
        return self.session.exec(select(Productos).offset(offset).limit(limit)).all()

    def update(self, id_producto: int, producto_update: ProductoUpdate) -> Optional[Productos]:
        db_producto = self.get_by_id(id_producto)
        if not db_producto:
            return None
        producto_data = producto_update.model_dump(exclude_unset=True)
        for key, value in producto_data.items():
            setattr(db_producto, key, value)
        self.session.add(db_producto)
        self.session.commit()
        self.session.refresh(db_producto)
        return db_producto

    def delete(self, id_producto: int) -> bool:
        db_producto = self.get_by_id(id_producto)
        if not db_producto:
            return False
        self.session.delete(db_producto)
        self.session.commit()
        return True
