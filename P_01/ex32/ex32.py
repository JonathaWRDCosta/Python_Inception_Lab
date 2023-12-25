##########################################################################################################################################
# File: ex32.py
# Created: 2023-12-24
# Modified: 2023-12-24
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script represents a menu for a restaurant. It allows the user to choose a product by entering its code and specifying the quantity, then calculates and displays the total price.
##########################################################################################################################################

print("Olá, esse é o nosso menu.")
print("-" * 32)
print("Especificações | Código | Preço")
print("-" * 32)
print("Cachorro Quente|   100  | 1.20 ")
print("Bauru Simples  |   101  | 1.30")
print("Bauru com Ovo  |   102  | 1.50")
print("Hamburger      |   103  | 1.20")
print("Cheeseburguer  |   104  | 1.70")
print("Suco           |   105  | 2.20")
print("Refrigerante   |   106  | 1.00")
print("-" * 32)

produto = int(input("Digite o código do produto que deseja: "))
qty = int(input("Digite a quantidade: "))

if produto == 100:
  preco = 1.20 * qty
  print(f"O valor total é de R${preco:.2f}")

elif produto == 101:
  preco = 1.30 * qty
  print(f"O valor total é de R${preco:.2f}")

elif produto == 102:
  preco = 1.50 * qty
  print(f"O valor total é de R${preco:.2f}")

elif produto == 103:
  preco = 1.20 * qty
  print(f"O valor total é de R${preco:.2f}")

elif produto == 104:
  preco = 1.70 * qty
  print(f"O valor total é de R${preco:.2f}")

elif produto == 105:
  preco = 1.20 * qty
  print(f"O valor total é de R${preco:.2f}")

elif produto == 106:
  preco = 1.00 * qty
  print(f"O valor total é de R${preco:.2f}")

else:
  print("Código ou valor incorreto.")