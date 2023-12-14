####################################################################################################
# File: ex18.py
# Created: 2023-12-14
# Modified: 2023-12-14
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script allows the user to choose an arithmetic operation (addition, subtraction, multiplication, or division)
# and performs the chosen operation based on user input.
####################################################################################################

print("Escolha uma opção:")
opcao = int(input("1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nQual a sua escolha? "))

if opcao == 1:
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite outro número: "))
  total = num1 + num2
  print(f"A soma de {num1} + {num2} é igual a: {total}")
elif opcao == 2:
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite outro número: "))
  total = num1 - num2
  print(f"A subtração de {num1} - {num2} é igual a: {total}")
elif opcao == 3:
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite outro número: "))
  total = num1 * num2
  print(f"A multiplicação de {num1} * {num2} é igual a: {total}")
elif opcao == 4:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))

    if num2 != 0:
        total = num1 / num2
        print(f"A divisão de {num1} / {num2} é igual a: {total}")
    else:
        print("Erro: Divisão por zero.")
else:
  print("Opção inválida.")