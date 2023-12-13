##########################################################
# File: ex09.py
# Created: 2023-12-12
# Modified: 2023-12-12
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: XXX
##########################################################

salario = float(input("Qual o salário do cliente? R$"))
prestacao = float(input("Qual o valor da prestação? R$"))

porcentagem = salario * 20 / 100

if prestacao <= porcentagem:
  print(f"20% do salário do cliente é igual a R${porcentagem:.2f} que é menor ou igual o valor da parcela R${prestacao:.2f}")
  print("Empréstimo concedido!")
else:
  print(f"20% do salário do cliente é igual a R${porcentagem:.2f} maior do que o valor da parcela R${prestacao:.2f}")
  print("Imprevimo não concedido!")