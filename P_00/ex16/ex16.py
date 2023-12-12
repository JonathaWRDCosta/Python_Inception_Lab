######################################################################
# File: ex16
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a length in inches, 
# converts it to centimeters, and then displays the converted length.
######################################################################

polegadas = float(input("Digite comprimento em polegadas para ser convertido em centímetros: "))
centimetros = polegadas * 2.54

print(f"{polegadas} convertidos em centímetros é igual a  {centimetros:.2f}")