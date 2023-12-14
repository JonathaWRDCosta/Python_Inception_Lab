#############################################################################################
# File: ex19.py
# Created: 2023-12-14
# Modified: 2023-12-14
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script checks whether a given number is divisible by 3, by 5, or by both.
#############################################################################################

num = int(input("Digite um número: "))

if num % 3 == 0 and num % 5 == 0:
  print(f"{num} é divisível por 3 e por 5 ao mesmo tempo.")
elif num % 3 == 0:
  print(f"{num} é divisível por 3 mas não por 5")
elif num % 5 == 0:
  print(f"{num} é divisível por 5 mas não por 3")