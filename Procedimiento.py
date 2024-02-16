'''Tabla de multiplicar'''
import os

def tabla_multiplicar(numero, limite=10):
    os.system('cls')
    print(f'******** Tabla del numero {numero} *********')
    for i in range(1,limite+1):
        print(f'{numero} x {i} = {numero*i}')


'''Bloque principal'''
tabla_multiplicar(4,12)
input('Presione ENTER para continuar.')
num=5
tabla_multiplicar(num)

print('Hasta luego!!!')