####################################################################################
# File: ex47
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an integer between 1000 and 9999,
# extracts and displays its thousands, hundreds, tens, and units digits.
####################################################################################

num = int(input("Digite um número de 1000 a 9999: "))

unidade = num % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000


print(f"Analisando o número {num}:")
print(f"Milhar: {milhar}")
print(f"Centena: {centena}")
print(f"Dezena : {dezena}")
print(f"Unidade: {unidade}")