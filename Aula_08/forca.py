import random
import os

def escolher_palavra():
    palavras = ['python', 'developer', 'programação', 'inteligencia artificial', 'algoritmo', 'computador', 'java', 'linguagens de programação',
             'desenvolvimento', 'software', 'hardware', 'rede', 'internet', 'banco de dados', 'sistema operacional', 'escova', 'caderno',
             'mesa', 'cadeira', 'monitor', 'teclado', 'mouse', 'celular', 'tablet', 'notebook', 'impressora', 'webcam', 'telescópio', 'otorrinolaringologista',
               'estetoscópio', 'anel', 'odontologia', 'engenheiro', 'garrafa', 'incorreto', 'ornintorrinco','abacaxi', 'computador', 'carambola', 'própolis', 'chocolate', 'pistache', 'colorir', '' ]

    return random.choice(palavras).lower()

def jogar_forca(): 
    palavra = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6

    while True:
        palavra_escondida = ''
        for letra in palavra:
            if letra in letras_corretas:
                palavra_escondida += letra
            else: 
                palavra_escondida += '_'

        print('Palavra: ',palavra_escondida)
        print('Letras erradas: ', letras_erradas)
        print('Tentativas restantes: ', tentativas)

        if palavra_escondida == palavra:
            print('Parabéns você ganhou!')
            break
        elif tentativas == 0:
            print('Você perdeu! A palavra era:', palavra)
            break

        letra_usuario = input('Digite uma letra: ').lower()

        if letra_usuario in palavra:
            print('Letra correta.')
            letras_corretas.append(letra_usuario)

        else:
            print('Letra errada!')
            letras_erradas.append(letra_usuario)
            tentativas -= 1
            

if __name__ == '__main__':
    os.system('cls')
    print(30*'-', 'Bem-vindo ao jogo da força', 30*'-')
    jogar_forca()

