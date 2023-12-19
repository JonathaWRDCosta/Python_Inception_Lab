##################################################################################################
# File: ex24.py
# Created: 2023-12-14
# Modified: 2023-12-14
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script calculates the total cost of a product based on the state's tax rate.
##################################################################################################

produto = float(input("Qual o valor do produto? R$"))
estado = input("Para qual estado será vendido o produto? [MG/SP/RJ/MS]: ").upper()

if estado == 'MG':
  imposto = produto + (produto * 7 / 100)
  print(f"O produto vendido para o do {estado} terá um custo total de R${imposto}")
elif estado == 'SP':
  imposto = produto + (produto * 12 / 100)
  print(f"O produto vendido para o do {estado} terá um custo total de R${imposto}")
elif estado == 'RJ':
  imposto = produto + (produto * 15 / 100)
  print(f"O produto vendido para o do {estado} terá um custo total de R${imposto}")
elif estado == 'MS':
  imposto = produto + (produto * 8 / 100)
  print(f"O produto vendido para o do {estado} terá um custo total de R${imposto}")
else:
  print("Uma ou mais informações estão erradas.")