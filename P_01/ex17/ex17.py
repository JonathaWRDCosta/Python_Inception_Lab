##################################################################################
# File: ex17.py
# Created: 2023-12-14
# Modified: 2023-12-14
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script calculates the area of a trapezoid based on user input.
##################################################################################

print("=====Vamos calcular a área de um Trapézio=====")
base1 = float(input("Base maior: "))
base2 = float(input("Base menor: "))
altura = float(input("Altura: "))

if base1 < 0 or base2 < 0:
  print("Base maior e a base menor devem ser maior do que zero")
else:
  resultado = ((base1 + base2) * altura) / 2
  print(f"A área do trapézio é de {resultado}")