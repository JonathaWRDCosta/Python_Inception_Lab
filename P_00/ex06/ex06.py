############################################################################
# File: ex06
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a temperature in Celsius, 
# converts it to Fahrenheit, and then displays the converted temperature.
############################################################################

celsius = float(input("Digite uma temperatura em graus Celsius para converter em Fahrenheit: "))
fahrenheit = celsius * (9.0 / 5.0) + 32

print(f"{celsius} convertido em Fahrenheit é igual a {fahrenheit}")
