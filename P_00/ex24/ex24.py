#################################################################################
# File: ex24
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an area in square meters (m²), 
# converts it to acres, and then displays the converted area.
#################################################################################

metros = float(input("Digite valor de área de metros quadrados m² para ser convertido em acres: "))
acres = metros * 0.000247

print(f"{metros} convertidos em acres é igual a {acres}")