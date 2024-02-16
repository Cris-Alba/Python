'''
Realizar una Calculadora Aritmética con las siguientes operaciones:
1. Suma de dos números.
2. Resta de dos números.
3. Multiplicación de dos números.
4. División de dos números (parte entera).
5. Modulo de una división.
6. Potencia de dos números.
Se deben ingresar dos valores enteros y luego elegir la operación del menú anterior.
Mostrar por pantalla el resultado.
'''

print('Bienvenido, Vamos ha realizar un cálculo con 2 números enteros')
print(" ")
num1=int(input('Introduce el primer número: '))
print(" ")
num2=int(input('Introduce el segundo número: '))
print(" ")
print('Operaciones:')
print('1. Suma')
print('2. Resta')
print('3. Multiplicación')
print('4. División')
print('5. Modulo de una división')
print('6. Potencia')

opcion=int(input('Elija el número del calculo elegido'))
resultado=0
operacion='nada'

if opcion==1:
    resultado=num1+num2
    operacion='suma'
elif opcion==2:
    resultado=num1-num2
    operacion='resta'
elif opcion==3:
    resultado=num1*num2
    operacion='multiplicación'
elif opcion==4:
    resultado=num1//num2
    operacion='división'
elif opcion==5:
    resultado=num1%num2
    operacion='modulo de división'
elif opcion==6:
    resultado=num1+num2
    operacion='potencia'
else:
    print('Ha habido un error, tiene que elegir una opción de la 1 a la 6.')

if operacion!='nada':
    print(f'El resultado de la {operacion} de {num1} y {num2} es {resultado}.')

