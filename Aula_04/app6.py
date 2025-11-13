
import random 
import time 
import os
secret_number = random.randint(1, 100)
tentativas = 0
max_tentativas = 10
acertou = False

print(30*'_', 'bem vindo ao jogo', 30*'_')

print(f'voce tem {max_tentativas} tentativas para acertar o numero secreto entre 1 e 100')
print('vamos comecar?')

while tentativas < max_tentativas:
    
    try:
        palpite = int(input('Digite seu palpite: '))
        tentativas += 1

        if palpite == secret_number:
            acertou = True
            break
        elif palpite < secret_number:
    
            print('Muito baixo!')
        else:
        
            print('Muito alto!')
    except ValueError:
        print('Por favor, digite um número válido.')

if acertou:
    print(f'Parabéns! Você acertou o número secreto {secret_number} em {tentativas} tentativas.')
else:
    print(f'Você não acertou o número secreto {secret_number} em {max_tentativas} tentativas.')