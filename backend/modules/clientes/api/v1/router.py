from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from modules.shared.database import get_session
from modules.clientes.repositories.clientes import ClienteRepository
from modules.clientes.schemas.clientes import ClienteCreate, ClienteUpdate, ClienteRead

router = APIRouter(prefix="/clientes", tags=["clientes"])

def get_repository(session: Session = Depends(get_session)) -> ClienteRepository:
    return ClienteRepository(session)

@router.post("/", response_model=ClienteRead)
def create_cliente(
    cliente: ClienteCreate, 
    repository: ClienteRepository = Depends(get_repository)
):
    return repository.create(cliente)

@router.get("/", response_model=List[ClienteRead])
def read_clientes(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    repository: ClienteRepository = Depends(get_repository)
):
    return repository.get_all(offset=offset, limit=limit)

@router.get("/{id_cliente}", response_model=ClienteRead)
def read_cliente_by_id(
    id_cliente: int, 
    repository: ClienteRepository = Depends(get_repository)
):
    db_cliente = repository.get_by_id(id_cliente)
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente

@router.patch("/{id_cliente}", response_model=ClienteRead)
def update_cliente(
    id_cliente: int, 
    cliente: ClienteUpdate, 
    repository: ClienteRepository = Depends(get_repository)
):
    db_cliente = repository.update(id_cliente, cliente)
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente

@router.delete("/{id_cliente}")
def delete_cliente(
    id_cliente: int, 
    repository: ClienteRepository = Depends(get_repository)
):
    success = repository.delete(id_cliente)
    if not success:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {"ok": True}
