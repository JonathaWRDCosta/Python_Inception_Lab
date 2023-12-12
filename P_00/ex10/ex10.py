###################################################################
# File: ex10
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a speed in km/h, 
# converts it to m/s, and then displays the converted speed.
###################################################################

kmh = float(input("Digite uma velocidade em km/h para converter em ms: "))
ms = kmh / 3.6

print(f"{kmh} convertidos em m/s é igual a {ms:.2f}")