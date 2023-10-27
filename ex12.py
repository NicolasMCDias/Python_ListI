#execicio 12:Calculando Desconto
preço = float(input('Qual é o valor do produto:R$'))
desconto = float(input('De quando é o desconto(de 0 á 85):'))
if desconto > 85:
  print('Seu desconto é inválido!!')
else:
  pv = preço - preço * (desconto / 100 )
  print(f'O valor do produto foi de R${preço} para R${pv}')