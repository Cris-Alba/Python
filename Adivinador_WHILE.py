''' Juego de adivinar un número
El sistema a través de la función random, generará un número al azar del 0 al 9.
El operador debe ingresar un número tratando de adivinar el mismo.
En la medida que realice los intentos y no adivine, se incrementará un contador, para
que al momento de adivinar el número se le informe al operador cual es el número
que adivino y en que intento.
'''
import random

numero=random.randint(0,9)
intentos=0
num=''

#ESTRUCTURA WHILE
while numero!=num:
    num=int(input('Adivina el número del 0 al 9:'))
    intentos=intentos+1
    if numero!=num:
        print(f'No adivinaste, el número {num} no es el correcto.')
        print('Intente nuevamente...')
        input('Pulse ENTER para continuar...')
else:
    print(f'FELICITACIONES!! adivinaste!!!')
    print(f'El número es {numero}, te costo {intentos} intentos adivinarlo.')

print('Has ta pronto!!')


