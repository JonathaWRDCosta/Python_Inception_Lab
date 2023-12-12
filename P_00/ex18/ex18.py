#################################################################################
# File: ex18
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a volume in cubic meters (m³), 
# converts it to liters, and then displays the converted volume.
#################################################################################

metros = float(input("Digite um valor de volume em metros cúbicos (m³) para ser convertido em litros: "))
litros = 1000 * metros

print(f"{metros} convertidos em litros é igual a {litros}")
