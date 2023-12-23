##########################################################
# File: ex06.py
# Created: 2023-12-22
# Modified: 2023-12-22
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: XXX
##########################################################

soma = 0

for _ in range(1, 11):
  num = int(input(f"Digite um número {_}/10: "))
  soma += num
media = soma / 10
print(f"{media}")