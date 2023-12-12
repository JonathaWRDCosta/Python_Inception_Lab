#####################################################################
# File: ex22
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a length in yards, 
# converts it to meters, and then displays the converted length.
#####################################################################

jardas = float(input("Digite um valor de comprimento em jardas para converter em metros: "))
metros = 0.91 * jardas

print(f"{jardas} convertido em metros é igual a {metros}")