#################################################################################################
# File: ex53.py
# Created: 2023-12-11
# Modified: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script calculates the cost of fencing a rectangular plot with a given length,
# width, and the price of the fence per meter.
#################################################################################################

comprimento = float(input("Qual o comprimento do terreno? "))
largura = float(input("Qual a largura do terreno? "))
preco_tela = float(input("Qual o preço da tela? R$"))

area = 2 * (comprimento + largura) * preco_tela

print(f"R${area:.2f}")