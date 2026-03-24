import pytest
from sqlmodel import Session, create_engine, SQLModel
from modules.cadenas.repositories.cadenas import CadenaRepository
from modules.cadenas.schemas.cadenas import CadenaCreate, CadenaUpdate
from modules.cadenas.models.cadenas import Cadena
from modules.propietarios.models.propietarios import Propietario

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        # Crea un propietario mock para las fk constraints de SQLite (si activadas)
        # o simplemente lo dejamos insertado.
        propietario = Propietario(nombre="Mock Propietario", correo="mock@test.com", clave_hash="secret")
        session.add(propietario)
        session.commit()
        session.refresh(propietario)
        # Guardo el id en la session para usarlo
        session.info["mock_propietario_id"] = propietario.id_propietario
        yield session

def test_create_cadena(session: Session):
    repository = CadenaRepository(session)
    propietario_id = session.info["mock_propietario_id"]
    cadena_in = CadenaCreate(nombre="Cadena 1", descripcion="Desc", id_propietario=propietario_id)
    cadena = repository.create(cadena_in)
    assert cadena.id_cadena is not None
    assert cadena.nombre == "Cadena 1"

def test_get_cadena(session: Session):
    repository = CadenaRepository(session)
    propietario_id = session.info["mock_propietario_id"]
    cadena_in = CadenaCreate(nombre="Cadena 1", descripcion="Desc", id_propietario=propietario_id)
    created = repository.create(cadena_in)
    
    fetched = repository.get_by_id(created.id_cadena)
    assert fetched is not None
    assert fetched.id_cadena == created.id_cadena

def test_update_cadena(session: Session):
    repository = CadenaRepository(session)
    propietario_id = session.info["mock_propietario_id"]
    cadena_in = CadenaCreate(nombre="Cadena 1", descripcion="Desc", id_propietario=propietario_id)
    created = repository.create(cadena_in)
    
    update_data = CadenaUpdate(nombre="Cadena Updated")
    updated = repository.update(created.id_cadena, update_data)
    assert updated.nombre == "Cadena Updated"

def test_delete_cadena(session: Session):
    repository = CadenaRepository(session)
    propietario_id = session.info["mock_propietario_id"]
    cadena_in = CadenaCreate(nombre="Cadena 1", descripcion="Desc", id_propietario=propietario_id)
    created = repository.create(cadena_in)
    
    success = repository.delete(created.id_cadena)
    assert success is True
    assert repository.get_by_id(created.id_cadena) is None
