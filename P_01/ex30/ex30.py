######################################################################################################
# File: ex30.py
# Created: 2023-12-19
# Modified: 2023-12-19
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter three numbers and prints them in ascending order.
######################################################################################################

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))

if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1

print("Números em ordem crescente:", num1, num2, num3)
