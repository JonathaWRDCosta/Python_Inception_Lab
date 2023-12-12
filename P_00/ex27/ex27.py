##########################################################################
# File: ex27
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an area in hectares, 
# converts it to square meters (m²), and then displays the converted area.
##########################################################################

hectares = float(input("Digite um valor de área em hectares para ser convertido em metros quadrados m²: "))
metros =  hectares * 10000

print(f"{hectares} convertidos em hectares é igual a {metros:.2f}")