from flask import Blueprint, request, jsonify
from workers.book_worker import (
    criar_livro_worker, listar_livros_worker, atualizar_livro_worker,
    deletar_livro_worker, avaliar_livro_worker
)
from utils.jwt_utils import verificar_token

book_bp = Blueprint('book', __name__)

def get_payload():
    auth = request.headers.get('Authorization')
    if not auth or not auth.startswith("Bearer "):
        return None
    token = auth.split(" ")[1]
    return verificar_token(token)

@book_bp.route('/', methods=['POST'])
def criar():
    payload = get_payload()
    if not payload:
        return {'erro': 'Token inválido'}, 401
    return criar_livro_worker(request.get_json())

@book_bp.route('/', methods=['GET'])
def listar():
    filtros = request.args.to_dict()
    return listar_livros_worker(filtros)

@book_bp.route('/<int:id_livro>', methods=['PUT'])
def editar(id_livro):
    payload = get_payload()
    if not payload:
        return {'erro': 'Token inválido'}, 401
    return atualizar_livro_worker(id_livro, request.get_json(), payload['is_admin'])

@book_bp.route('/<int:id_livro>', methods=['DELETE'])
def deletar(id_livro):
    payload = get_payload()
    if not payload:
        return {'erro': 'Token inválido'}, 401
    return deletar_livro_worker(id_livro, payload['is_admin'])

@book_bp.route('/<int:id_livro>/avaliar', methods=['POST'])
def avaliar(id_livro):
    nota = request.get_json().get('nota')
    return avaliar_livro_worker(id_livro, nota)
