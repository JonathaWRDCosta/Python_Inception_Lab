################################################################################
# File: ex15.py
# Created: 2023-12-13
# Modified: 2023-12-13
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an integer between 1 and 7,
# and then displays the corresponding day of the week.
################################################################################

num = int(input("Digite um número inteiro entre 1 e 7: "))

match num:
  case 1:
    print("Domingo")
  case 2:
    print("Segunda-Feira")
  case 3:
    print("Terça-Feira")
  case 4:
    print("Quarta-Feira")
  case 5:
    print("Quinta-Feira")
  case 6:
    print("Sexta-Feira")
  case 7:
    print("Sábado")
  case _:
    print("Número inválido.")