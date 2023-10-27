#Ex.20:Sorteando ordem na lista
from random import shuffle
n1 = input('1º nome:')
n2 = input('2º nome:')
n3 = input('3º nome:')
n4 = input('4º nome:')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será :')
print(lista)