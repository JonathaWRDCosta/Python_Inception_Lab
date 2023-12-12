#############################################################################
# File: ex29
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter four grades of a student, 
# calculates the average, and then displays the result.
#############################################################################

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
nota4 = float(input("Digite a quarta nota do aluno: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média é de {media:.2f}")