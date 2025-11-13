from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URI = 'sqlite:///controle_usuario.db'



try:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    print('Banco conectado com sucesso')

except Exception as e:
    print('Erro ao tentar conectar com o banco')
Base = declarative_base()

Base.metadata.create_all(engine)
