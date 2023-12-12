################################################################################################
# File: ex36
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter the height and radius of a circular cylinder, 
# calculates its volume, and then displays the result.
################################################################################################

altura = float(input("Digite a altura de um cilindro circular: "))
raio = float(input("Digite o raio de um cilindro circular: "))

volume = 3.141592 * (raio * raio) * altura

print(f"O volume de um cilindro que tem altura de {altura} e um raio de {raio} é igual a {volume}")