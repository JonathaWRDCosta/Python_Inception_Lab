###########################################################################
# File: ex17
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a length in centimeters, 
# converts it to inches, and then displays the converted length.
###########################################################################

centimetros = float(input("Digite comprimento em centímetros para ser convertido em polegadas: "))
polegadas = centimetros / 2.54

print(f"{centimetros} convertidos em polegadas é igual a  {polegadas:.2f}")