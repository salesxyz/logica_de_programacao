'''
Programa: Contagem regressiva
Importanto bibliotecas 
Aula 04: 19/08/25
'''
# importando bibliotecas (lib)
import os 
from time import sleep 

cont = input('Digite um numero inteiro: ')


try:
    cont_int = int(cont)
    while cont_int >=0:
     print(f'contagem regressiva: {cont_int}...')
     sleep(1)
     cont_int -= 1
     os.system('cls')
                         
except:
    print('Digite um numero valido!')

print('Fim da contagem!')
