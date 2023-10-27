#Analizador de texto
nome = input('Por favor, insirá seu nome completo:').strip().title()
print('seu nome em maiusculas:{}'.format(nome.upper()))
print('Seu nome em minusculas:{}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('seu primeiro nome é {} e têm {} letras'.format(separa[0], len(separa[0])))