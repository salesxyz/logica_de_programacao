# Importando bibliotecas (lib)
#SISTEMA DE SORTEIO 2.0
import random

lista = []

sair = False

while sair == False:
   nome_candidato = input('Digite os nomes para sorteio ou clique enter para sair: ')
   if nome_candidato !="": 
      # append - adiciona o valor da variavel dentro da lista
      lista.append(nome_candidato)
   else: 
          sair = True
escolhido = random.choice(lista)
print(f'O escolhido foi {escolhido}')


