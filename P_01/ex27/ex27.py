####################################################################
# File: ex27.py
# Created: 2023-12-16
# Modified: 2023-12-16
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script classifies a swimmer into age categories.
####################################################################

idade = int(input("Qual a idade do naddador? "))

if idade >= 1 and idade < 5:
  print("Idade não tem classificação adequada.")
elif idade >= 5 and idade <= 7:
  print("Nadador classe Infantil A.")
elif idade >= 8 and idade <= 10:
  print("Nadador classe Infantil B.")
elif idade >= 11 and idade <= 13:
  print("Nadador classe Juvenil A.")
elif idade >= 14 and idade <= 17:
  print("Nadador classe Juvenil B.")
elif idade >= 18:
  print("Nadador classe Sênior.")
else:
  print("Idade não válida.")