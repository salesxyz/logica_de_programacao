'''
import mysql
import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conexao = mysql.connector.connect(
            host='195.179.238.1',
            user='u275872813_2ds',
            password='Controlegasto25',
            database='u275872813_controle_gasto'
        )
        if conexao.is_connected():
            print('Conexao com o banco bem sucedida!')
            return conexao 
    except Error as e:
        print('Falha ao conectar com o banco!')
        return None
if __name__ == '__main__':
    get_connection()
'''



import sqlite3

def get_connet():
    try:
        conexao = sqlite3.connect('controle_produto.db')
        print('Conexao bem sucedida!')
        return conexao 
    
    except sqlite3.Error as e:
        print('Falha na conexao!', e)
        return None
    


if __name__ == '__main__':
    get_connet()