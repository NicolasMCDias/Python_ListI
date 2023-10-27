#exercicio 10:conversor de moeda
reais = float(input('insirá um valor em reais:R$'))
dolar = reais / 5.11
Yenes = reais / 0.045
Libras = reais / 6.95
euro = reais / 5.78
print('Seus R${:.2f} se tormam U${:.2f}, ¥{:.2f}, £{:.2f} e €{:.2f}'.format(reais, dolar, Yenes, Libras, euro))
