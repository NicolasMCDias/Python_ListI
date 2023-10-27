#Ex.15:Aluguel de carro
dia = int(input('Quantos dias você alugou o carro?'))
km = float(input('Circulou por quantos Quilometrôs:'))
valor = dia * 60 + km * 0.15
print(f'vai lhe custar R${valor}')