##############################################################################################
# File: ex04.py
# Created: 2023-12-12
# Modified: 2023-12-12
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an integer, checks if it is non-negative,
# and then calculates and displays the square and square root of the entered number.
##############################################################################################

from math import sqrt, pow

num = int(input("Digite um número: "))

if num >= 0:
  pot = pow(num, 2)
  raiz = sqrt(num)
  print(f"O número {num} ao quadrado é igual a {pot}")
  print(f"A raiz quadrada de {num} é igual a {raiz:.3f}")
else:
  print("Número inválido, digite um número positivo.")