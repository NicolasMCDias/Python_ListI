#exercicio 11:Pintando parede
altura = float(input('Altura[m]:'))
comprimento = float(input('Comprimento[m]:'))
area = altura * comprimento
print(f'Uma parede de {comprimento}x{altura} tem uma área de {area}m², serão necessarios {area / 2}litros de tinta')