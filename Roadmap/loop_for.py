"""
Loop for

Loop -> Estrutura de repetição.
For -> É uma dessas estruturas.

C ou Java

for (int i = 0; i < (Um limitador); i++)
{
  //Execução do loop
}

Python

for item in interável:
  //Execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores interáveis

Exemplos de intereáveis:

- String
  nome = 'Geek University'
- Lista
  lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
- Range
  numeros = range(1, 10)

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
  print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
  for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range)

range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não

for numero in range(1, 10):
  print(numero)

# enumerate is useful for obtaining an indexed list:
# (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
for i, v in enumerate(nome):
  print(nome[i])

for i, v in enumerate(nome):
  print(v)

for _, v in enumerate(nome): #Quando não precisamos de um valor, descartamos com um _ (underline)
  print(v)

nome = 'Geek Univeristy'
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros = range(1, 10) # Tem que transformar em lista.

for valor in enumerate(nome):
  print(valor)

qtd = int(input("Quantas vezes esse loop deve rodar? "))
soma = 0

for n in range(1, qtd + 1):
  num = int(input(f"Informe {n}/{qtd} valor: "))
  soma = soma + num
print(f"A soma é {soma}.")

nome = 'Geek University'
for letra in nome:
  print(letra, end='')

# Tabela de emojis unicode https://apps.timwhitlock.info/emoji/tables/unicode
"""


# Original: U+1F60F
# Modificado: U0001F60F
for _ in range(3):
  for i in range(1, 11):
    print("\U0001F60F" * i)