#######################################################################
# File: ex20
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a mass in kilograms, 
# converts it to pounds, and then displays the converted mass.
#######################################################################

quilograma = float(input("Digite um valor de massa em quilogramas para ser convertido em libras: "))
libras = quilograma / 0.45

print(f"{quilograma} convertido em libras é igual a {libras:.2F}")
