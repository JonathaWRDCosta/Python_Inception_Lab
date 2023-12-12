#########################################################################################################
# File: ex44
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter the height of a step and the desired height to reach,
# calculates the number of steps needed to reach the desired height,
# and then displays the result.
#########################################################################################################

altura_degrau = float(input("Qual a altura do degrau [cm]? "))
altura_alcancar = float(input("Qual altura deseja alcançar [cm]? "))

resultado = int(altura_alcancar / altura_degrau)

print(f"Para alcançar uma altura de {altura_degrau}cm você terá que subir {resultado} degraus")