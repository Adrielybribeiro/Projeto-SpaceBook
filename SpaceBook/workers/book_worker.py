
from repositories.book_repository import (
    criar_livro, listar_livros, atualizar_livro,
    deletar_livro, avaliar_livro
)
from flask import jsonify

def listar_livros_worker(filtros):
    livros = listar_livros(filtros)  # Verifique se isso não está quebrando!
    lista = [
        {'id': l[0], 'titulo': l[1], 'autor': l[2], 'genero': l[3], 'ano': l[4], 'nota': l[5]}
        for l in livros
    ]
    return jsonify(lista), 200

def criar_livro_worker(data):
    criar_livro(data['titulo'], data['autor'], data['genero'], data['ano'])
    return {'mensagem': 'Livro criado com sucesso'}, 201

def atualizar_livro_worker(id_livro, data, is_admin):
    if not is_admin:
        return {'erro': 'Apenas administradores podem editar livros'}, 403
    atualizar_livro(id_livro, data['titulo'], data['autor'], data['genero'], data['ano'])
    return {'mensagem': 'Livro atualizado com sucesso'}, 200

def deletar_livro_worker(id_livro, is_admin):
    if not is_admin:
        return {'erro': 'Apenas administradores podem remover livros'}, 403
    deletar_livro(id_livro)
    return {'mensagem': 'Livro removido'}, 200

def avaliar_livro_worker(id_livro, nota):
    if nota < 0 or nota > 5:
        return {'erro': 'Nota deve estar entre 0 e 5'}, 400
    avaliar_livro(id_livro, nota)
    return {'mensagem': 'Livro avaliado com sucesso'}, 200
