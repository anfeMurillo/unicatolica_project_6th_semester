from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from modules.shared.database import get_session
from modules.trabajadores.repositories.trabajadores import TrabajadorRepository
from modules.trabajadores.schemas.trabajadores import TrabajadorCreate, TrabajadorUpdate, TrabajadorRead

router = APIRouter(prefix="/trabajadores", tags=["trabajadores"])

def get_repository(session: Session = Depends(get_session)) -> TrabajadorRepository:
    return TrabajadorRepository(session)

@router.post("/", response_model=TrabajadorRead)
def create_trabajador(
    trabajador: TrabajadorCreate, 
    repository: TrabajadorRepository = Depends(get_repository)
):
    return repository.create(trabajador)

@router.get("/", response_model=List[TrabajadorRead])
def read_trabajadores(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    repository: TrabajadorRepository = Depends(get_repository)
):
    return repository.get_all(offset=offset, limit=limit)

@router.get("/{id_trabajador}", response_model=TrabajadorRead)
def read_trabajador_by_id(
    id_trabajador: int, 
    repository: TrabajadorRepository = Depends(get_repository)
):
    db_trabajador = repository.get_by_id(id_trabajador)
    if not db_trabajador:
        raise HTTPException(status_code=404, detail="Trabajador no encontrado")
    return db_trabajador

@router.patch("/{id_trabajador}", response_model=TrabajadorRead)
def update_trabajador(
    id_trabajador: int, 
    trabajador: TrabajadorUpdate, 
    repository: TrabajadorRepository = Depends(get_repository)
):
    db_trabajador = repository.update(id_trabajador, trabajador)
    if not db_trabajador:
        raise HTTPException(status_code=404, detail="Trabajador no encontrado")
    return db_trabajador

@router.delete("/{id_trabajador}")
def delete_trabajador(
    id_trabajador: int, 
    repository: TrabajadorRepository = Depends(get_repository)
):
    success = repository.delete(id_trabajador)
    if not success:
        raise HTTPException(status_code=404, detail="Trabajador no encontrado")
    return {"ok": True}
