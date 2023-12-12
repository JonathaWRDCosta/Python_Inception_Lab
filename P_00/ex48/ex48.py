###################################################################################
# File: ex48
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script prompts the user to enter an integer representing seconds,
# converts it into hours, minutes, and seconds, and then displays the result.
###################################################################################

seg = int(input("Digite um valor inteiro em segundos: "))

hou = seg // 3600
seg = seg % 3600
min = seg // 60
seg = seg % 60

print(f"{hou}h:{min}min:{seg}seg")