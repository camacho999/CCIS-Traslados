# Documentación del Proyecto Flask

## Estructura del Proyecto

```
/workspace/
├── app/                      # Paquete principal de la aplicación
│   ├── __init__.py          # Factory function y configuración
│   ├── models/              # Modelos de base de datos (SQLAlchemy)
│   │   ├── __init__.py
│   │   └── user.py          # Modelo de usuario
│   ├── routes/              # Blueprints y rutas
│   │   ├── __init__.py
│   │   ├── main.py          # Rutas principales
│   │   ├── auth.py          # Rutas de autenticación
│   │   └── forms.py         # Formularios WTForms
│   ├── services/            # Lógica de negocio y servicios
│   │   └── __init__.py
│   ├── api/                 # Endpoints API REST (opcional)
│   │   └── __init__.py
│   ├── static/              # Archivos estáticos (CSS, JS, imágenes)
│   │   ├── css/
│   │   └── js/
│   └── templates/           # Templates Jinja2
│       ├── base.html        # Template base
│       ├── index.html       # Página de inicio
│       ├── about.html       # Página "acerca de"
│       ├── auth/            # Templates de autenticación
│       │   ├── login.html
│       │   └── register.html
│       └── errors/          # Templates de errores
│           ├── 404.html
│           └── 500.html
├── config/                  # Configuración de la aplicación
│   ├── __init__.py
│   └── settings.py          # Clases de configuración
├── migrations/              # Migraciones de Flask-Migrate
├── tests/                   # Tests unitarios y de integración
│   ├── __init__.py
│   └── test_basic.py
├── .env.example             # Ejemplo de variables de entorno
├── .gitignore               # Archivos ignorados por Git
├── Makefile                 # Comandos comunes
├── pytest.ini               # Configuración de pytest
├── requirements.txt         # Dependencias principales
├── requirements-dev.txt     # Dependencias de desarrollo
└── run.py                   # Punto de entrada principal
```

## Instalación

### 1. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 2. Instalar dependencias
```bash
# Producción
pip install -r requirements.txt

# Desarrollo
pip install -r requirements-dev.txt
```

### 3. Configurar variables de entorno
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

### 4. Inicializar base de datos
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Ejecución

### Modo desarrollo
```bash
make dev
# o
FLASK_ENV=development flask run --reload
```

### Modo producción
```bash
make run
# o
python run.py
```

## Testing

```bash
# Ejecutar tests
make test

# Con coverage
make test-coverage
```

## Comandos Útiles (Makefile)

- `make install` - Instalar dependencias
- `make dev` - Ejecutar en modo desarrollo
- `make run` - Ejecutar en modo producción
- `make test` - Ejecutar tests
- `make db-init` - Inicializar migraciones
- `make db-migrate` - Crear nueva migración
- `make db-upgrade` - Aplicar migraciones
- `make clean` - Limpiar archivos temporales

## Características Principales

✅ **Flask** con Application Factory Pattern
✅ **SQLAlchemy** como ORM para SQLite3
✅ **Flask-Migrate** para gestión de migraciones
✅ **Flask-WTF** para formularios con validación CSRF
✅ **Flask-Login** para gestión de sesiones de usuario
✅ **Flask-Limiter** para rate limiting
✅ **Blueprints** para organización modular
✅ **Tests** con pytest
✅ **Configuración** separada por entornos
✅ **.env** para variables sensibles

## Próximos Pasos Sugeridos

1. Agregar más modelos según necesidades
2. Implementar API REST en `/app/api/`
3. Agregar servicios en `/app/services/`
4. Implementar autenticación JWT (si es necesario)
5. Agregar logging estructurado
6. Configurar Docker (opcional)
7. Implementar CI/CD
