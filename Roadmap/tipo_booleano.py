"""
Tipo Booleano

Algebra Boolean, criada por George Boole

2 constantes, falso ou verdadeiro

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial minúscula

Errado:
true, false

Certo:
True, False
"""

ativo = True
print(ativo)

"""
Operações básicas:
"""

# Negação (not):
"""
Fazendo a negação, se o valor boolean for verdadeiro o resultado será falso,
se o valor for falso, o resultado será verdadeiro.
"""

print(not ativo)
logado =  False
# Ou (or)
"""
É uma operação binária , ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
"""
print(ativo or logado)

# E (and)
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos tem que ser verdadeiros
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
"""