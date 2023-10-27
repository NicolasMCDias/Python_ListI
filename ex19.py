#Ex.19:Sorteando um item
from random import choice
print('Quem vai lavar a roupa')
n1 = str(input('1º nome:'))
n2 = str(input('2º nome:'))
n3 = str(input('3º nome:'))
n4 = str(input('4º nome:'))
lista = [n1, n2, n3, n4]
print(f'Quem vai lavar a louça é:{choice(lista)}')