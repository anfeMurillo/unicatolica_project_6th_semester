from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from modules.shared.database import get_session
from modules.cadenas.repositories.cadenas import CadenaRepository
from modules.cadenas.schemas.cadenas import CadenaCreate, CadenaUpdate, CadenaRead

router = APIRouter(prefix="/cadenas", tags=["cadenas"])

def get_repository(session: Session = Depends(get_session)) -> CadenaRepository:
    return CadenaRepository(session)

@router.post("/", response_model=CadenaRead)
def create_cadena(
    cadena: CadenaCreate, 
    repository: CadenaRepository = Depends(get_repository)
):
    return repository.create(cadena)

@router.get("/", response_model=List[CadenaRead])
def read_cadenas(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    repository: CadenaRepository = Depends(get_repository)
):
    return repository.get_all(skip=offset, limit=limit)

@router.get("/{id_cadena}", response_model=CadenaRead)
def read_cadena_by_id(
    id_cadena: int, 
    repository: CadenaRepository = Depends(get_repository)
):
    db_cadena = repository.get_by_id(id_cadena)
    if not db_cadena:
        raise HTTPException(status_code=404, detail="Cadena no encontrada")
    return db_cadena

@router.patch("/{id_cadena}", response_model=CadenaRead)
def update_cadena(
    id_cadena: int, 
    cadena: CadenaUpdate, 
    repository: CadenaRepository = Depends(get_repository)
):
    db_cadena = repository.update(id_cadena, cadena)
    if not db_cadena:
        raise HTTPException(status_code=404, detail="Cadena no encontrada")
    return db_cadena

@router.delete("/{id_cadena}")
def delete_cadena(
    id_cadena: int, 
    repository: CadenaRepository = Depends(get_repository)
):
    success = repository.delete(id_cadena)
    if not success:
        raise HTTPException(status_code=404, detail="Cadena no encontrada")
    return {"ok": True}
