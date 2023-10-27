#Ex.23:separando digitos de um número
num = int(input('Insirá um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade:{u};\033[34mDezena:\033[m{d};\033[32mCentena:\033[m{c};\033[36mMilhar:\033[m{m}')