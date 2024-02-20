'''Realizar un menú en donde se pueda elegir distintos tipos de conversiones:
1 - Convertir de grados celsius a Fahrenheit
2 - Convertir de grados Faherenheit a celsius
3- Salir

Luego se solicita los grados al operador y se realiza la conversión mostrando
los resultados y volviendo al menú principal
Utilizar funciones!
Formula = (0 ºC x 9/5) + 32 = 32 ºF
            (32 ºF - 32) * 5/9 = 0 ºC
'''

import os

def menu():
    os.system('cls')
    print('*************** Programa de Conversión de Temperaturas **************')
    print(' 1 - Convertir de grados celsius a Fahrenheit')
    print(' 2 - Convertir de grados Faherenheit a celsius')
    print(' 3 - Salir')

def celsius_a_fahrenheit(grados):
    return (grados*9/5) + 32

def fahrenheit_a_celsius(grados):
    return (grados-32) * 5/9

def main():
    opc=0
    while (opc!=3):
        menu()
        print('')
        opc=int(input(' Ingrese una opción del menú : '))
        if (opc==1):
            grados=float(input('Ingrese los grados celsius a convertir : '))
            valor = celsius_a_fahrenheit(grados)
            print(f'La conversión de {grados}ºC a Fahrenheit es : {valor}ºF')
        elif(opc==2):
            grados=float(input('Ingrese los grados fahrenheit a convertir : '))
            valor = fahrenheit_a_celsius(grados)
            print(f'La conversión de {grados}ºF a celsius es : {valor}ºC')
        elif(opc==3):
            print('Gracias por utilizar nuestro programa!')
        else:
            print('Ingrese una opción valida del 1 al 3')
        input('Presine ENTER para continuar.')

    print('Hasla luego!')
    input('Presione ENTER para terminar.')


if __name__=='__main__':
    main()
