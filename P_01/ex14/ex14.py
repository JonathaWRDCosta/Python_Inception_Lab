##########################################################
# File: ex14.py
# Created: 2023-12-13
# Modified: 2023-12-13
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: XXX
##########################################################

print(30 * "=","NOTAS FINAIS",30 * "=")
print("*Olá Professores, as notas devem ser lançadas no sistema entre 0.0 e 10.0*")
print(74 * "=")

trabalho_lab = float(input("Notas trabalho de laboratório: "))
avaliacao_semestre = float(input("Notas de avaliação semestral: "))
exame_final = float(input("Nota exame final: "))

media = ((trabalho_lab * 2) + (avaliacao_semestre * 3) + (exame_final * 5)) / 10

if trabalho_lab < 0.0 or trabalho_lab > 10.0 or avaliacao_semestre < 0.0 or avaliacao_semestre > 10.0 or exame_final < 0.0 or exame_final > 10.0:
  print("Uma ou mais notas inválidas.")
elif media > 0.0 and media < 2.9:
  print(f"A média do aluno foi de {media}, por tanto...")
  print(f"REPROVADO! Estude mais...")
elif media > 3.0 and media < 4.9:
  print(f"A média do aluno foi de {media}, por tanto...")
  print(f"RECUPERAÇÃO! Estude mais para a próxima...")
else:
  print(f"A média do aluno foi de {media}, por tanto...")
  print(f"APROVADO! Parabéns!")
