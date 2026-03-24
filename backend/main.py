from fastapi import FastAPI
from contextlib import asynccontextmanager
from modules.shared.database import create_db_and_tables
from modules.clientes.api.v1.router import router as clientes_router
from modules.locales.api.v1.router import router as locales_router
from modules.productos.api.v1.router import router as productos_router
from modules.trabajadores.api.v1.router import router as trabajadores_router
from modules.mesas.api.v1.router import router as mesas_router
from modules.ordenes.api.v1.router import router as ordenes_router
from modules.ventas.api.v1.router import router as ventas_router
from modules.propietarios.api.v1.router import router as propietarios_router
from modules.cadenas.api.v1.router import router as cadenas_router

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
app.include_router(locales_router, prefix="/api/v1")
app.include_router(productos_router, prefix="/api/v1")
app.include_router(trabajadores_router, prefix="/api/v1")
app.include_router(mesas_router, prefix="/api/v1")
app.include_router(ordenes_router, prefix="/api/v1")
app.include_router(ventas_router, prefix="/api/v1")
app.include_router(propietarios_router, prefix="/api/v1")
app.include_router(cadenas_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API del Proyecto Integrador"}
