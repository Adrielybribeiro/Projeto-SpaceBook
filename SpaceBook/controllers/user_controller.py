from flask import Blueprint, request, jsonify
from workers.user_worker import registrar_usuario, login_usuario

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')
    return registrar_usuario(nome, email, senha)

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')
    return login_usuario(email, senha)
