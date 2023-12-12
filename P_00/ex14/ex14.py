#######################################################################
# File: ex14
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an angle in degrees, 
# converts it to radians, and then displays the converted angle.
#######################################################################

graus = float(input("Digite um ângulo em graus para serem convertidos em radianos: "))
radianos = graus * 3.14 / 180

print(f"{graus} convertidos para radianos é igual a {radianos:.2f}")