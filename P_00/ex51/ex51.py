###################################################################################################
# File: ex51
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter coordinates (x, y), calculates the distance
# from the origin to the point using the Euclidean distance formula, and then displays the result.
###################################################################################################

from math import sqrt

x = int(input("Digite coordenada 1: "))
y = int(input("Digite coordenada 2: "))

distancia = sqrt((x * x) + (y * y))

print(f"A distância da origem ao ponto P ({x}, {y}) é {distancia:.0f} unidades")