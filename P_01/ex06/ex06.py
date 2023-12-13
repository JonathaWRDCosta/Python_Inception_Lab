########################################################################################
# File: ex06.py
# Created: 2023-12-12
# Modified: 2023-12-12
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter two numbers, compares them, and
# then displays whether the first or second number is greater along with the difference.
########################################################################################

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
  print(f"O primeiro número digitado é maior {num1} e á diferença é de {num1 - num2}")
elif num1 == num2:
  print("Os números são iguais!")
else:
  print(f"O segundo número digitado é maior {num2} e a diferença entre eles é de {num2 - num1}")