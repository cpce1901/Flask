from flask import Blueprint, render_template, jsonify, request


api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/api-all', methods=['GET'])
def api_all():    
    return "API-ALL"

@api_bp.route('/api-last', methods=['GET'])
def api_last():    
    return "API-LAST"

@api_bp.route('/api-add', methods=['POST'])
def api_add():    
    return "API-ADD"
