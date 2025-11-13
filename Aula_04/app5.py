'''



'''
#Importando lib
from random import randint


print('Tente advinhar o numero!')
num1 = int(input('Digite um numero: '))

num_secreto = randint(1, 10)

if num1 == num_secreto:
    print('Parabens você venceu!')
else: 
    print('Você perdeu')
    print(F'O numero correto é {num_secreto}')
