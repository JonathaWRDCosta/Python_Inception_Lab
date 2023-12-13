##########################################################
# File: ex03.py
# Created: 2023-12-12
# Modified: 2023-12-12
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: XXX
##########################################################

from math import sqrt

num = float(input("Digite um número real: "))

if num >= 0:
  raiz = sqrt(num)
  print(f"A raiz quadrada de {num} é igual a {raiz}")
else:
  print(f"O número {num} ao quadrado é igual a {num * num}")