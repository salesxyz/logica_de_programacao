import os

Sala1 = 'Doutor estranho'
idade1 = 14
Sala2 = 'Lego filme'
idade2 = 12
Sala3 = 'Advogado do Diabo'
idade3 = 16
Sala4 = 'Invocação do mal 6'
idade4 = 18
Sala5 = 'Batman'
idade5 = 14

while True:
    print('Bem vindo ao cinema!')
    print('Escolha uma das opções de filmes abaixo:')
    print(f'1 - {Sala1} | classificação: {idade1} anos')
    print(f'2 - {Sala2} | classificação: {idade2} anos')
    print(f'3 - {Sala3} | classificação: {idade3} anos')
    print(f'4 - {Sala4} | classificação: {idade4} anos')
    print(f'5 - {Sala5} | classificação: {idade5} anos')

    try:
        opcao = int(input('Digite o número do filme que deseja assistir: '))
        idade = int(input('Digite sua idade: '))
    except ValueError:
        print('Por favor, digite números válidos.')
        continue

    if opcao == 1:
        if idade >= idade1:
            print(f'Aproveite o filme {Sala1}')
        else:
            print('Você não tem idade suficiente para assistir esse filme.')
    elif opcao == 2:
        if idade >= idade2:
            print(f'Aproveite o filme {Sala2}')
        else:
            print('Você não tem idade suficiente para assistir esse filme.')
    elif opcao == 3:
        if idade >= idade3:
            print(f'Aproveite o filme {Sala3}')
        else:
            print('Você não tem idade suficiente para assistir esse filme.')
    elif opcao == 4:
        if idade >= idade4:
            print(f'Aproveite o filme {Sala4}')
        else:
            print('Você não tem idade suficiente para assistir esse filme.')
    elif opcao == 5:
        if idade >= idade5:
            print(f'Aproveite o filme {Sala5}')
        else:
            print('Você não tem idade suficiente para assistir esse filme.')
    else:
        print('Opção inválida. Por favor, escolha um número de 1 a 5.')

    sair = input('Deseja sair do sistema? (s/n): ').strip().lower()
    if sair == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        break
