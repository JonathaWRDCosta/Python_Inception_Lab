##########################################################################################################################################
# File: ex34.py
# Created: 2023-12-25
# Modified: 2023-12-25
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script takes the student's grade and the number of absences as input and outputs the corresponding grade based on a predefined scale.
##########################################################################################################################################

nota = float(input("Qual a nota do aluno? "))
faltas = int(input("Quantas faltas o aluno teve? "))

if nota < 0 or nota > 10:
  print("Notas inválidas. Notas devem estar entre 0.0 e 10.0!")

else:
  if nota >= 9.0:
    if faltas <= 20:
      print("A nota do aluno é A.")
    else:
      print("A nota do aluno é B.")

  elif nota >= 7.5 and nota <= 8.9:
    if faltas <= 20:
      print("A nota do aluno é B.")
    else:
      print("A nota do aluno é C.")

  elif nota >= 5.0 and nota <= 7.4:
    if faltas <= 20:
      print("A nota do aluno é C.")
    else:
      print("A nota do aluno é D.")

  elif nota >= 4.0 and nota <= 4.9:
    if faltas <= 20:
      print("A nota do aluno é D.")
    else:
      print("A nota do aluno é E.")

  elif nota >= 0.0 and nota <= 3.9:
    if faltas <= 20:
      print("A nota do aluno é E.")
    else:
      print("A nota do aluno é F.")
