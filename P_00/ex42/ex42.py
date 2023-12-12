###########################################################################
# File Name: ex42
# Created on: 2023-12-11
# Author: Jonatha Costa
# Email: jonathawiliamsrdcosta@gmail.com
#
# Description: 
# This script prompts the user to enter the base salary of an employee,
# calculates a 5% bonus, a 7% discount, and then displays the total amount.
###########################################################################


salario_base = float(input("Insira o salário base do funcionário: R$"))

bonus = salario_base * 5 / 100
desconto = salario_base * 7 / 100
total = salario_base + bonus - desconto

print(f"Bonus: R${bonus:.2f}")
print(f"Desconto: R${desconto:.2f}")
print(f"Valor total: R${total:.2f}")