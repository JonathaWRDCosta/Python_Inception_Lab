################################################################################
# File: ex25.py
# Created: 2023-12-14
# Modified: 2023-12-14
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script solves a quadratic equation (ax^2 + bx + c = 0) and prints the solutions.
################################################################################

import cmath

num1 = float(input("Digite o coeficiente A: "))
num2 = float(input("Digite o coeficiente B: "))
num3 = float(input("Digite o coeficiente C: "))

delta = num2**2 - 4*num1*num3

solucao1 = (-num2 + cmath.sqrt(delta)) / (2 * num1)
solucao2 = (-num2 - cmath.sqrt(delta)) / (2 * num1)

print(f"Solução 1: {solucao1}")
print(f"Solução 2: {solucao2}")
