import sqlite3 

def get_connect():
    try:
        conexao = sqlite3.connect('controle_produto.db')
        print('Conexão bem sucedida1')
        return conexao
    except sqlite3.Error as e:
        print('Falha na conexão', e)
        return None

if __name__ == '__main__':
    get_connect()