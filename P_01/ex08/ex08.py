#############################################################################################
# File: ex08.py
# Created: 2023-12-12
# Modified: 2023-12-12
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter two valid grades (between 0.0 and 10.0),
# calculates the average, and displays the result.
#############################################################################################

nota1 = float(input("Digite uma nota válida (0.0 - 10.0): "))
nota2 = float(input("Digite outra nota válida (0.0 - 10.0): "))

media = (nota1 + nota2) / 2

if nota1 < 0.0 or nota1 > 10.0 or nota2 < 0.0 or nota2 > 10.0:
  print("Uma ou outra nota é inválida! Uma nota válida é uma nota entre 0.0 e 10.0")
else:
  print(f"A média do aluno é de {media:.1f}!")