###########################################################################
# File: ex32
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter a number, 
# calculates the successor of its triple and the predecessor of its double,
# then displays the sum of the successor and predecessor.
###########################################################################

num = int(input("Digite um número: "))

sucessor = (num * 3) + 1
antecessor = (num * 2) - 1

print(f"A soma do sucessor de seu triplo com o antecessor de seu dobro é {sucessor + antecessor}")