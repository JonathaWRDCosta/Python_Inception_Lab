#######################################################################
# File: ex15
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an angle in radians, 
# converts it to degrees, and then displays the converted angle.
#######################################################################

radianos = float(input("Digite um ângulo em radiano para serem convertidos em graus: "))
graus =  radianos * 180 / 3.14

print(f"{radianos} convertidos para graus é igual a {graus:.2f}")