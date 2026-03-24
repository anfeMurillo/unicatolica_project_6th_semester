from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from modules.shared.database import get_session
from modules.ventas.repositories.ventas import VentaRepository
from modules.ventas.schemas.ventas import VentaCreate, VentaUpdate, VentaRead

router = APIRouter(prefix="/ventas", tags=["ventas"])

def get_repository(session: Session = Depends(get_session)) -> VentaRepository:
    return VentaRepository(session)

@router.post("/", response_model=VentaRead)
def create_venta(
    venta: VentaCreate, 
    repository: VentaRepository = Depends(get_repository)
):
    return repository.create(venta)

@router.get("/", response_model=List[VentaRead])
def read_ventas(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    repository: VentaRepository = Depends(get_repository)
):
    return repository.get_all(offset=offset, limit=limit)

@router.get("/{id_venta}", response_model=VentaRead)
def read_venta_by_id(
    id_venta: int, 
    repository: VentaRepository = Depends(get_repository)
):
    db_venta = repository.get_by_id(id_venta)
    if not db_venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return db_venta

@router.patch("/{id_venta}", response_model=VentaRead)
def update_venta(
    id_venta: int, 
    venta: VentaUpdate, 
    repository: VentaRepository = Depends(get_repository)
):
    db_venta = repository.update(id_venta, venta)
    if not db_venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return db_venta

@router.delete("/{id_venta}")
def delete_venta(
    id_venta: int, 
    repository: VentaRepository = Depends(get_repository)
):
    success = repository.delete(id_venta)
    if not success:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return {"ok": True}
