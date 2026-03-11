import pytest
from sqlmodel import Session, create_engine, SQLModel
from modules.clientes.repositories.clientes import ClienteRepository
from modules.clientes.schemas.clientes import ClienteCreate, ClienteUpdate
from modules.clientes.models.clientes import Cliente

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def test_create_cliente(session: Session):
    repository = ClienteRepository(session)
    cliente_in = ClienteCreate(nombre="Test User", correo="test@example.com", clave_hash="secret")
    cliente = repository.create(cliente_in)
    assert cliente.id_cliente is not None
    assert cliente.nombre == "Test User"
    assert cliente.correo == "test@example.com"

def test_get_cliente(session: Session):
    repository = ClienteRepository(session)
    cliente_in = ClienteCreate(nombre="Test User", correo="test@example.com", clave_hash="secret")
    created_cliente = repository.create(cliente_in)
    
    fetched_cliente = repository.get_by_id(created_cliente.id_cliente)
    assert fetched_cliente is not None
    assert fetched_cliente.id_cliente == created_cliente.id_cliente

def test_update_cliente(session: Session):
    repository = ClienteRepository(session)
    cliente_in = ClienteCreate(nombre="Test User", correo="test@example.com", clave_hash="secret")
    created_cliente = repository.create(cliente_in)
    
    update_data = ClienteUpdate(nombre="Updated User")
    updated_cliente = repository.update(created_cliente.id_cliente, update_data)
    assert updated_cliente.nombre == "Updated User"
    assert updated_cliente.correo == "test@example.com"

def test_delete_cliente(session: Session):
    repository = ClienteRepository(session)
    cliente_in = ClienteCreate(nombre="Test User", correo="test@example.com", clave_hash="secret")
    created_cliente = repository.create(cliente_in)
    
    success = repository.delete(created_cliente.id_cliente)
    assert success is True
    assert repository.get_by_id(created_cliente.id_cliente) is None
