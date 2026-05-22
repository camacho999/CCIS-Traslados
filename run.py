"""
Script principal para ejecutar la aplicación Flask
"""
import os
from app import create_app, db
from app.models.user import User

# Crear la aplicación con la configuración adecuada
app = create_app(os.environ.get('FLASK_ENV', 'development'))


@app.shell_context_processor
def make_shell_context():
    """Contexto para flask shell."""
    return {'db': db, 'User': User}


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
