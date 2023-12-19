##############################################################################
# File: ex21.py
# Created: 2023-12-14
# Modified: 2023-12-14
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script allows the user to choose an arithmetic operation
# (addition, subtraction, multiplication, or division) and performs the chosen
# operation based on user input.
##############################################################################

print("Escolha uma opção: ")
escolha = int(input("1 - Soma de dois número.\n2 - Diferença entre dois números.\n3 - Produto entre dois números.\n4 - Divisão entre dois números.\nQual sua escolha? "))

if escolha < 1 or escolha > 4:
  print("Opção inválida.")
elif escolha == 1:
  print("Soma entre dois número:")
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite outro número: "))
  resultado = num1 + num2
  print(f"A soma entre {num1} + {num2} = {resultado}")
elif escolha == 2:
  print("Diferença entre dois números:")
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite outro número: "))
  if num1 > num2:
    diferenca = num1 - num2
    print(f"A diferença entre {num1} e {num2} = {diferenca}")
  else:
    diferenca = num2 - num1
    print(f"A diferença entre {num2} e {num1} = {diferenca}")
elif escolha == 3:
  print("Produto entre dois números:")
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite outro número: "))
  resultado = num1 * num2
  print(f"O produto de {num1} * {num2} = {resultado}")
else:
  print("Divisão entre dois números:")
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite outro número: "))
  if num2 <= 0:
    print("O denominador precisa ser maior que zero")
  else:
    resultado = num1 / num2
    print(f"A divisão de {num1} / {num2} = {resultado}")