"""
Recebendo dados do usuário.

input -> Todo dado recebido via input é do tipo string.

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""
# - Aspas duplas triplas -> """Angelina Jolie """

# Entrada de dados
# print("Qual seu nome? ")
# nome = input() # Input -> Entrada

nome = input("Qual seu nome? ")

# Exemplo de print antigo 2.x
# print("Seja bem-vindo(a) %s" % nome)

# Exemplo de print moderno 3.x
#print("Seja bem-vindo(a) {}".format(nome))

# Exemplo de print atual 3.7
print(f"Seja bem-vindo {nome}")

# print("Qual sua idade? ")
# idade = input()

idade = int(input("Qual sua idade? "))

# Processamento

# Saída de dados
# Exemplo de print antigo 2.x
# print("A %s tem %s anos" % (nome, idade))

# Exemplo de print moderno 3.x
# print("A {} tem {} anos".format(nome, idade))
 
 # Exemplo de print atual 3.7
print(f"{nome} tem {idade} anos")

"""
int(idade) -> cast

Cast é a conversão de um tipo de dado para outro.
"""
print(f"{nome} nasceu em {2023 - idade}") 