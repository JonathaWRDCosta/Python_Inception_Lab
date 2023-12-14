################################################################################################################
# File: ex20.py
# Created: 2023-12-14
# Modified: 2023-12-14
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script checks if three given values can form a triangle and determines the type of triangle.
################################################################################################################

print("Me de três valores e eu verificarei se pode formar um tri|angulo e qual tipo de triângulo.")
num1 = int(input("Digite um valor A: "))
num2 = int(input("Digite um valor B: "))
num3 = int(input("Digite um valor C: "))

if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
  print("Forma triângulo.")
  if num1 == num2 == num3:
    print("Triângulo Equilátero.")
  elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Triângulo Isósceles.")
  else:
    print("Triângulo Escaleno.")
else:
  print("Não formam um triângulo...")