###################################################################################################
# File: ex13.py
# Created: 2023-12-13
# Modified: 2023-12-13
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter three grades, calculates the weighted average,
# and then displays whether the student is approved or not based on a threshold of 60.
###################################################################################################

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = ((nota1 * 1) + (nota2 * 1) + (nota3 * 2)) / 4

if media >= 60:
  print(f"A média do aluno foi de {media} por tanto...")
  print("APROVADO!")
else:
  print(f"A média do aluno foi de {media} por tanto...")
  print("Reprovado! Estude mais!")