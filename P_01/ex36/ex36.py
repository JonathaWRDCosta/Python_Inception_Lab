###########################################################################################################
# File: ex36.py
# Created: 2023-12-25
# Modified: 2023-12-25
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script calculates the commission to be paid to a salesperson based on the sales amount.
###########################################################################################################

valor_venda = float(input("Digite o valor da venda: R$"))

if valor_venda >= 100000:
    comissao = 700 + 0.16 * valor_venda
elif valor_venda >= 80000:
    comissao = 650 + 0.14 * valor_venda
elif valor_venda >= 60000:
    comissao = 600 + 0.14 * valor_venda
elif valor_venda >= 40000:
    comissao = 550 + 0.14 * valor_venda
elif valor_venda >= 20000:
    comissao = 500 + 0.14 * valor_venda
else:
    comissao = 400 + 0.14 * valor_venda

print(f"A comissão a ser paga ao vendedor é: R${comissao:.2f}")
