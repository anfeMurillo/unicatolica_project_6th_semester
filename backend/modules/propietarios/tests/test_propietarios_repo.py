import pytest
from sqlmodel import Session, create_engine, SQLModel
from modules.propietarios.repositories.propietarios import PropietarioRepository
from modules.propietarios.schemas.propietarios import PropietarioCreate, PropietarioUpdate
from modules.propietarios.models.propietarios import Propietario

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def test_create_propietario(session: Session):
    repository = PropietarioRepository(session)
    propietario_in = PropietarioCreate(nombre="Propietario 1", correo="admin1@test.com", clave_hash="secret")
    propietario = repository.create(propietario_in)
    assert propietario.id_propietario is not None
    assert propietario.nombre == "Propietario 1"
    assert propietario.correo == "admin1@test.com"

def test_get_propietario(session: Session):
    repository = PropietarioRepository(session)
    propietario_in = PropietarioCreate(nombre="Propietario 1", correo="admin1@test.com", clave_hash="secret")
    created = repository.create(propietario_in)
    
    fetched = repository.get_by_id(created.id_propietario)
    assert fetched is not None
    assert fetched.id_propietario == created.id_propietario

def test_update_propietario(session: Session):
    repository = PropietarioRepository(session)
    propietario_in = PropietarioCreate(nombre="Propietario 1", correo="admin1@test.com", clave_hash="secret")
    created = repository.create(propietario_in)
    
    update_data = PropietarioUpdate(nombre="Propietario Updated")
    updated = repository.update(created.id_propietario, update_data)
    assert updated.nombre == "Propietario Updated"
    assert updated.correo == "admin1@test.com"

def test_delete_propietario(session: Session):
    repository = PropietarioRepository(session)
    propietario_in = PropietarioCreate(nombre="Propietario 1", correo="admin1@test.com", clave_hash="secret")
    created = repository.create(propietario_in)
    
    success = repository.delete(created.id_propietario)
    assert success is True
    assert repository.get_by_id(created.id_propietario) is None
