from fastapi import FastAPI
from contextlib import asynccontextmanager
from modules.shared.database import create_db_and_tables
from modules.clientes.api.v1.router import router as clientes_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database
    create_db_and_tables()
    yield

app = FastAPI(
    title="Proyecto Integrador - Restaurante",
    description="API para la gestión de cadenas de restaurantes",
    version="0.1.0",
    lifespan=lifespan
)

# Include routers
app.include_router(clientes_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API del Proyecto Integrador"}
