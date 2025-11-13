import random
import string

def gerar_senha(comprimento=12, incluir_maiusculo=True, incluir_minusculo=True, 
                  Incluir_numeros=True, incluir_caracter=True):
    caracteres=''
    if incluir_maiusculo:
        caracteres += string.ascii_uppercase
    if incluir_minusculo:
        caracteres += string.ascii_lowercase
    if Incluir_numeros:
        caracteres += string.digits
    if incluir_caracter:
        caracteres += string.punctuation
    if not caracteres:
        return ValueError('Deve conter pelo menos um caracter')
    senha = ''.join(random.choice(caracteres) for _ in range(caracteres))
    print(f'senha:{senha}')
    return senha

def main():
    print('Gerador de Senhas Fortes')
    comprimento = int(input('Digite o comprimento daa senha(padrão é 12):')or 12)
    incluir_maiuscula = input('Incluir maiuscula (s/n, padrão = sim): ').lower() != 'n'
    incluir_minuscual = input('Incluir minuscula (s/n, padrão = sim)').lower() != 'n'
    incluir_numeros = input('Incluir números (s/n, padrão = sim )').lower() != 'n'
    incluir_simbolos = input('Incluir caracter especial (s/n, padrão = sim)').lower != 'n'
 
    senha = gerar_senha(comprimento = 12, incluir_maiusculo = True, incluir_minusculo = True, incluir_numeros = True, 
                         incluir_caracter_esp = True)

    print (f'a senha gerada foi: {senha}')

    with open('Aula08/senhas.txt', 'a') as S:
        S.write(f'\nsenha')



if __name__ == "__main__":
    main()
