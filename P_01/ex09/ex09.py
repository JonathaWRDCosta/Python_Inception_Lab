#########################################################################################################
# File: ex09.py
# Created: 2023-12-12
# Modified: 2023-12-12
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter the client's salary and the loan installment amount,
# calculates 20% of the salary, and then determines whether the loan is granted or not.
#########################################################################################################

salario = float(input("Qual o salário do cliente? R$"))
prestacao = float(input("Qual o valor da prestação? R$"))

porcentagem = salario * 20 / 100

if prestacao <= porcentagem:
  print(f"20% do salário do cliente é igual a R${porcentagem:.2f} que é menor ou igual o valor da parcela R${prestacao:.2f}")
  print("Empréstimo concedido!")
else:
  print(f"20% do salário do cliente é igual a R${porcentagem:.2f} maior do que o valor da parcela R${prestacao:.2f}")
  print("Imprevimo não concedido!")