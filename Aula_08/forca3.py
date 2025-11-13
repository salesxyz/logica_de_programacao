import random
import json

with open(fr"C:\Users\VictorHugodeSalesRod\OneDrive - Sistema FIBRA\Desktop\logica_de_programacao\Aula_08\arquivo.json", 'r', encoding='utf-8') as arquivo:
    palavras = json.load(arquivo)

def tema01():
    return random.choice(palavras["tema01"])

def tema02():
    return random.choice(palavras["tema02"])

def tema03():
    return random.choice(palavras["tema03"])

def tema04():
    return random.choice(palavras["tema04"])

def tema05():
    return random.choice(palavras["tema05"])

def escolher_tema():
    print("Escolha um tema:")
    print("1 - Comidas")
    print("2 - Animais")
    print("3 - Países")
    print("4 - Cores")
    print("5 - Esportes")

    while True:
        escolha = input("Digite o número do tema escolhido: ")
        if escolha == '1':
            return tema01(), 'Comidas'
        elif escolha == '2':
            return tema02(), 'Animais'
        elif escolha == '3':
            return tema03(), 'Países'
        elif escolha == '4':
            return tema04(), 'Cores'
        elif escolha == '5':
            return tema05(), 'Esportes'
        else:
            print("Opção inválida. Tente novamente.")

def jogar_forca(): 
    palavra, tema = escolher_tema()
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

        print(f'Tema: {tema}')
        print('Palavra: ', palavra_escondida)
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
            if letra_usuario not in letras_corretas:
                print('Letra correta.')
                letras_corretas.append(letra_usuario)
            else:
                print('Você já tentou essa letra. Tente outra.')
        else:
            if letra_usuario not in letras_erradas:
                print('Letra errada!')
                letras_erradas.append(letra_usuario)
                tentativas -= 1
            else:
                print('Você já tentou essa letra errada. Tente outra.')

if __name__ == '__main__':
    print(30*'-', 'Bem-vindo ao jogo da forca', 30*'-')
    jogar_forca()