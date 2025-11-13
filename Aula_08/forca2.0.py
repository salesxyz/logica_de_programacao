#bibliotecas usadas no código
import random
import os

# Temas e palavras
def tema01():

    comidas = ['pizza', 'hamburguer', 'sushi', 'churrasco', 'salada', 'lasanha', 'tacos', 'paella', 'curry', 'ramen', 
               'pasta', 'sorvete', 'bolo', 'pudim', 'crepe', 'mousse', 'fondue', 'tapioca', 'brigadeiro', 'coxinha',
               'empada','bobó de camarao', 'escondidinho', 'farofa', 'tapioca', 'pao de queijo', 'churrasco', 'baiao de dois',
                 'arroz carreteiro', 'dobradinha', 'canjica', 'curau', 'pe de moleque', 'paçoca', 'arroz doce']
    return random.choice(comidas)

def tema02():
    animais = ['leao', 'tigre', 'elefante', 'girafa', 'zebra', 'canguru', 'panda', 'urso', 'lobo', 'raposa',
               'coelho', 'tartaruga', 'jacare', 'crocodilo', 'hipopotamo', 'rinoceronte', 'bufalo', 'antilope',
               'guepardo', 'chita', 'hiena']
    return random.choice(animais)
def tema03():
    paises = ['brasil', 'argentina', 'chile', 'colombia', 'peru', 'venezuela', 'uruguai', 'paraguai', 'bolivia',
              'equador', 'guiana', 'suriname', 'frança', 'espanha', 'portugal', 'italia', 'alemanha', 'frança',
              'inglaterra', 'irlanda', 'escocia', 'gales']
    return random.choice(paises)
def tema04():
    cores = ['vermelho', 'azul', 'verde', 'amarelo', 'laranja', 'roxo', 'rosa', 'marrom', 'cinza', 'preto',
             'branco', 'dourado', 'prateado', 'turquesa', 'violeta', 'magenta', 'ciano', 'bege', 'lilas',]
    return random.choice(cores)
def tema05():
    esportes = ['futebol', 'basquete', 'volei', 'tenis', 'natacao', 'corrida', 'ciclismo', 'boxe', 'judo',
               'karate', 'taekwondo', 'ginastica', 'surf', 'skate', 'esgrima', 'rugby', 'criquete',
               'hoquei', 'golf', 'beisebol', 'handebol']
    return random.choice(esportes)

#MENU de escolha do tema
def escolher_tema():
    print("Escolha um tema:")
    print("1 - Comidas")
    print("2 - Animais")
    print("3 - Países")
    print("4 - Cores")
    print("5 - Esportes")
 #Laço para garantir que o usuário escolha um tema válido
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
#Estrutura principal do jogo
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
        print('Palavra: ',palavra_escondida)
        print('Letras erradas: ', letras_erradas)
        print('Tentativas restantes: ', tentativas)
            #Verifica se o jogador ganhou ou perdeu
        if palavra_escondida == palavra:
            print('Parabéns você ganhou!')
            break
        elif tentativas == 0:
            print('Você perdeu! A palavra era:', palavra)
            break

        letra_usuario = input('Digite uma letra: ').lower()
          #Verifica se a letra já foi tentada
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
                print('Você já tentou essa letra. Tente outra.')
if __name__ == '__main__':
      os.system('cls')
      print(30*'-', 'Bem-vindo ao jogo da forca', 30*'-')
jogar_forca()

#Fim do código