###########################################################################
# File: ex37
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter the price of a product, 
# calculates the discounted price with a 12% discount, 
# and then displays the result.
###########################################################################

produto = float(input("Digite o valor de um produto: R$"))

desconto = produto - (produto * 12 / 100)

print(f"Um produto que custa R${produto} custará R${desconto} com 12% de desconto aplicado.")