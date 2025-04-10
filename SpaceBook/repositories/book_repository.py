from flask import g

def criar_livro(titulo, autor, genero, ano):
    g.cursor.execute("""
        INSERT INTO livros (titulo, autor, genero, ano_publicacao)
        VALUES (%s, %s, %s, %s)
    """, (titulo, autor, genero, ano))
    g.db.commit()

def listar_livros(filtros):
    query = "SELECT id, titulo, autor, genero, ano_publicacao, nota FROM livros WHERE 1=1"
    params = []

    if 'titulo' in filtros:
        query += " AND titulo LIKE %s"
        params.append(f"%{filtros['titulo']}%")
    if 'autor' in filtros:
        query += " AND autor LIKE %s"
        params.append(f"%{filtros['autor']}%")
    if 'genero' in filtros:
        query += " AND genero = %s"
        params.append(filtros['genero'])
    if 'ano' in filtros:
        query += " AND ano_publicacao = %s"
        params.append(filtros['ano'])

    g.cursor.execute(query, tuple(params))
    return g.cursor.fetchall()

def atualizar_livro(id_livro, titulo, autor, genero, ano):
    g.cursor.execute("""
        UPDATE livros SET titulo=%s, autor=%s, genero=%s, ano_publicacao=%s WHERE id=%s
    """, (titulo, autor, genero, ano, id_livro))
    g.db.commit()

def deletar_livro(id_livro):
    g.cursor.execute("DELETE FROM livros WHERE id = %s", (id_livro,))
    g.db.commit()

def avaliar_livro(id_livro, nota):
    g.cursor.execute("UPDATE livros SET nota = %s WHERE id = %s", (nota, id_livro))
    g.db.commit()
