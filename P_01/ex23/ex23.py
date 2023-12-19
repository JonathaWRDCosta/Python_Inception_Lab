#################################################################
# File: ex23.py
# Created: 2023-12-14
# Modified: 2023-12-14
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script checks if a given year is a leap year.
#################################################################

ano = int(input("Digite um ano para saber se é um ano bissexto: "))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
  print(f"O ano {ano} é bissexto")
else:
  print(f"O ano {ano} não é bissexto")