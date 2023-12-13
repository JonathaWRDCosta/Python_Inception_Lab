################################################################################################
# File: ex11.py
# Created: 2023-12-12
# Modified: 2023-12-12
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a number greater than 0 and less than 1000,
# calculates the sum of its digits, and then displays the result.
################################################################################################
num = int(input("Digite um número maior que 0 e menor que 1000: "))

unidade = num % 10
dezena = (num // 10) % 10
centena = num // 100
total = unidade + dezena + centena

if num < 0:
  print("Número inválido!")
else:
  print(f"Número digitado {num} e seu algarismo é {total}")