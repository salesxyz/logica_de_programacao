import json
import os
usuarios = []
nome_arquivo= ''

limpar= lambda: os.system('cls' if  os.name== 'nt' else ' clear')

while True:
    usuario = {}
    print('1 - Cadastrar novo usuário.')
    print('2 - Salvar arquivo json.')
    print('3 - Fazer leitura do json.')
    print('4 - Sair do sistema.')

    opcao = input('informa a opção desejada: ')
    limpar()

    match opcao:
        case '1':
            usuario['nome'] = input('informa o nome: ').strip()
            usuario['idade'] = input('informe idade: ')
            usuario['email'] = input('digite o email: ').strip().lower()
            usuarios.append(usuario)
            limpar()
            print('usuario cadastrado com sucesso!')
            continue
        case '2':
            novo_arquivo = input('informe o nome do arquivo: ').strip().lower()
            
            with open(f'Aula_06/{novo_arquivo}.json', 'w', encoding='utf-8') as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            limpar()
            print('arquivo salvo com sucesso!')
            continue
        case '3':
            if not nome_arquivo:
                nome_arquivo = input('digite o nome do arquivo').strip().lower()
            with open(f'Aula_06/{nome_arquivo}.json', 'r', encoding='utf-8') as f:
                dados = json.load(f)
            print(f"{'-'*20} usuarios {'-'*20}\n")
            for usuario in dados:
                for chave in usuario:
                    print(f'{chave.capitalize()}: {usuario.get(chave)}')
                print('-'*40)
            continue
        case '4':
            print('saindo do sistema!')
            break
        case _:
            print('Opção inválida!')
            