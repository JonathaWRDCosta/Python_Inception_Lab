##############################################################################################
# File: ex43
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter the product price,
# calculates the price with a 10% discount, the value of each installment for a 3-month plan,
# and the commission for the seller for both cash and installment sales.
##############################################################################################

valor_produto = float(input("Qual o valor do produto? R$"))
dez_desconto = valor_produto - (valor_produto * 10 / 100)
tres_parcela = valor_produto / 3
comissao_avista = dez_desconto * 5 / 100
comissao_parcelado = valor_produto * 5 / 100

print(f"O produto com 10% de desconto R${dez_desconto:.2f}")
print(f"Valor da parcela em 3x sem juros R${tres_parcela:.2f}")
print(f"Comissão do vendedor(a) se a venda for a vista R${comissao_avista} (5% sobre o valor com desconto)")
print(f"Comissão do vendedor(a) se a venda for parcelada R${comissao_parcelado} (5% sobre o valor total)")