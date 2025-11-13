from sqlalchemy import Column, Interger, String
from passlib.hash import pbkdf2_sha256 as sha256
from connection import Base

class Usuario(Base):
   

    #Construtor: quando quero usar os atributos para novos valores
    def __init__(self,nome, email, senha):
        self.__nome = nome
        self.__email= email
        self.__senha = senha
    
    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, email):
        self.__email = email
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha




    __tablename__ = 'USUARIO'

    id = Column (Interger, primary_key=True, autoincrement=True)
    nome = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    

     
    

    def gen_senha(self, senha):
        return sha256.hash(senha)
    
    def verificar_Senha(self, senha):
        return sha256.verify(senha)



