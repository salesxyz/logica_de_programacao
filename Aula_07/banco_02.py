import os

class Conta:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.saldo = 0.0
        self.ativa = True
        self.cpf = cpf

def menu():
    print("Escolha a opção que deseja usar:")
    print("1 - Criar conta")
    print("2 - Exibir dados")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Encerrar")
    print("6 - Sair")
    return input("Função: ")

def criar_conta():
    nome = input("Digite seu nome completo: ")
    cpf = input("Digite seu CPF ou RG: ")
    return Conta(nome, cpf)

def exibir_dados(conta):
    print(f"Nome: {conta.nome}, \nCPF: {conta.cpf}, \nSaldo: R${conta.saldo:.2f}, \nAtiva: {conta.ativa}")

def depositar(conta):
    v = float(input("Valor depósito: "))
    conta.saldo += v
    print(f"Depósito realizado. Novo saldo: R${conta.saldo:.2f}")

def sacar(conta):
    v = float(input("Valor saque: "))
    if v <= conta.saldo:
        conta.saldo -= v
        print(f"Saque realizado. Novo saldo: R${conta.saldo:.2f}")
    else:
        print("Saldo insuficiente.")

def encerrar(conta):
    conta.ativa = False
    print("Conta encerrada.")

conta = None

while True:
    op = menu()
    if op == '1':
        conta = criar_conta()
        print("Conta criada.")
    elif op == '2' and conta:
        exibir_dados(conta)
    elif op == '3' and conta and conta.ativa:
        depositar(conta)
    elif op == '4' and conta and conta.ativa:
        sacar(conta)
    elif op == '5' and conta:
        encerrar(conta)
    elif op == '6':
        os.system('cls')
        break
    else:
        print("Opção inválida ou conta inexistente.")