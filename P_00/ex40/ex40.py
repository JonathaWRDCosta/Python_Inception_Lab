##############################################################################
# File: ex40
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter the number of days worked,
# calculates the gross pay (R$30.00 per day), applies an 8% tax deduction,
# and then displays the net pay.
##############################################################################

dias = int(input("Quantos dias trabalhados? "))
bruto = dias * 30
liquido = bruto - (bruto * 8 / 100)

print(f"O valor liquido a ser pago é de R${liquido:.2f}")