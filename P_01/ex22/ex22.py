###################################################################################################################
# File: ex22.py
# Created: 2023-12-14
# Modified: 2023-12-14
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script checks if a person is eligible for retirement based on age and years of work experience.
###################################################################################################################

idade = int(input("Qual sua idade? "))
tempo_trabalho = int(input("Quanto tempo de trabalho? "))

if idade >= 60 and tempo_trabalho >= 25:
  print("Sim, pode se aposentar por ser maior de 60 anos e ter um tempo de trabalho maior que 25.")
elif tempo_trabalho >= 30:
  print("Sim, pode se aposentar por tempo de trabalho maior que 30 anos.")
elif idade >= 65:
  print("Sim, pode se aposdentar por ter idade mínima de 65 anos.")
else:
  print("Não pode se aposentar.")