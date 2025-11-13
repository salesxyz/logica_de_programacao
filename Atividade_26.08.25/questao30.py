#ARRUMAR A TABUADA
x = int(input("Digite o numero da tabuada: "))
for num in range(1, 11):
  resultado = x * num
  print(f'{x} X  {num} = {resultado}')
