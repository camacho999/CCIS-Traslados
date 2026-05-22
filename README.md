# Flask App - Proyecto Base

Aplicación Flask moderna con SQLAlchemy, SQLite3 y las mejores prácticas actuales.

## 🚀 Características

- **Flask 3.0** - Framework web ligero y potente
- **SQLAlchemy 2.0** - ORM moderno para gestión de base de datos
- **SQLite3** - Base de datos ligera integrada
- **Flask-Migrate** - Migraciones de base de datos con Alembic
- **Flask-WTF** - Formularios con validación CSRF
- **Flask-Login** - Gestión de sesiones de usuario
- **Flask-Limiter** - Rate limiting para seguridad
- **Estructura modular** - Organización siguiendo el patrón Application Factory

## 📁 Estructura del Proyecto

```
project/
├── app/
│   ├── models/          # Modelos de base de datos
│   │   ├── __init__.py
│   │   └── user.py      # Modelo de usuario
│   ├── routes/          # Blueprints y rutas
│   │   ├── __init__.py
│   │   ├── main.py      # Rutas principales
│   │   ├── auth.py      # Autenticación
│   │   └── forms.py     # Formularios WTForms
│   ├── templates/       # Plantillas HTML
│   │   ├── base.html    # Template base
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── auth/        # Templates de autenticación
│   │   └── errors/      # Templates de errores
│   └── static/          # Archivos estáticos
│       ├── css/
│       │   └── style.css
│       ├── js/
│       │   └── main.js
│       └── img/
├── config/              # Configuración de la aplicación
│   ├── __init__.py
│   └── settings.py      # Configuraciones por entorno
├── migrations/          # Migraciones de base de datos
├── tests/               # Tests unitarios
│   ├── __init__.py
│   └── test_basic.py
├── .env.example         # Ejemplo de variables de entorno
├── .gitignore
├── requirements.txt     # Dependencias del proyecto
├── run.py              # Punto de entrada principal
└── README.md           # Este archivo
```

## 🛠️ Instalación

### Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clonar el repositorio** (si aplica)
```bash
git clone <repository-url>
cd <project-directory>
```

2. **Crear entorno virtual**
```bash
python -m venv venv
```

3. **Activar entorno virtual**

   - **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   - **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

5. **Configurar variables de entorno**
```bash
cp .env.example .env
```

   Editar `.env` y configurar:
   - `SECRET_KEY`: Clave secreta única para producción
   - `DATABASE_URL`: URL de la base de datos (por defecto SQLite)

6. **Inicializar la base de datos**
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## 🎯 Uso

### Iniciar la aplicación

```bash
python run.py
```

O usando Flask CLI:

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

La aplicación estará disponible en `http://localhost:5000`

### Comandos útiles

```bash
# Ejecutar tests
python -m pytest tests/

# Shell de Flask
flask shell

# Migraciones
flask db migrate -m "Descripción del cambio"
flask db upgrade
flask db downgrade
```

## 📝 Modelos Disponibles

### User (Usuario)

El modelo `User` incluye:

- `id`: Identificador único
- `username`: Nombre de usuario (único)
- `email`: Correo electrónico (único)
- `password_hash`: Contraseña hasheada
- `created_at`: Fecha de creación
- `updated_at`: Fecha de actualización
- `is_active`: Estado de la cuenta
- `is_admin`: Rol de administrador

Métodos:
- `set_password(password)`: Hashea y establece la contraseña
- `check_password(password)`: Verifica la contraseña
- `to_dict()`: Convierte el modelo a diccionario

## 🔐 Autenticación

El sistema incluye:

- Registro de usuarios con validación
- Inicio de sesión seguro
- Cierre de sesión
- Protección CSRF en formularios
- Rate limiting para prevenir abusos

## 🧪 Testing

```bash
# Ejecutar todos los tests
python -m pytest tests/ -v

# Ejecutar con coverage
pytest --cov=app tests/
```

## 🌍 Despliegue

### Desarrollo

```bash
export FLASK_ENV=development
python run.py
```

### Producción

1. Configurar variables de entorno seguras
2. Usar un servidor WSGI como Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

## 📦 Dependencias Principales

| Paquete | Versión | Descripción |
|---------|---------|-------------|
| Flask | 3.0.0 | Framework web |
| Flask-SQLAlchemy | 3.1.1 | ORM para base de datos |
| Flask-Migrate | 4.0.5 | Migraciones de DB |
| Flask-WTF | 1.2.1 | Formularios |
| Flask-Login | 0.6.3 | Gestión de sesiones |
| Flask-Limiter | 3.5.0 | Rate limiting |
| SQLAlchemy | 2.0.23 | ORM SQL |

## 🔒 Seguridad

- Protección CSRF habilitada en todos los formularios
- Contraseñas hasheadas con Werkzeug
- Rate limiting para prevenir ataques de fuerza bruta
- Variables de entorno para datos sensibles
- SQL injection prevenido mediante SQLAlchemy ORM

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🤝 Contribuir

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📞 Soporte

Para reportar bugs o solicitar features, por favor abre un issue en el repositorio.

---

**Desarrollado con ❤️ usando Flask y Python**
