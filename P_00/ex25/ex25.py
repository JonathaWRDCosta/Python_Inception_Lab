##########################################################################
# File: ex25
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an area in acres, 
# converts it to square meters (m²), and then displays the converted area.
##########################################################################

acres = float(input("Digite valor de área em acres para ser convertido em metros quadrados m²: "))
metros =  acres * 4048.58

print(f"{acres} convertidos em acres é igual a {metros:.2f}")