from flask import Blueprint, render_template


reportes_bp = Blueprint('reportes_bp', __name__)

@reportes_bp.route('/reportes')
def reportes():
    
    return "REPORTES"
