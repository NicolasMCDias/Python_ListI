#Ex.18:Seno, Cosseno e Tangente
from math import sin, tan, cos, radians
an = float(input('Incirá o valor de um ângulo:'))
seno = sin(radians(an))
Cosseno = cos(radians(an))
tangente = tan(radians(an))
print(f'O ângulo em seno é {seno:.2f}, em cosseno é {Cosseno:.2f} e em tangente é {tangente:.2f}')