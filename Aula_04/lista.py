#IN: Encotra valores dentro da lista
#EXECEPT : Utilizado para fazer tratamento de erros
#COUNT: Conta a quantidade de vezes que un valor que foi encontrado
#RANGE: Gerar numeros
'''
nome_lista = ('Fulano' , 'Ciclano' , 'Beltrano', 'Joana', 'Maria', 'Mariana', 'Fulano')

for i in range(len(nome_lista)):
    print(f'(i +1)º nome da lista: {nome_lista[i]}')

nome = input('Informe o noem que deseja encotrar: ')

quantidade = nome_lista.count(nome)

try: 
    print(f'{nome} foi encontrado na lista {quantidade} vezes.')
except: 
      prit(f'{nome} nao foi encontrado')
'''
'''
nome_lista[0] = 'Alex'

for nome in nome_lista:
    print(nome)
'''
'''
nome_lista = ('Fulano' , 'Ciclano' , 'Beltrano', 'Joana', 'Maria', 'Mariana', 'Fulano')
nome_a_alterar = input('Informe o nome que deseja alterar : ')
nome_lista[nome_a_alterar.index(nome_a_alterar)] = input('Informe o novo nome: ')

for nome in nome_lista:
    print(nome)
'''
#TABUADA

numero = int(input('Digite o numero: '))

for i in  range(1 , 11):
    resultado = numero * i
    print(f'{i} X {numero} = {resultado}')
