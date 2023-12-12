"""
Tipo float.

Tipo real, decimal.

Casas decimais.

OBS: Os separadores das casas decimais na programação é ponto e não vírgula.
"""

# Errado do ponto de vista float, mas gera uma tupla
valor = 1,44
print(valor)
print(type(valor))

# Certo do ponto de vista float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
OBS: Perdemos precisão ao converter um float para inteiro.
"""

res = int(valor)
print(res)
print(type(res))