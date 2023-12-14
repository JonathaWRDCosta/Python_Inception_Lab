#################################################################################
# File: ex16.py
# Created: 2023-12-14
# Modified: 2023-12-14
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an integer between 1 and 12,
# and then displays the corresponding month of the year.
#################################################################################

num = int(input("Digite um número inteiro entre 1 e 12: "))

match num:
  case 1:
    print("Janeiro")
  case 2:
    print("Fevereiro")
  case 3:
    print("Março")
  case 4:
    print("Abril")
  case 5:
    print("Maio")
  case 6:
    print("Junho")
  case 7:
    print("Julho")
  case 8:
   print("Agosto")
  case 9:
   print("Setembro")
  case 10:
   print("Outubro")
  case 11:
   print("Novembro")
  case 12:
    print("Dezembro")
  case _:
    print("Número inválido.")