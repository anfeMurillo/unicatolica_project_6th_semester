# Proyecto Integrador - Backend

## Descripción
API para la gestión de múltiples cadenas de restaurantes. Desarrollado con **FastAPI** y **SQLModel**, siguiendo principios de arquitectura limpia y desarrollo guiado por pruebas (TDD). Permite a los dueños de negocios administrar sus cadenas (locales, productos, empleados, ventas) de forma centralizada y segura.

## Requisitos
- Python 3.12+
- `uv` como gestor de paquetes y entornos virtuales.

## Instalación y Ejecución

1. Asegúrate de tener `uv` instalado, y luego sincroniza las dependencias (se creará un entorno virtual automáticamente):
   ```bash
   uv sync
   ```
   *(Si `uv` falla o no lo tienes en el PATH, asegúrate de instalarlo según la [documentación oficial](https://github.com/astral-sh/uv#installation)).*

2. Activa el entorno virtual e inicia el servidor de desarrollo:
   ```bash
   # En Windows:
   .venv\Scripts\activate
   
   # O utilizando uv directamente:
   uv run fastapi dev main.py
   ```

## Documentación API interactiva
Una vez corriendo el servidor (por defecto en el puerto 8000), puedes explorar y probar la API desde tu navegador:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Arquitectura
Para comprender cómo está estructurado el código, qué patrones de diseño se usan, y cómo están organizados los módulos, referirse al documento detallado de [Arquitectura (architecture.md)](architecture.md).
