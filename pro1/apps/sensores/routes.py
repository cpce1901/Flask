from flask import Blueprint, render_template


sensores_bp = Blueprint('sensores_bp', __name__)

@sensores_bp.route('/sensores')
def sensores():
    
    return "SENSORES"
