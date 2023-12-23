"""
Loop while

Forma geral

while expressão_booleana:
  //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:

num = 5

num < 5

Exemplo 1:

numero = 1

while numero < 10:
  print(numero)
  # numero = numero + 1
OBS: Em um loop while. é importante que cuidemos de um critério de parada para não causar loop infinito.

# C ou Java

while(expressão)
{
  //Execução
}
# C ou Java

do{
  /Execução
} while(Expresão):

"""

# Exemplo 2:
resposta = ''

while resposta != 'sim':
  resposta = input("Já acabou Jessica? ")

