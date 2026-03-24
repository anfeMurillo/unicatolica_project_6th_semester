import pytest
from sqlmodel import Session, create_engine, SQLModel
from modules.mesas.repositories.mesas import MesaRepository
from modules.mesas.schemas.mesas import MesaCreate, MesaUpdate
from modules.mesas.models.mesas import Mesas

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def test_create_mesa(session: Session):
    repository = MesaRepository(session)
    mesa_in = MesaCreate(numero=5, id_local=1)
    mesa = repository.create(mesa_in)
    assert mesa.id_mesa is not None
    assert mesa.numero == 5
    assert mesa.id_local == 1

def test_get_mesa(session: Session):
    repository = MesaRepository(session)
    mesa_in = MesaCreate(numero=5, id_local=1)
    created_mesa = repository.create(mesa_in)
    
    fetched_mesa = repository.get_by_id(created_mesa.id_mesa)
    assert fetched_mesa is not None
    assert fetched_mesa.id_mesa == created_mesa.id_mesa

def test_update_mesa(session: Session):
    repository = MesaRepository(session)
    mesa_in = MesaCreate(numero=5, id_local=1)
    created_mesa = repository.create(mesa_in)
    
    update_data = MesaUpdate(numero=10)
    updated_mesa = repository.update(created_mesa.id_mesa, update_data)
    assert updated_mesa.numero == 10
    assert updated_mesa.id_local == 1

def test_delete_mesa(session: Session):
    repository = MesaRepository(session)
    mesa_in = MesaCreate(numero=5, id_local=1)
    created_mesa = repository.create(mesa_in)
    
    success = repository.delete(created_mesa.id_mesa)
    assert success is True
    assert repository.get_by_id(created_mesa.id_mesa) is None
