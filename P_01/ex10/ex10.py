###################################################################################
# File: ex10.py
# Created: 2023-12-12
# Modified: 2023-12-12
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter their height and gender (M/F),
# calculates the ideal weight based on the gender, and then displays the result.
###################################################################################

altura = float(input("Qual sua altura? M"))
sexo = input("Qual o seu sexo? [M/F]: ").upper()

if sexo == 'M':
  peso_ideal = (72.7 * altura) - 58
  print(f"Olá, para homens o peso ideal é de {peso_ideal:.2f} quilos.")
elif sexo == 'F':
  peso_ideal = (62.1 * altura) - 44.7
  print(f"Olá, para mulheres o peso ideal é de {peso_ideal:.2f} quilos.")
else:
  print("Uma ou mais informações estão incorretas. Lembre-se que altura será medida em CM.")
  print("E o sexo é preciso apenas digitar M para masculino ou F para feminino.")