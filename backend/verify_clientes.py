from sqlmodel import Session, create_engine, SQLModel
from modules.clientes.repositories.clientes import ClienteRepository
from modules.clientes.schemas.clientes import ClienteCreate, ClienteUpdate
from modules.clientes.models.clientes import Cliente

def verify():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        repository = ClienteRepository(session)
        
        # 1. Create
        print("Testing Create...")
        cliente_in = ClienteCreate(nombre="Felipe", correo="felipe@example.com", clave_hash="hash123")
        cliente = repository.create(cliente_in)
        assert cliente.id_cliente is not None
        assert cliente.nombre == "Felipe"
        print(f"Created Cliente with ID: {cliente.id_cliente}")
        
        # 2. Get
        print("Testing Get...")
        fetched = repository.get_by_id(cliente.id_cliente)
        assert fetched.nombre == "Felipe"
        print("Fetched Cliente matches.")
        
        # 3. Update
        print("Testing Update...")
        update_in = ClienteUpdate(nombre="Felipe Updated")
        updated = repository.update(cliente.id_cliente, update_in)
        assert updated.nombre == "Felipe Updated"
        print("Updated Cliente matches.")
        
        # 4. List
        print("Testing List...")
        all_clientes = repository.get_all()
        assert len(all_clientes) == 1
        print(f"List size: {len(all_clientes)}")
        
        # 5. Delete
        print("Testing Delete...")
        success = repository.delete(cliente.id_cliente)
        assert success is True
        assert repository.get_by_id(cliente.id_cliente) is None
        print("Deleted Cliente successfully.")

if __name__ == "__main__":
    try:
        verify()
        print("\nAll Clientes CRUD operations verified successfully!")
    except Exception as e:
        print(f"\nVerification failed: {e}")
        exit(1)
