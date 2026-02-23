# Proyecto Integrador Sexto Semestre

### Estudiantes

Andres Felipe Hurtado [ Tech Lead ]

Andres Felipe Diaz

Esteban Giraldo

### Materias Involucradas

Electiva de Ingenieria

[Docente]

Desarrollo de Software II

[Docente]

Sistemas Operativos

[Docente]

### Sobre el proyecto:

Este es un proyecto basado en una plataforma de gestion
de cadenas de restaurantes enfocado en la parte de gestion del inventario, personal y establecimientos, ademas de una app donde las y los clientes pueden solicitar el platillo sin tener que acercarse a al cajero en ningun momento.

### Stack tecnolocio:

Python:
  - FastAPI
  - SQLModel

Dart:
  - Flutter

Database:
  - PostgreSQL
  - MongoDB

Desiciones de arquitectura en el Backend.
  
1. Arquitectura por Capas (Layered Architecture).
2. Diseño Guiado por Pruebas (Test Drive Desing).
3. Inyeccion de Dependencias (Dependecy Injection).

Este proyecto trabaja sobre la metodologia GitHub Flow.

## 🛠️ Git Best Practices (Senior Level)

Para mantener un historial limpio, escalable y profesional, seguimos estas reglas:

1. Atomic Commits

Cada commit debe resolver una sola tarea lógica. Si corriges un bug y cambias un estilo, haz dos commits. Esto facilita revertir cambios sin efectos colaterales.
2. Conventional Commits

Usamos prefijos estandarizados para identificar la naturaleza del cambio:

    feat: Nueva funcionalidad.

    fix: Corrección de errores.

    docs: Cambios en documentación.

    refactor: Mejora de código (sin cambiar lógica ni arreglar bugs).

    test: Adición o corrección de pruebas.

    chore: Mantenimiento (dependencias, configuración).

3. Writing Effective Messages

    Asunto: Máximo 50 caracteres, en imperativo (Ej: Pon "Agrega validacion de email" , no pongas "Agregado" ...).

    Cuerpo: Explica el porqué del cambio, no el "qué" (el código ya muestra el qué).

    Revisión: Evita git add . a ciegas. Usa git status o git add -p para evitar subir archivos basura (.env, logs, prints).
