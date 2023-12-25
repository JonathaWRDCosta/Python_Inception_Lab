##########################################################################################################################################
# File: ex33.py
# Created: 2023-12-24
# Modified: 2023-12-24
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script calculates the new price of a product based on its original price, applies different percentage increases according to predefined ranges, and categorizes the product as "BARATO" (CHEAP), "NORMAL" (NORMAL), "CARO" (EXPENSIVE), or "MUITO CARO" (VERY EXPENSIVE).
##########################################################################################################################################

produto = float(input("Qual o valor do produto? R$"))

if produto < 50.00:
  aumento = produto + (produto * 5 / 100)
  print(f"O novo valor do produto é R${aumento:.2f}")
  if aumento <= 80.00:
    print("De acordo com a tabela, se enquadra em BARATO!")
  elif aumento > 80.00 and aumento <= 120.00:
    print("De acordo com a tabela, se enquadra em NORMAL!")
  elif aumento > 120.00 and aumento <= 200:
    print("De acordo com a tabela, se enquadra em CARO!")
  else:
    print("De acordo com a tabela, se enquadra em MUITO CARO!")

elif produto >= 50.00 and produto <= 100.00:
  aumento = produto + (produto * 10 / 100)
  print(f"O novo valor do produto é R${aumento:.2f}")
  if aumento <= 80.00:
    print("De acordo com a tabela, se enquadra em BARATO!")
  elif aumento > 80.00 and aumento <= 120.00:
    print("De acordo com a tabela, se enquadra em NORMAL!")
  elif aumento > 120.00 and aumento <= 200:
    print("De acordo com a tabela, se enquadra em CARO!")
  else:
    print("De acordo com a tabela, se enquadra em MUITO CARO!")

elif produto > 100.00:
  aumento = produto + (produto * 15 / 100)
  print(f"O novo valor do produto é R${aumento:.2f}")
  if aumento <= 80.00:
    print("De acordo com a tabela, se enquadra em BARATO!")
  elif aumento > 80.00 and aumento <= 120.00:
    print("De acordo com a tabela, se enquadra em NORMAL!")
  elif aumento > 120.00 and aumento <= 200:
    print("De acordo com a tabela, se enquadra em CARO!")
  else:
    print("De acordo com a tabela, se enquadra em MUITO CARO!")