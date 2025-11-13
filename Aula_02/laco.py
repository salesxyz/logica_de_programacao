print()
print(30*'-', 'calculadora de imc', 30*'-')
'''
peso = float(input('Digite seu peso:').replace (',','.'))
altura = float(input('Digite sua altura: ').replace(',','.'))

imc = peso / (altura*altura)

if imc <= 18.5:
    print('abaixo do normal')
elif imc <= 24.9:
    print('normal')
elif imc <= 29.9:
    print ('exesso de peso')
elif imc >= 30:
    print ('obesidade')
elif imc >= 35:
    print ('obesidade II')
elif imc >= 40:
    print ('obesidade III')
'''

print()
print(30*'-', 'Elevador de carga', 30*'-')
'''
Problema 2: Um elevadro de carga possui capacidade para 200kg. Crie um programa que receba do usuario seu peso 
e o peso da carga e verifica se a carga est autorizada a usar o elevador ou nao
'''
'''
peso_usuario = float(input('Digite o seu peso em kg:'))
peso_carga = float(input('Digite o seu peso em kg:'))
peso_total = peso_carga + peso_usuario
if peso_total <= 200:
    print('Não autorizado.')
else:
    print('Autorizado.')
# Finalizado 

print()
print(30*"-",repeticao, 30*"-")
'''
print()
print(30*'-', 'Repetidores', 30*'-')
#CONT da o infinito do looping ate atingir o valor que foi especificado
#BRAKE da quebra de looping
#PASS pode ser usado em qualquer estrutura, o pass é usado em bloco vazio para ignorar o erro
#WHILE TRUE quando cria um laço infinito
#FOR Pode ser declarado varias vezes, mas possui limite, sempre executado com numero finito de vezes
'''
peso = float(input('Digite seu peso:').replace (',','.'))
altura = float(input('Digite sua altura: ').replace(',','.'))

imc = (peso/(altura*altura)) 

print()
print(f' Seu IMC e: {imc:.2f}')

if imc <= 18.5:9
    print('Abaixo do normal')
elif imc <= 24.5:
    print('Peso normal')
elif imc <= 29.5:
    print('Sobrepeso')
''' 

nome = input("Digite seu nome: ")
cpf = input("Digite seu cpf: ")
telefone = input("Digite seu telefone: ")
dt_nascimento = input("Digite sua data de nascimento: ")
print(80*'=')

while True:
 #menu principal
 print(30*'-','SISTEMA DE CONSOLE 2DS',30*'-')
 print('1 - Calculadora IMC')
 print('2 - Maioridade')
 print('3 - Calculadora')
 print('4 - Dados pessoais')
 print('5 - Feliz Natal!')
 print('6 - Sair')

 opcao = input('Digite uma opção: ')
 
 if opcao == '1':
     opcao = input('Digite uma opção: ')
     if opcao == '1':
        peso = float(input('Digite seu peso:').replace (',','.'))
        altura = float(input('Digite sua altura: ').replace(',','.'))
        imc = peso / (altura*altura)

     if imc <= 18.5:
      print('abaixo do normal')
     elif imc <= 24.9:
      print('normal')
     elif imc <= 29.9:
      print ('exesso de peso')
     elif imc >= 30:
      print ('obesidade')
     elif imc >= 35:
      print ('obesidade II')
     elif imc >= 40:
      print ('obesidade III')

 elif opcao == '2':
   dt_nascimento = int(input("Digite seu ano de nascimento: "))
   ano_atual =2025
   idade = ano_atual - dt_nascimento
   print(nome , 'é maior de idade.' if idade >=18 else 'é menor de idade')
 elif opcao == '3':
        num1 = float(input('Digite o primeiro numero: ').replace(',','.'))
        num2 = float(input('Digite o segundo numero: ').replace(',','.'))
        operador = input('Digite o operador (+, -, *, /): ')
    
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                print('Erro: Divisão por zero não é permitida.')
                
        else:
            print('Operador inválido!')
            
    
        print(f'O resultado de {num1} {operador} {num2} é: {resultado}')
 elif opcao == '4':
     print(50*'-')
     print(f'Nome: {nome} | Telefone: {telefone}  |')
     print(f'CPF: {cpf} | Data de Nascimento: {dt_nascimento} |')
     print(50*'-')

 elif opcao == '5':
     linhas = 15
     j = 1
     while j <= linhas:
         espaços = linhas - j
         estrelas = 2 * j - 1
         print(" " * espaços + "^" * estrelas)
         j +=1

 elif opcao == '6':
     print("Saindo do sistema...")
     break
  
else:
  print('Opção inválida!')

nome = 'Sales'

for i in nome:
    print(i.replace(i,'*'))