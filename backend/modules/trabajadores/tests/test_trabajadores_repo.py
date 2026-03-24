import pytest
from sqlmodel import Session, create_engine, SQLModel
from modules.trabajadores.repositories.trabajadores import TrabajadorRepository
from modules.trabajadores.schemas.trabajadores import TrabajadorCreate, TrabajadorUpdate
from modules.trabajadores.models.trabajadores import Trabajadores

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def test_create_trabajador(session: Session):
    repository = TrabajadorRepository(session)
    trabajador_in = TrabajadorCreate(
        nombre="Juan", 
        apellido="Perez", 
        cargo="Mesero", 
        correo="juan@example.com", 
        clave_hash="secreta123"
    )
    trabajador = repository.create(trabajador_in)
    assert trabajador.id_trabajador is not None
    assert trabajador.nombre == "Juan"
    assert trabajador.cargo == "Mesero"

def test_get_trabajador(session: Session):
    repository = TrabajadorRepository(session)
    trabajador_in = TrabajadorCreate(
        nombre="Juan", 
        apellido="Perez", 
        cargo="Mesero", 
        correo="juan@example.com", 
        clave_hash="secreta123"
    )
    created_trabajador = repository.create(trabajador_in)
    
    fetched_trabajador = repository.get_by_id(created_trabajador.id_trabajador)
    assert fetched_trabajador is not None
    assert fetched_trabajador.id_trabajador == created_trabajador.id_trabajador

def test_update_trabajador(session: Session):
    repository = TrabajadorRepository(session)
    trabajador_in = TrabajadorCreate(
        nombre="Juan", 
        apellido="Perez", 
        cargo="Mesero", 
        correo="juan@example.com", 
        clave_hash="secreta123"
    )
    created_trabajador = repository.create(trabajador_in)
    
    update_data = TrabajadorUpdate(cargo="Supervisor")
    updated_trabajador = repository.update(created_trabajador.id_trabajador, update_data)
    assert updated_trabajador.cargo == "Supervisor"
    assert updated_trabajador.nombre == "Juan"

def test_delete_trabajador(session: Session):
    repository = TrabajadorRepository(session)
    trabajador_in = TrabajadorCreate(
        nombre="Juan", 
        apellido="Perez", 
        cargo="Mesero", 
        correo="juan@example.com", 
        clave_hash="secreta123"
    )
    created_trabajador = repository.create(trabajador_in)
    
    success = repository.delete(created_trabajador.id_trabajador)
    assert success is True
    assert repository.get_by_id(created_trabajador.id_trabajador) is None
