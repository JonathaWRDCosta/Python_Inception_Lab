####################################################################################
# File: ex26.py
# Created: 2023-12-15
# Modified: 2023-12-15
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script calculates and categorizes the fuel consumption of a car.
####################################################################################

distancia = float(input("Digite a distância percorrida em Km: "))
litros_de_gasolina = float(input("Digite a quantidade de litros de gasolina consumidos: "))

consumo = distancia / litros_de_gasolina

print("| CONSUMO | (Km/l) | Mensagem           |")
print("-" * 41)

if consumo < 8.0:
    print(f"| {consumo:.1f}     | Maior que 8.0   | Venda o carro!     |")
elif 8.0 <= consumo <= 14.0:
    print(f"| {consumo:.1f}     | 8.0 a 14.0       | Econômico!          |")
else:
    print(f"| {consumo:.1f}     | Maior que 14.0  | Super econômico!    |")
