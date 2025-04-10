from flask import g

def buscar_usuario_por_email(email):
    g.cursor.execute("SELECT id, nome, email, senha, is_admin FROM usuarios WHERE email = %s", (email,))
    return g.cursor.fetchone()

def criar_usuario(nome, email, senha, is_admin=False):
    g.cursor.execute("INSERT INTO usuarios (nome, email, senha, is_admin) VALUES (%s, %s, %s, %s)",
                     (nome, email, senha, is_admin))
    g.db.commit()
