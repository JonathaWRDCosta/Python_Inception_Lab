#############################################################################################
# File: ex52.py
# Created: 2023-12-12
# Modified: 2023-12-12
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script calculates and displays the prize distribution among three players
# based on the amounts they bet on a prize pool.
#############################################################################################

premio = float(input("Qual o valor do prêmio? R$"))

jogador_a = float(input("Qual o valor que o jogador 1 apostou? R$"))
jogador_b = float(input("Qual o valor que o jogador 2 apostou? R$"))
jogador_c = float(input("Qual o valor que o jogador 3 apostou? R$"))

total_apostado = jogador_a + jogador_b + jogador_c

premio_a = (jogador_a/total_apostado) * premio
premio_b = (jogador_b/total_apostado) * premio
premio_c = (jogador_c/total_apostado) * premio

print(f"O jogador 1 apostou R${jogador_a:.2f} equivalente a {(jogador_a / total_apostado) * 100:.2f}% do prêmio e ganhará R${premio_a:.2f}")
print(f"O jogador 2 apostou R${jogador_b:.2f} equivalente a {(jogador_b / total_apostado) * 100:.2f}% do prêmio e ganhará R${premio_b:.2f}")
print(f"O jogador 3 apostou R${jogador_c:.2f} equivalente a {(jogador_c / total_apostado) * 100:.2f}%  do prêmio e ganhará R${premio_c:.2f}")