'''Armar una cuenta regresiva, de 10 a 0, que decremente cada 1 segundo
para el despegue de nuestro cohete a Marte'''

import os
import time

print('¿Estas preparado para el despegue?')
input('Presione la tecla ENTER')

for numero in range(10,-1,-1):
    print(numero)
    time.sleep(1)
    os.system('cls')

print('Buen viaje!!!')
print('Nos vemos en Marte!!!')

#Lo ejecutamos en consola