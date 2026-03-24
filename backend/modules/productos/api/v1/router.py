from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from modules.shared.database import get_session
from modules.productos.repositories.productos import ProductoRepository
from modules.productos.schemas.productos import ProductoCreate, ProductoUpdate, ProductoRead

router = APIRouter(prefix="/productos", tags=["productos"])

def get_repository(session: Session = Depends(get_session)) -> ProductoRepository:
    return ProductoRepository(session)

@router.post("/", response_model=ProductoRead)
def create_producto(
    producto: ProductoCreate, 
    repository: ProductoRepository = Depends(get_repository)
):
    return repository.create(producto)

@router.get("/", response_model=List[ProductoRead])
def read_productos(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    repository: ProductoRepository = Depends(get_repository)
):
    return repository.get_all(offset=offset, limit=limit)

@router.get("/{id_producto}", response_model=ProductoRead)
def read_producto_by_id(
    id_producto: int, 
    repository: ProductoRepository = Depends(get_repository)
):
    db_producto = repository.get_by_id(id_producto)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@router.patch("/{id_producto}", response_model=ProductoRead)
def update_producto(
    id_producto: int, 
    producto: ProductoUpdate, 
    repository: ProductoRepository = Depends(get_repository)
):
    db_producto = repository.update(id_producto, producto)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@router.delete("/{id_producto}")
def delete_producto(
    id_producto: int, 
    repository: ProductoRepository = Depends(get_repository)
):
    success = repository.delete(id_producto)
    if not success:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"ok": True}
