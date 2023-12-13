##########################################################
# File: ex02.py
# Created: 2023-12-12
# Modified: 2023-12-12
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: XXX
##########################################################

from math import sqrt

num = int(input("Digite um número: "))

if num >= 0:
  raiz = sqrt(num)
  print(f"A raiz quadrada de {num} é igual a {raiz}")
else:
  print("O número é inválido, digite um número positivo.")