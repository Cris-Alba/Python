'''Calcular el promedio de una cantidad de numero'''

acumulador=0
cantidad=int(input('Ingrese la cantidad de numeros: '))

for numero in range(cantidad):
    valor=int(input(f'Ingrese el numero {numero+1}: '))
    acumulador=acumulador+valor

promedio=acumulador/cantidad
print(f'El calculo del promedio es {promedio}')

print('Hasta luego!')

#Lo ejecutamos en consola