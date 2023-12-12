"""
Tipo String

Em Python um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'Uma string', '123', 'a', 'True', '42.21'
- Estiver entre aspas duplas -> "Uma string", "123", "a", "True", "42.21"
- Estiver entre aspas simples triplas -> '''Uma string''', '''123''', '''a''', '''True''', '''42.21'''

nome1 = 'Geek University'
nome2 = "Geek University"
nome3 =  '''Geek University'''
print(nome1)
print(type(nome1))
print(nome2)
print(type(nome2))
print(nome3)
print(type(nome3))

nome = "Gina's bar"
print(nome)
print(type(nome))

nome = "Angelina \nJolie"
print(nome)
print(type(nome))

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome = 'Geek University'
print(nome[0:4]) # Slice de string
print(nome[5:15]) # Slice de string

# [  0,         1]
# ['Geek', 'University']
print(nome.split()[0])
print(nome.split()[1])

"""
# - Estiver entre aspas duplas triplas -> """Uma string""", """123""", """a""", """True""", """42.21"""

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome = 'Geek University'
"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
"""
print(nome[::-1]) # Inversão de string Pythonic
print(nome.replace('G', 'P'))