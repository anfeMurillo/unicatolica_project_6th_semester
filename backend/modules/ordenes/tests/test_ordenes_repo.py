import pytest
from sqlmodel import Session, create_engine, SQLModel
from modules.ordenes.repositories.ordenes import OrdenRepository
from modules.ordenes.schemas.ordenes import OrdenCreate, OrdenUpdate
from modules.ordenes.models.ordenes import Ordenes

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def test_create_orden(session: Session):
    repository = OrdenRepository(session)
    orden_in = OrdenCreate(id_cliente=1, id_empleado=2, id_mesa=3, estado="pendiente")
    orden = repository.create(orden_in)
    assert orden.id_orden is not None
    assert orden.estado == "pendiente"
    assert orden.id_cliente == 1

def test_get_orden(session: Session):
    repository = OrdenRepository(session)
    orden_in = OrdenCreate(id_cliente=1, id_empleado=2, id_mesa=3, estado="pendiente")
    created_orden = repository.create(orden_in)
    
    fetched_orden = repository.get_by_id(created_orden.id_orden)
    assert fetched_orden is not None
    assert fetched_orden.id_orden == created_orden.id_orden
    assert fetched_orden.fecha is not None

def test_update_orden(session: Session):
    repository = OrdenRepository(session)
    orden_in = OrdenCreate(id_cliente=1, id_empleado=2, id_mesa=3, estado="pendiente")
    created_orden = repository.create(orden_in)
    
    update_data = OrdenUpdate(estado="pagado")
    updated_orden = repository.update(created_orden.id_orden, update_data)
    assert updated_orden.estado == "pagado"
    assert updated_orden.id_cliente == 1

def test_delete_orden(session: Session):
    repository = OrdenRepository(session)
    orden_in = OrdenCreate(id_cliente=1, id_empleado=2, id_mesa=3, estado="pendiente")
    created_orden = repository.create(orden_in)
    
    success = repository.delete(created_orden.id_orden)
    assert success is True
    assert repository.get_by_id(created_orden.id_orden) is None
