from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from modules.shared.database import get_session
from modules.mesas.repositories.mesas import MesaRepository
from modules.mesas.schemas.mesas import MesaCreate, MesaUpdate, MesaRead

router = APIRouter(prefix="/mesas", tags=["mesas"])

def get_repository(session: Session = Depends(get_session)) -> MesaRepository:
    return MesaRepository(session)

@router.post("/", response_model=MesaRead)
def create_mesa(
    mesa: MesaCreate, 
    repository: MesaRepository = Depends(get_repository)
):
    return repository.create(mesa)

@router.get("/", response_model=List[MesaRead])
def read_mesas(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    repository: MesaRepository = Depends(get_repository)
):
    return repository.get_all(offset=offset, limit=limit)

@router.get("/{id_mesa}", response_model=MesaRead)
def read_mesa_by_id(
    id_mesa: int, 
    repository: MesaRepository = Depends(get_repository)
):
    db_mesa = repository.get_by_id(id_mesa)
    if not db_mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    return db_mesa

@router.patch("/{id_mesa}", response_model=MesaRead)
def update_mesa(
    id_mesa: int, 
    mesa: MesaUpdate, 
    repository: MesaRepository = Depends(get_repository)
):
    db_mesa = repository.update(id_mesa, mesa)
    if not db_mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    return db_mesa

@router.delete("/{id_mesa}")
def delete_mesa(
    id_mesa: int, 
    repository: MesaRepository = Depends(get_repository)
):
    success = repository.delete(id_mesa)
    if not success:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    return {"ok": True}
