# Flask Application Configuration
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuración base de la aplicación."""
    
    # Configuración secreta
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-in-production'
    
    # Configuración de SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
    }
    
    # Configuración de Flask-Limiter
    RATELIMIT_DEFAULT = "100 per hour"
    RATELIMIT_STORAGE_URL = os.environ.get('REDIS_URL') or "memory://"
    
    # Configuración de WTF
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = None
    
    # Configuración de sesión
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hora


class DevelopmentConfig(Config):
    """Configuración para desarrollo."""
    DEBUG = True
    ENV = 'development'


class ProductionConfig(Config):
    """Configuración para producción."""
    DEBUG = False
    ENV = 'production'
    
    # En producción, usar una clave secreta más segura
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # Base de datos en producción (ej. PostgreSQL)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'


class TestingConfig(Config):
    """Configuración para testing."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
