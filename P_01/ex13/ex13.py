##########################################################
# File: ex13.py
# Created: 2023-12-13
# Modified: 2023-12-13
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: XXX
##########################################################

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