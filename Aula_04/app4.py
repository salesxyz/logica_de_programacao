#Importando lib
#SISTEMA DE SORTEIO 3.0

import random
import os 
import time

lista_nomes = []
lista_sorteados= []

while True:
    nome = input('Digite o nome para o sorteio: ')
    lista_nomes.append(nome)
 
   
    if lista_nomes:
        os.system("cls")
        escolhido = random.choice(lista_nomes)
        lista_sorteados.append(escolhido)

        print(f'O escolhido foi: {escolhido}')
    opcao = input('Deseja sortear outro nome? S- Sim \n| N- Não \n: ').lower()
    os.system('cls')

    if opcao !='S':
     break
    else:
       print("Não a mais nomes para sortear")
print('Program finalizado!')
print(f'Os sorteados foram{lista_sorteados}')


'''
POP - função, remove pelo indice
 pop() - remover o ultimo indice
 pop(0) - remove o indice 0
  
DEL- instrução, remover item pelo indice, mais de um item
  del[1:10]

REMOVE - remove a partir de uma variavel
  lista.remove(variavel)

'''