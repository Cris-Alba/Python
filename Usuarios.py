'''
Armar un script en Python que permita almacenar registros de usuarios. Para cada
usuario necesitamos registrar nombre, apellido, edad y peso, estos valores seran
guardados en una tupla.
Para cargar y trabajar con varios usuarios se creará una lista en la cual me
permita guardar los registros de cada usuario, es decir una lista de tuplas.
El programa debe tener un menu ciclico, en el cual pueda registrar los usuarios
y consultar los mismos.
'''
import os

REGISTRAR = 1
CONSULTAR = 2
SALIR = 0


def mostrar_menu():
    os.system('cls')
    print(f'''         Mis usuarios
    
    {REGISTRAR} - Registrar un usuario.
    {CONSULTAR} - Consultar los usuarios.
    {SALIR} - Salir del programa.
    ''')


def registrar_usuario(usuarios):
    print('      Registrar Usuario')
    nombre = input('Nombre : ')
    apellido = input('Apellido : ')
    edad = int(input('Edad : '))
    peso = float(input('Peso : '))
    usuarios.append((nombre, apellido, edad, peso))


def consultar_usuario(usuarios):
    os.system('cls')
    print('         Consulta de usuarios')
    if len(usuarios) == 0 :
        print('Aún no hay registrados usuarios')
    else:
        for usuario in usuarios:
            nombre, apellido, edad, peso=usuario
            print(f'Nombre: {nombre}')
            print(f'Apellido: {apellido}')
            print(f'Edad: {edad}')
            print(f'Peso: {peso}')
            print('********************************************************')

def main():
    mis_usuarios = []
    continuar = True
    while continuar:
        mostrar_menu()
        opc=int(input('Seleccione la opción del menú : '))
        if opc == REGISTRAR:
            registrar_usuario(mis_usuarios)
        elif opc == CONSULTAR:
            consultar_usuario(mis_usuarios)
        elif opc == SALIR:
            continuar = False
        else:
            print('Opción no válida, elija una opción correcta.')
        input('Presione ENTER para continuar...')
    print('Hasta luego!!')

if __name__=='__main__':
    main()