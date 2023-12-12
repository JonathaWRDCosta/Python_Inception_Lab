########################################################################
# File: ex38
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an employee's salary, 
# calculates the new salary with a 25% increase, 
# and then displays the result.
########################################################################

salario = float(input("Digite o valor do salário de um funcionário: R$"))
aumento = salario + (salario * 25 / 100)

print(f"Um funcionário que recebia R${salario} passará a receber R${aumento} com 25% de aumento.")