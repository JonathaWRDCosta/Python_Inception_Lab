#################################################################################
# File: ex26
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an area in square meters (m²), 
# converts it to hectares, and then displays the converted area.
#################################################################################

metros = float(input("Digite um valor de área em metros quadrados m² para ser convertido hectares: "))
hectares = metros * 0.0001

print(f"{metros} convertidos em hectares é igual a {hectares:.2f}")