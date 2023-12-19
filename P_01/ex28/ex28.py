######################################################################################
# File: ex28.py
# Created: 2023-12-16
# Modified: 2023-12-16
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script calculates different types of averages based on user input.
######################################################################################

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))

escolha = int(input("Escolha uma opção: \n1 - Geométrica\n2 - Ponderada\n3 - Harmônica\n4 - Aritmética\n"))

if num1 < 1 or num2 < 1 or num3 < 1:
    print("Valores inválidos, os valores devem ser positivos.")
elif escolha == 1:
    resultado = (num1 * num2 * num3) ** (1 / 3)
    print(f"A média geométrica é {round(resultado, 2)}")
elif escolha == 2:
    w1 = int(input("Digite o peso para o primeiro número: "))
    w2 = int(input("Digite o peso para o segundo número: "))
    w3 = int(input("Digite o peso para o terceiro número: "))
    
    resultado = (w1 * num1 + w2 * num2 + w3 * num3) / (w1 + w2 + w3)
    print(f"A média ponderada é {round(resultado, 2)}")
elif escolha == 3:
    resultado = 3 / (1/num1 + 1/num2 + 1/num3)
    print(f"A média harmônica é {round(resultado, 2)}")
elif escolha == 4:
    resultado = (num1 + num2 + num3) / 3
    print(f"A média aritmética é {round(resultado, 2)}")
else:
    print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")
