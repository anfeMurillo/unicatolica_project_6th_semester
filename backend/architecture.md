# Arquitectura del Backend

El backend está diseñado siguiendo los principios de **Clean Architecture** (Arquitectura Limpia) y el enfoque modular de **Domain-Driven Design (DDD)**. Toda la lógica está dividida por conceptos del negocio (módulos), lo que permite que el proyecto sea altamente escalable y mantenible.

Recientemente se implementó una **arquitectura Multi-Tenant** que permite a múltiples `propietarios` gestionar sus respectivas `cadenas` de restaurantes asegurando el aislamiento de datos.

## Estructura Global

```text
backend/
├── main.py              # Punto de entrada de FastAPI y registro de dependencias
├── pyproject.toml       # Dependencias y configuración principal de Python (vía uv)
├── README.md            # Información básica del proyecto
├── architecture.md      # Documentación arquitectónica (este archivo)
└── modules/             # Lógica principal subdividida en entidades del negocio
    ├── shared/          # Código transversal (Conexión BD, utilidades comunes)
    ├── propietarios/    # Gestión de dueños de negocios (Multi-tenant)
    ├── cadenas/         # Gestión de empresas asociadas a un propietario
    ├── clientes/
    ├── locales/         # Sucursales asociadas a una cadena
    ├── mesas/
    ├── ordenes/
    ├── productos/       # Productos asociados a una cadena
    ├── trabajadores/
    └── ventas/
```

## Anatomía de un Módulo
Cada módulo dentro de `modules/` encapsula una entidad y está dividido en subcapas, separando estrictamente responsabilidades (Principio de Responsabilidad Única - SRP).

```text
modulo_ejemplo/
├── models/
│   └── modulo_ejemplo.py    # Modelos SQLModel (Tablas en la BD)
├── schemas/
│   └── modulo_ejemplo.py    # Modelos Pydantic (Validación de entrada y salida DTOs)
├── repositories/
│   └── modulo_ejemplo.py    # Patrón Repository: Acceso y abstracción a los datos (CRUD)
├── api/v1/
│   └── router.py            # Enrutador FastAPI (Endpoints HTTP)
└── tests/
    └── test_ejemplo_repo.py # Pruebas unitarias del módulo (TDD)
```

## Principios de Diseño Aplicados

### 1. Inyección de Dependencias (Dependency Injection)
Todos los componentes delegan la creación de sus dependencias, usando el sistema subyacente de `Depends` de FastAPI.
- El objeto de sesión de la BD (`Session`) se inyecta en el **Repository**.
- El **Repository** se inyecta en el **Router** (controlador).
Esto evita crear objetos estáticos o dependencias acopladas globales y mejora enormemente la capacidad de hacer pruebas unitarias (Mocking).

### 2. Patrón Repositorio (Repository Pattern)
Nuestros endpoints (routers) no realizan directamente operaciones SQL, sino que delegan las llamadas a objetos `Repository`. El `Repository` media entre el dominio (la lógica del negocio) y la capa de persistencia (`SQLModel`).

### 3. Principio de Responsabilidad Única (SRP de SOLID)
Cada sub-directorio sirve un único propósito:
- **`models`**: Entienden cómo la BD almacena y define entidades.
- **`schemas`**: Aseguran los tipos exactos, ocultando información crítica hacia/desde las peticiones HTTP (DTOs).
- **`repositories`**: Orquestan persistencia de datos (insert, update, delete, select).
- **`api`**: Maneja el ciclo de vida de peticiones web (HTTP request/response), valida datos serializables mediante schemas, y llama al repositorio apropiado.

### 4. Pruebas y TDD (Test-Driven Development)
Cada módulo cuenta con un suite propia de pruebas con `pytest`. Dichos tests definen una Base de Datos EFÍMERA en SQLite en memoria (`sqlite:///:memory:`) inyectando esta sesión "limpia" en el `Repository`. Con esto, garantizamos el correcto funcionamiento de toda la manipulación de data sin depender de infraestructura externa (como PostgreSQL) al momento de testear la lógica.
