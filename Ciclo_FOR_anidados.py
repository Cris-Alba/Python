'''Tabla de multiplicar del 1 al 10.
Que multiplique también del 1 al 10.'''

import os

for numero in range(1,10+1):
    print(f'******** Tabla del numero {numero} *********')
    for multiplicador in range(1,10+1):
        print(f'{multiplicador} x {numero} = {multiplicador*numero}')
    input('Presione ENTER para continuar.')
    os.system('cls')

print('Hasta luego!!')
