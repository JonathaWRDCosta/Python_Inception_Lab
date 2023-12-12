############################################################################
# File: ex09
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a temperature in Celsius, 
# converts it to Kelvin, and then displays the converted temperature.
############################################################################

celsius = float(input("Digite uma temperatura em graus Celsius para converter em Kelvin: "))
kelvin = celsius + 273.15

print(f"{celsius} convertido em Kelvin é igual a {kelvin:.2f}")
