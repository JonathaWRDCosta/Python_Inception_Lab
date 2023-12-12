###########################################################################
# File: ex08
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a temperature in Kelvin, 
# converts it to Celsius, and then displays the converted temperature.
###########################################################################

kelvin = float(input("Digite uma temperatura em graus Kelvin para converter em Celsius: "))
celsius = kelvin - 273.15

print(f"{kelvin} convertido em Celsius é igual a {celsius:.2f}")
