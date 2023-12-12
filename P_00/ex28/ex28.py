####################################################################
# File: ex28
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter three values, 
# calculates the sum of their squares, and then displays the result.
####################################################################

num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
num3 = int(input("Digite mais um valor: "))

res = (num1 * num1) + (num2 * num2) + (num3 * num3)

print(f"A soma dos quadrados dos números digitados é igual a {res}")