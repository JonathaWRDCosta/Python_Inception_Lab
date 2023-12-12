####################################################################
# File: ex21
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a mass in pounds, 
# converts it to kilograms, and then displays the converted mass.
####################################################################

libras = float(input("Digite um valor de massa em libras para ser convertido em quilogramas: "))
quilograma =  libras * 0.45

print(f"{libras} convertido em quilogramas é igual a {quilograma:.2F}")
