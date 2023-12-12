############################################################################
# File: ex13
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a distance in kilometers, 
# converts it to miles, and then displays the converted distance.
############################################################################

quilometros = float(input("Digite uma distância em quilômetros para converter em milhas: "))
milhas = quilometros / 1.61

print(f"{quilometros} convertidos em milhas é igual a {milhas:.2f}")