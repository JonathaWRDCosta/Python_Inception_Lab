########################################################################################
# File: ex50
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter their age, calculates the birth year,
# and then displays the result.
########################################################################################

from datetime import date

ano = date.today().year

idade = int(input("Qual sua idade? "))

nascimento = ano - idade

print(f"Você nasceu em {nascimento}")