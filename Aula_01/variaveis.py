# comentario de linha 
print('Olá mundo esse é o meu primeiro script em python')
print(30*"-","concatenando texto", 40*"-")
print('Hello world')

'''
comentario de bloco 

nome ="Vitor"
idade = 16
data_de_nascimento = 2008

print('Olá meu nome é', nome, 'tenho', idade, 'nasci em', data_de_nascimento)
'''
print()
print(30*"-","  Tipo de variaveis", 40*"-")
# Tipos de variaveis 
nome = "Sales"
idade = 16
altura = 1.72
ativo = True

print("O tipo da variavel nome é:", type(nome))
print("O tipo da variavel idade é:", type(idade))
print("O tipo da variavel altura é:", type(altura))
print("O tipo da variavel ativo é:", type(ativo))

print()
print(30*"-","Operadores", 40*"-")
# Operadores
num1 = 5
num2 = 6 

soma = num1 + num2
divi = num1 / num2
mult = num1 * num2
sub = num1 - num2
resto = num1 %2
expo = num1 ** num2

print("O resultado da soma", num1 ,"+", num2, "é:", soma)
print('O resultado da divisão', num1, "/", num2, 'é:', divi)
print("O resultado da multiplicação", num1, "*", num2, "é:", mult)
print("O resultado da subtração", num1, "-", num2, "é:", sub)
print("O resultado do resto", num1, "%","é", resto)
print("O resultado da exponenciação", num1, "**", num2, "é:", expo)

print()
print(30*"-","Operadores de comparação", 40*"-")
#Operadores de comparação
num1 == num2
num1 >= num2
num1 <= num2
num1 != num2

ano = 2025
print("Ano atual", ano)
ano +=1 
print ("Ano acrecido de +1", ano)
ano -=1 
print ("Ano decrecido de -1", ano)

# Operadores lógicos
#AND, OR, NOT

print()
print(30*"-","entrada de dados", 40*"-")

#nome_usuario = input("Digite o seu nome: ")
#print('seja bem-vindo ao sistema python', nome_usuario)

print()
print(30*"-","Calculadora Simples", 40*"-")
 # O "INPUT" por padrão é um 'STR' (conjunto de caracteres), não dando para somar.
# numero1 = int(input('Digite o primeiro numero: '))
# numero2 = int(input('Digite o segundo numero: '))

# soma = numero1 + numero2
# divi = numero1 / numero2
# mult = numero1 * numero2
# sub = numero1 - numero2

# print("O resultado da soma", numero1 ,"+", numero2, "é:", soma)
# print('O resultado da divisão', numero1, "/", numero2, 'é:', divi)
# print("O resultado da multiplicação", numero1, "*", numero2, "é:", mult)
# print("O resultado da subtração", numero1, "-", numero2, "é:", sub)


#TIPOS DE DADOS
# FLOAT = numeros reais, ou seja, tem ",", exemplo: 5.20
# INT = numeros inteiros
# STR = textos, conjunto de caracteres
# BOOl = valores logicos como TRUE e FALSE

print()
print(30*"-","Convertendo tipos de dados", 40*"-")


ano_nascimento = input('Digite seu ano de nascimento ')

#Convertendo para inteiro 
ano_nascimento = int(ano_nascimento)
print (type(ano_nascimento))

n1 = 10
n2 = 20

print('A soma é:', n1 + n2, type(n1), float(n2))

saudacao = input('Digite seu nome: ')
cpf = input('Digite seu CPF: ')
telefone = input('Digite seu telefone: ')

print(20*"-",'Dados pessoai', 20*'-')
print('Nome: ', saudacao)
print('CPF:', cpf, "| Telefone: ",telefone)
print(50*'-')   