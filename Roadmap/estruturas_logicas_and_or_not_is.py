"""
Estruturas logicas: and, or, not e is

Operadora unários:
  - not;
Operadora binários:
  - and, or e is;

  Regras de funcionamento:

  Para o 'and', ambos os valores precisam ser True
  Para o 'or', um ou outro valor precisa de True
  Para o 'not', o valor do boolean é invertido, ou seja, se for True vira False e se for False vira True
  Para o 'is', o valor é comparado com um segundo
"""

ativo = False
logado = False

if ativo:
  print("Usuário ativo no sistema.")

if not ativo:
  print("Você precisa ativar sua conta. Por favor, cheque seu email. (not)")

if logado or ativo:
  print("Bem-vindo usuário! (or)")

if logado and ativo:
  print("Bem-vindo usuário! (and)")
else:
  print("Você precisa ativar sua conta. Por favor, cheque seu email. (and)")

if ativo is False:
  print("Você precisa ativar sua conta. Por favor, cheque seu email. (is)")
else:
  print("Bem-vindo usuário! (is)")

# Ativo é Falso?
print(ativo is False)