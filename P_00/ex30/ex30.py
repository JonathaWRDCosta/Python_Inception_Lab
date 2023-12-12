############################################################################################
# File: ex30
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an amount in euros, 
# the current exchange rate for dollars, and then displays the converted amount in dollars.
############################################################################################

euro = float(input("Digite um valor em euro: "))
dolar = float(input("Cotação do dólar atual: "))

conversao = euro * dolar

print(f"€{euro} equivale a USD{conversao}")