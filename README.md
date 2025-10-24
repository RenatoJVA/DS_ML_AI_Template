# Template para Proyectos de Data Science, Machine Learning e IA

Este repositorio es un template robusto y escalable diseñado para iniciar rápidamente proyectos complejos de ciencia de datos, machine learning e inteligencia artificial. Incluye una configuración moderna y las mejores prácticas para el desarrollo, la gestión de dependencias y la infraestructura.

## Características

- **Gestión de Entorno con `uv`**: Utiliza `uv` para una gestión de dependencias y entornos virtuales de Python ultrarrápida.
- **Base de Datos con Docker**: Configuración de servicios contenerizados usando Docker y Docker Compose.
- **PostgreSQL + pgvector**: Incluye una base de datos PostgreSQL con la extensión `pgvector` preinstalada, ideal para aplicaciones de IA que requieren búsqueda por similitud (embeddings).
- **Gestión de Secretos**: Uso de un archivo `.env` para gestionar de forma segura las credenciales y configuraciones.
- **Estructura de Proyecto Escalable**: Una organización de archivos y directorios pensada para crecer.

## Cómo Empezar

Sigue estos pasos para configurar tu entorno de desarrollo local.

### Prerrequisitos

Asegúrate de tener instaladas las siguientes herramientas en tu sistema:

- [Python](https://www.python.org/downloads/) (versión 3.10 o superior)
- [Docker](https://www.docker.com/get-started) y [Docker Compose](https://docs.docker.com/compose/install/)
- `uv`:
  ```bash
  pip install uv
  ```

### Instalación

1. **Clona el repositorio:**
   ```bash
   git clone <URL-del-repositorio>
   cd <nombre-del-repositorio>
   ```

2. **Configura las variables de entorno:**
   Crea una copia del archivo de ejemplo `.env.example` (si existiera) o crea un archivo `.env` nuevo en la raíz del proyecto. Debería contener como mínimo:
   ```env
   # Credenciales de la base de datos
   POSTGRES_DB=mydatabase
   POSTGRES_USER=myuser
   POSTGRES_PASSWORD=mypassword
   ```

3. **Levanta la base de datos:**
   Este comando iniciará un contenedor de Docker con PostgreSQL y pgvector en segundo plano.
   ```bash
   docker-compose up -d
   ```
   Puedes verificar que el contenedor está corriendo con `docker ps`.

4. **Crea el entorno virtual e instala las dependencias:**
   Usa `uv` para crear el entorno y sincronizar las dependencias listadas en `pyproject.toml`.
   ```bash
   uv venv
   uv sync
   ```

## Estructura del Proyecto

```
.
├── .env                # Archivo para variables de entorno (ignorado por Git)
├── .gitignore          # Archivos y directorios ignorados por Git
├── .python-version     # Versión de Python para el proyecto
├── docker-compose.yml  # Configuración de Docker para la base de datos
├── Dockerfile          # Dockerfile para la aplicación (si se necesita)
├── main.py             # Punto de entrada principal de la aplicación
├── pyproject.toml      # Dependencias y configuración del proyecto Python
├── README.md           # Documentación del proyecto
└── uv.lock             # Archivo de bloqueo de dependencias de uv
```

## Uso

Para ejecutar el script principal de la aplicación:

```bash
uv run python main.py
```

## Base de Datos

Este template utiliza una base de datos **PostgreSQL** con la extensión **pgvector**, que se ejecuta en un contenedor de Docker.

- **Host**: `localhost`
- **Puerto**: `5432`
- **Usuario**: El valor de `POSTGRES_USER` en tu archivo `.env`
- **Contraseña**: El valor de `POSTGRES_PASSWORD` en tu archivo `.env`
- **Base de datos**: El valor de `POSTGRES_DB` en tu archivo `.env`

Para conectarte a la base de datos desde tu aplicación Python, necesitarás un conector como `psycopg2`. Puedes instalarlo con:

```bash
uv pip install psycopg2-binary
```

## Desarrollo

_(Sección de ejemplo - adaptar según las necesidades)_

### Testing

Para ejecutar las pruebas unitarias:
```bash
uv run pytest
```

### Linting y Formateo

Para asegurar un estilo de código consistente, usamos `ruff`:
```bash
# Formatear el código
uv run ruff format .

# Revisar por errores de linting
uv run ruff check .
```
