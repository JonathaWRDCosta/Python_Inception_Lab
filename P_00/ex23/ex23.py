######################################################################
# File: ex23
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a length in meters, 
# converts it to yards, and then displays the converted length.
######################################################################

metros = float(input("Digite um valor de comprimento em metros para converter em jardas: "))
jardas = metros / 0.91

print(f"{metros} convertido em jardas é igual a {jardas}")