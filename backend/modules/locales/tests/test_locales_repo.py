import pytest
from sqlmodel import Session, create_engine, SQLModel
from modules.locales.repositories.locales import LocalRepository
from modules.locales.schemas.locales import LocalCreate, LocalUpdate
from modules.locales.models.locales import Local

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def test_create_local(session: Session):
    repository = LocalRepository(session)
    local_in = LocalCreate(nombre="Sede Principal", direccion="Calle 123 #45-67")
    local = repository.create(local_in)
    assert local.id_local is not None
    assert local.nombre == "Sede Principal"
    assert local.direccion == "Calle 123 #45-67"

def test_get_local(session: Session):
    repository = LocalRepository(session)
    local_in = LocalCreate(nombre="Sede Principal", direccion="Calle 123 #45-67")
    created_local = repository.create(local_in)
    
    fetched_local = repository.get_by_id(created_local.id_local)
    assert fetched_local is not None
    assert fetched_local.id_local == created_local.id_local

def test_update_local(session: Session):
    repository = LocalRepository(session)
    local_in = LocalCreate(nombre="Sede Principal", direccion="Calle 123 #45-67")
    created_local = repository.create(local_in)
    
    update_data = LocalUpdate(nombre="Sede Norte")
    updated_local = repository.update(created_local.id_local, update_data)
    assert updated_local.nombre == "Sede Norte"
    assert updated_local.direccion == "Calle 123 #45-67"

def test_delete_local(session: Session):
    repository = LocalRepository(session)
    local_in = LocalCreate(nombre="Sede Principal", direccion="Calle 123 #45-67")
    created_local = repository.create(local_in)
    
    success = repository.delete(created_local.id_local)
    assert success is True
    assert repository.get_by_id(created_local.id_local) is None
