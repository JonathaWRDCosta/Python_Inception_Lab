##########################################################
# File: ex02.py
# Created: 2023-12-22
# Modified: 2023-12-22
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: XXX
##########################################################

num = 1

# Usando 'for'
for _ in range (num, 100 + 1):
  print(f"{_}")

# Usando 'while'
while num <= 100:
  print(f"{num}")
  num += 1

# Usando um tipo de 'do while'
while True:
  print(f"{num}")
  num += 1
  if num == 101:
    break