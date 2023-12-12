##################################################################################
# File: ex46
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an integer between 100 and 999,
# extracts and displays its units, tens, and hundreds digits.
##################################################################################

num = int(input("Digite um número inteiro de 100 a 999: "))
unidade = num % 10
dezena = (num // 10) % 10
centena = num // 100

print(f"{unidade}{dezena}{centena}")