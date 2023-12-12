###################################################################################################
# File: ex41
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter the hourly wage and the number of hours worked,
# calculates the gross pay, adds a 10% bonus, 
# and then displays the total amount to be paid.
###################################################################################################

valor_hora = float(input("Valor das horas trabalhadas: R$"))
horas_trabalhadas = int(input("Horas trabalhadas: "))

bruto = horas_trabalhadas * valor_hora

bonus = bruto + (bruto * 10 / 100)

print(f"O valor bruto total é de R${bruto} + acréscimo de 10% o total a ser pago é de R${bonus}")