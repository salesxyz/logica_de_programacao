from usuario_model import Usuario
from sqlalchemy.orm import Session

session = Session()


def criar_usuario(nome, email, senha):
    usuario_db = Usuario(nome = Usuario.nome, email = Usuario.email, senha = Usuario.senha)
    usuario_db.senha = usuario_db.gen_senha(Usuario.senha)

    session.add(usuario_db)
    session.commit
    return usuario_db


def listar_usuario_email(email):
    Usuario_db = session.query(Usuario).filter(Usuario.email == email).first()
    return Usuario_db


def listar_usuario_id(id):
      usuario_db = session.query(Usuario).filter(Usuario.id == id).first()
    if usuario_db:
        session.delete(usuario_db)
        session.commit()
        return True
    return False


def listar_usario():
    usuario_db = session.query(Usuario).all()
    return usuario_db


def excluir_usuario(id):
    usuario_db = session.query(Usuario).filter(Usuario.id == id).first()
    if usuario_db:
        session.delete(usuario_db)
        session.commit()
        return True
    return None 

def usuario_db = session.query(Usuario).filter(Usuario.id == id).first()
    if usuario_db:
        session.delete(usuario_db)
        session.commit()
        return True
    return False


