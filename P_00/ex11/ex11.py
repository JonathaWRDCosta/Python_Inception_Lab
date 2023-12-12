##################################################################
# File: ex11
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a speed in m/s, 
# converts it to km/h, and then displays the converted speed.
##################################################################

ms = float(input("Digite uma velocidade em m/s para converter em km/h: "))
kmh = ms * 3.6

print(f"{ms} convertidos em km/h é igual a {kmh:.2f}")