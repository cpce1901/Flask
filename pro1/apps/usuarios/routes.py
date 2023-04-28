from flask import Blueprint, render_template
from .models import User

usuarios_bp = Blueprint('usuarios_bp', __name__)

@usuarios_bp.route('/usuarios')
def usuarios():
    
    return "USUARIOS"
