#######################################################################
# File: ex12
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a distance in miles, 
# converts it to kilometers, and then displays the converted distance.
#######################################################################

milhas = float(input("Digite uma distância em milhas para converter em quilômetros: "))
quilometros = 1.61 * milhas

print(f"{milhas} convertidos em quilômetros é igual a {quilometros:.2f}")