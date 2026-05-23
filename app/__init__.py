"""
Aplicación Flask con SQLAlchemy y SQLite3
Estructura modular siguiendo buenas prácticas
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager, current_user

# Inicialización de extensiones
db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
limiter = Limiter(key_func=get_remote_address)
login_manager = LoginManager()


def create_app(config_name='development'):
    """Factory function para crear la aplicación Flask."""
    
    app = Flask(__name__)
    
    # Cargar configuración
    from config.settings import config
    app.config.from_object(config[config_name])
    
    # Inicializar extensiones con la app
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    limiter.init_app(app)
    login_manager.init_app(app)
    
    # Configurar login_manager
    from app.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Registrar blueprints
    register_blueprints(app)
    
    # Configurar templates y errores
    register_templates(app)
    register_error_handlers(app)
    
    return app


def register_blueprints(app):
    """Registrar todos los blueprints de la aplicación."""
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')


def register_templates(app):
    """Configurar contexto de templates."""
    @app.context_processor
    def inject_globals():
        """Variables globales disponibles en todos los templates."""
        return {
            'app_name': 'Flask App',
            'current_user': current_user,
        }


def register_error_handlers(app):
    """Registrar manejadores de errores personalizados."""
    from flask import render_template
    
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500
