import pytest
from sqlmodel import Session, create_engine, SQLModel
from modules.productos.repositories.productos import ProductoRepository
from modules.productos.schemas.productos import ProductoCreate, ProductoUpdate
from modules.productos.models.productos import Productos

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def test_create_producto(session: Session):
    repository = ProductoRepository(session)
    producto_in = ProductoCreate(nombre="Hamburguesa Clásica", descripcion="Carne, queso, lechuga, tomate", precio=15000)
    producto = repository.create(producto_in)
    assert producto.id_producto is not None
    assert producto.nombre == "Hamburguesa Clásica"
    assert producto.precio == 15000

def test_get_producto(session: Session):
    repository = ProductoRepository(session)
    producto_in = ProductoCreate(nombre="Hamburguesa Clásica", descripcion="Carne, queso, lechuga, tomate", precio=15000)
    created_producto = repository.create(producto_in)
    
    fetched_producto = repository.get_by_id(created_producto.id_producto)
    assert fetched_producto is not None
    assert fetched_producto.id_producto == created_producto.id_producto

def test_update_producto(session: Session):
    repository = ProductoRepository(session)
    producto_in = ProductoCreate(nombre="Hamburguesa Clásica", descripcion="Carne, queso, lechuga, tomate", precio=15000)
    created_producto = repository.create(producto_in)
    
    update_data = ProductoUpdate(precio=16000)
    updated_producto = repository.update(created_producto.id_producto, update_data)
    assert updated_producto.nombre == "Hamburguesa Clásica"
    assert updated_producto.precio == 16000

def test_delete_producto(session: Session):
    repository = ProductoRepository(session)
    producto_in = ProductoCreate(nombre="Hamburguesa Clásica", descripcion="Carne, queso, lechuga, tomate", precio=15000)
    created_producto = repository.create(producto_in)
    
    success = repository.delete(created_producto.id_producto)
    assert success is True
    assert repository.get_by_id(created_producto.id_producto) is None
