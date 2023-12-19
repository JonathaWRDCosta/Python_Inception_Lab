##########################################################################################################
# File: ex29.py
# Created: 2023-12-19
# Modified: 2023-12-19
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script is a basic math quiz that asks the user to solve five random addition problems.
##########################################################################################################

import random

print("Olá, bem vindo a prova básica de mátemcatica.")
print("Vamos começar :D")

points = 0

for _ in range(1, 6):
  random1 = random.randrange(1, 100)
  random2 = random.randrange(1, 100)

  soma = random1 + random2

  print(f"Qual é a soma entre {random1} + {random2}?")
  resposta = int(input("Resposta: "))
  if resposta == soma:
    print(f"Muito bem! Está correto, a soma entre {random1} e {random2} é {soma}")
    points += 1
  else:
    print(f"Incorreto, a resposta certá é {soma}")

print(f"Você obteve {points} de 5 pontos.")