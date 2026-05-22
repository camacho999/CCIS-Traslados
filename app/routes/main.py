"""
Blueprint principal de la aplicación
"""
from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Página de inicio."""
    return render_template('index.html')


@main_bp.route('/about')
def about():
    """Página sobre el proyecto."""
    return render_template('about.html')
