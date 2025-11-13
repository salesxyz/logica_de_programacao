#Importando Bibliotecas (lib)
import random

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o Segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto numero: ')
nome5 = input('Digite o quinto numero: ')

lista_nomes = [nome1 , nome2, nome3, nome4, nome5]

escolhido = random.choice(lista_nomes)
print(f'O escollhido foi {escolhido}')
