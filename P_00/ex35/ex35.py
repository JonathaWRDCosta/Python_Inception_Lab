############################################################################################
# File: ex35
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter the two legs of a right-angled triangle, 
# calculates the hypotenuse, and then displays the result.
############################################################################################

import math

a = int(input("Digite o cateto de um triângulo: "))
b = int(input("Digite outro cateto do triângulo: "))

sqrt = math.sqrt(a**2 + b**2)

print(f"O valor da hipotenusa é {sqrt}")