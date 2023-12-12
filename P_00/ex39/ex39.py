##########################################################################################
# File: ex39
# Created em: 2023-12-11
# Author: Jonatha Costa <jonathawiliamsrdcosta@gmail.com>
#
# Description: This script distributes a prize of R$780,000.00 among three winners,
# where the first winner receives 46%, the second 32%, and the third the remaining amount.
##########################################################################################

import locale

# Defina a localidade para o Brasil
locale.setlocale(locale.LC_MONETARY, 'pt_BR')

premio = 780000000

primeiro = premio * 46 / 100
segundo = premio * 32 / 100
terceiro = premio - (primeiro + segundo)

print("A importância de R$780.000,00 será dividida entre três ganhadores de um concurso.")
print("Sendo que da quantia total")
print(f"O primeiro ganhador receberá 46%: R$ {locale.format_string('%.2f', primeiro, grouping=True)}")
print(f"O segundo ganhador ganhará 32%: R$ {locale.format_string('%.2f', segundo, grouping=True)}")
print(f"O terceiro receberá o restante: R$ {locale.format_string('%.2f', terceiro, grouping=True)}")
