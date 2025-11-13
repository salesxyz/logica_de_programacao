# Função comum usando return
def soma(a, b):
    return a + b

resultado = soma(2, 3)
print("Resultado com return:", resultado)

# Função geradora usando yield
def contador():
    for i in range(3):
        yield i

print("Usando yield e next:")
for valor in contador():
    print(valor)

#Função repulsiva