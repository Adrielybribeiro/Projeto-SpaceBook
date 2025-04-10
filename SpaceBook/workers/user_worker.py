import hashlib
from repositories.user_repository import buscar_usuario_por_email, criar_usuario
from utils.jwt_utils import gerar_token

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def registrar_usuario(nome, email, senha, is_admin=False):
    if buscar_usuario_por_email(email):
        return {'erro': 'Email já cadastrado'}, 400
    senha_hash = hash_senha(senha)
    criar_usuario(nome, email, senha_hash, is_admin)
    return {'mensagem': 'Usuário criado com sucesso'}, 201

def login_usuario(email, senha):
    user = buscar_usuario_por_email(email)
    if not user:
        return {'erro': 'Usuário não encontrado'}, 404
    senha_hash = hash_senha(senha)
    if senha_hash != user[3]:
        return {'erro': 'Senha incorreta'}, 401
    token = gerar_token(user[0], user[4])
    return {'token': token}, 200
