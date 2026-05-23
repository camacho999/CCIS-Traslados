# Makefile para Flask App
.PHONY: install run dev test clean db-init db-migrate db-upgrade lint

# Instalar dependencias
install:
pip install -r requirements.txt

# Ejecutar aplicación en modo producción
run:
python run.py

# Ejecutar en modo desarrollo con recarga automática
dev:
FLASK_ENV=development flask run --reload

# Ejecutar tests
test:
python -m pytest tests/ -v

# Ejecutar tests con coverage
test-coverage:
python -m pytest tests/ --cov=app --cov-report=html

# Limpiar archivos temporales
clean:
find . -type f -name "*.pyc" -delete
find . -type d -name "__pycache__" -delete
find . -type d -name ".pytest_cache" -delete
rm -rf htmlcov/ .coverage

# Inicializar base de datos
db-init:
flask db init

# Crear migración
db-migrate:
flask db migrate -m "migration message"

# Aplicar migraciones
db-upgrade:
flask db upgrade

# Downgrade migraciones
db-downgrade:
flask db downgrade

# Ejecutar linter
lint:
flake8 app/ config/ tests/

# Formatear código
format:
black app/ config/ tests/ run.py

# Crear usuario admin (ejemplo)
create-admin:
python -c "from app import create_app, db; from app.models.user import User; \
app = create_app(); \
with app.app_context(): \
user = User(username='admin', email='admin@example.com', is_admin=True); \
user.set_password('admin123'); \
db.session.add(user); \
db.session.commit(); \
print('Admin creado exitosamente')"
