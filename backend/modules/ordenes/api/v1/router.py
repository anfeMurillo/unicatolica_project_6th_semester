from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from modules.shared.database import get_session
from modules.ordenes.repositories.ordenes import OrdenRepository
from modules.ordenes.schemas.ordenes import OrdenCreate, OrdenUpdate, OrdenRead

router = APIRouter(prefix="/ordenes", tags=["ordenes"])

def get_repository(session: Session = Depends(get_session)) -> OrdenRepository:
    return OrdenRepository(session)

@router.post("/", response_model=OrdenRead)
def create_orden(
    orden: OrdenCreate, 
    repository: OrdenRepository = Depends(get_repository)
):
    return repository.create(orden)

@router.get("/", response_model=List[OrdenRead])
def read_ordenes(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    repository: OrdenRepository = Depends(get_repository)
):
    return repository.get_all(offset=offset, limit=limit)

@router.get("/{id_orden}", response_model=OrdenRead)
def read_orden_by_id(
    id_orden: int, 
    repository: OrdenRepository = Depends(get_repository)
):
    db_orden = repository.get_by_id(id_orden)
    if not db_orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return db_orden

@router.patch("/{id_orden}", response_model=OrdenRead)
def update_orden(
    id_orden: int, 
    orden: OrdenUpdate, 
    repository: OrdenRepository = Depends(get_repository)
):
    db_orden = repository.update(id_orden, orden)
    if not db_orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return db_orden

@router.delete("/{id_orden}")
def delete_orden(
    id_orden: int, 
    repository: OrdenRepository = Depends(get_repository)
):
    success = repository.delete(id_orden)
    if not success:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return {"ok": True}
