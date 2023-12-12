#######################################################################
# File: ex45
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an uppercase letter,
# converts it to lowercase using the ASCII values, 
# and then displays the result.
#######################################################################

letra = input("Digite uma letra maiúscula: ")

conversao = chr(ord(letra) + 32)

print(conversao)