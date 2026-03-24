import pytest
from sqlmodel import Session, create_engine, SQLModel
from modules.ventas.repositories.ventas import VentaRepository
from modules.ventas.schemas.ventas import VentaCreate, VentaUpdate
from modules.ventas.models.ventas import Ventas

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def test_create_venta(session: Session):
    repository = VentaRepository(session)
    venta_in = VentaCreate(id_cliente=1, id_orden=2, valor=15000)
    venta = repository.create(venta_in)
    assert venta.id_venta is not None
    assert venta.valor == 15000
    assert venta.id_cliente == 1

def test_get_venta(session: Session):
    repository = VentaRepository(session)
    venta_in = VentaCreate(id_cliente=1, id_orden=2, valor=15000)
    created_venta = repository.create(venta_in)
    
    fetched_venta = repository.get_by_id(created_venta.id_venta)
    assert fetched_venta is not None
    assert fetched_venta.id_venta == created_venta.id_venta
    assert fetched_venta.fecha is not None

def test_update_venta(session: Session):
    repository = VentaRepository(session)
    venta_in = VentaCreate(id_cliente=1, id_orden=2, valor=15000)
    created_venta = repository.create(venta_in)
    
    update_data = VentaUpdate(valor=20000)
    updated_venta = repository.update(created_venta.id_venta, update_data)
    assert updated_venta.valor == 20000
    assert updated_venta.id_cliente == 1

def test_delete_venta(session: Session):
    repository = VentaRepository(session)
    venta_in = VentaCreate(id_cliente=1, id_orden=2, valor=15000)
    created_venta = repository.create(venta_in)
    
    success = repository.delete(created_venta.id_venta)
    assert success is True
    assert repository.get_by_id(created_venta.id_venta) is None
