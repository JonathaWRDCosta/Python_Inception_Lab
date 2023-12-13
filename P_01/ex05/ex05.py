############################################################################################""
# File: ex05.py
# Created: 2023-12-12
# Modified: 2023-12-12
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an integer, checks if it is even or odd,
# and then displays the result.
############################################################################################""

num = int(input("Digite um número: "))

if num % 2 == 0:
  print(f"O número {num} é par!")
else:
  print(f"O número {num} é ímpar!")