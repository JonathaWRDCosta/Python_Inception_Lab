###########################################################################
# File: ex19
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a volume in liters, 
# converts it to cubic meters (m³), and then displays the converted volume.
###########################################################################

litros = float(input("Digite um valor de volume em litros para ser convertido em metros cúbicos (m³): "))
metros = litros / 1000

print(f"{litros} convertidos em metros cúbicos (m³) é igual a {metros}")
