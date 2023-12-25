#########################################################################################################
# File: ex35.py
# Created: 2023-12-25
# Modified: 2023-12-25
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script takes a date as input (day, month, and year) and checks if it is a valid date.
#########################################################################################################

print("Digite uma data, primeiro dia, depois mês e depois ano.")
dia = int(input("Digite um dia: "))
mes = int(input("Digite um mês: "))
ano = int(input("Digite um ano: "))

if mes >= 1 and mes <= 12:
    if mes == 2:
        if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
            max_dias = 29 
        else:
            max_dias = 28
    elif mes in [4, 6, 9, 11]:
        max_dias = 30
    else:
        max_dias = 31

    if 1 <= dia <= max_dias:
        print(f"Data válida: {dia}/{mes}/{ano}")
    else:
        print("Número de dias inválido para o mês.")
else:
    print("Mês inválido.")
