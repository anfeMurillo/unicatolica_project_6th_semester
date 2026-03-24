from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from modules.shared.database import get_session
from modules.locales.repositories.locales import LocalRepository
from modules.locales.schemas.locales import LocalCreate, LocalUpdate, LocalRead

router = APIRouter(prefix="/locales", tags=["locales"])

def get_repository(session: Session = Depends(get_session)) -> LocalRepository:
    return LocalRepository(session)

@router.post("/", response_model=LocalRead)
def create_local(
    local: LocalCreate, 
    repository: LocalRepository = Depends(get_repository)
):
    return repository.create(local)

@router.get("/", response_model=List[LocalRead])
def read_locales(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    repository: LocalRepository = Depends(get_repository)
):
    return repository.get_all(offset=offset, limit=limit)

@router.get("/{id_local}", response_model=LocalRead)
def read_local_by_id(
    id_local: int, 
    repository: LocalRepository = Depends(get_repository)
):
    db_local = repository.get_by_id(id_local)
    if not db_local:
        raise HTTPException(status_code=404, detail="Local no encontrado")
    return db_local

@router.patch("/{id_local}", response_model=LocalRead)
def update_local(
    id_local: int, 
    local: LocalUpdate, 
    repository: LocalRepository = Depends(get_repository)
):
    db_local = repository.update(id_local, local)
    if not db_local:
        raise HTTPException(status_code=404, detail="Local no encontrado")
    return db_local

@router.delete("/{id_local}")
def delete_local(
    id_local: int, 
    repository: LocalRepository = Depends(get_repository)
):
    success = repository.delete(id_local)
    if not success:
        raise HTTPException(status_code=404, detail="Local no encontrado")
    return {"ok": True}
