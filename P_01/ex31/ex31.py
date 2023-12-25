#########################################################################################################################
# File: ex31.py
# Created: 2023-12-24
# Modified: 2023-12-24
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter their height and weight, and then determines their fitness category.
#########################################################################################################################

altura = float(input("Qual sua altura? "))
peso = float(input("Qual o seu peso? "))

if altura < 1.20:
  if peso <= 60:
    print("Categoria A.")
  elif peso > 60 and peso <= 90:
    print("Categoria D.")
  else:
    print("Categoria G.")
elif altura >= 1.20 and altura <= 1.70:
  if peso <= 60:
    print("Categoria B.")
  elif peso > 60 and peso <= 90:
    print("Categoria E.")
  else:
    print("Categoria H.")
else:
  if peso <= 60:
    print("Categoria C.")
  elif peso > 60 and peso <= 90:
    print("Categoria F.")
  else:
    print("Categoria I.")