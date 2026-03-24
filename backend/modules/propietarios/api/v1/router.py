from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from modules.shared.database import get_session
from modules.propietarios.repositories.propietarios import PropietarioRepository
from modules.propietarios.schemas.propietarios import PropietarioCreate, PropietarioUpdate, PropietarioRead

router = APIRouter(prefix="/propietarios", tags=["propietarios"])

def get_repository(session: Session = Depends(get_session)) -> PropietarioRepository:
    return PropietarioRepository(session)

@router.post("/", response_model=PropietarioRead)
def create_propietario(
    propietario: PropietarioCreate, 
    repository: PropietarioRepository = Depends(get_repository)
):
    return repository.create(propietario)

@router.get("/", response_model=List[PropietarioRead])
def read_propietarios(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    repository: PropietarioRepository = Depends(get_repository)
):
    return repository.get_all(skip=offset, limit=limit)

@router.get("/{id_propietario}", response_model=PropietarioRead)
def read_propietario_by_id(
    id_propietario: int, 
    repository: PropietarioRepository = Depends(get_repository)
):
    db_propietario = repository.get_by_id(id_propietario)
    if not db_propietario:
        raise HTTPException(status_code=404, detail="Propietario no encontrado")
    return db_propietario

@router.patch("/{id_propietario}", response_model=PropietarioRead)
def update_propietario(
    id_propietario: int, 
    propietario: PropietarioUpdate, 
    repository: PropietarioRepository = Depends(get_repository)
):
    db_propietario = repository.update(id_propietario, propietario)
    if not db_propietario:
        raise HTTPException(status_code=404, detail="Propietario no encontrado")
    return db_propietario

@router.delete("/{id_propietario}")
def delete_propietario(
    id_propietario: int, 
    repository: PropietarioRepository = Depends(get_repository)
):
    success = repository.delete(id_propietario)
    if not success:
        raise HTTPException(status_code=404, detail="Propietario no encontrado")
    return {"ok": True}
