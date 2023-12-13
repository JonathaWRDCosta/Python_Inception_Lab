##########################################################
# File: ex12.py
# Created: 2023-12-13
# Modified: 2023-12-13
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: XXX
##########################################################

from math import log2, log10

num = int(input("Digite um número: "))

if num < 0:
  print("Número inválido.")
else:
  base2 = log2(num)
  base10 = log10(num)
  print(f"O logaritmo de {num} na base 2 é {base2:.0f}")
  print(f"O logaritmo de {num} na base 10 é {base10:.2f}")