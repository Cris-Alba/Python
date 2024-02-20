'''Realice una lista de nombres y apellidos, correspondiente a un curso de programación.
Dentro del programa deberá existir esta lista para poder almacenar los distintos nombre y
apellidos de los alumnos inscriptos al curso.
Dentro del programa se podrán hacer las siguientes operaciones :
Agregar
Insertar
Mostrar lista de nombres y apellidos
Eliminar un alumno de la lista
Ordenar la lista
Limpiar la lista

Todo esto se deberá poder realizar a trevés de un menu en el programa'''

import  os

alumnos=[]

def menu():
    os.system('cls')
    print(f'''         **** Administración de Alumnos  ***
    
        1 - Agregar alumnos.
        2 - Insertar alumnos.
        3 - Mostrar lista de alumnos.
        4 - Buscar alumnos.
        5 - Eliminar alumnos.
        6 - Ordenar lista de alumnos.
        7 - Limpiar lista de alumnos.
        8 - Salir. ''')

def agregar():
    print('     Agregar alumnos.')
    apeNom=input('Ingrese el Apellido y nombre del alumno : ')
    alumnos.append(apeNom)
    print('El alumno se ingreso con éxito!')

def insertar():
    print('     Insertar alumnos.')
    apeNom=input('Ingrese el Apellido y nombre del alumno : ')
    pos=int(input('Ingrese la posición en la lista : '))
    alumnos.insert(pos,apeNom)
    print('El alumno se insertó de forma exitosa!')

def mostrar():
    print('     Lista de alumnos.')
    if len(alumnos)>0:
        for alumno in alumnos:
            print(alumno)
    else:
        print('No hay alumnos inscritos.')

def buscar():
    print('     Buscar un alumno.')
    if len(alumnos)>0:
        alumno=input('Ingrese el apellido y nombre a buscar : ')
        if alumno in alumnos:
            cantidad=alumnos.count(alumno)
            inicio=0
            for i in range(cantidad):
                pos=alumnos.index(alumno,inicio)
            print(f'{alumno} se encuentra en la posición {pos+1}.')
            inicio=pos+1
        else:
            print(f'{alumno} no se encuentra inscripto en la lista.')
    else:
        print('No hay alumnos inscritos.')

def eliminar():
    print('     Eliminar alumnos.')
    if len(alumnos)>0:
        for i in range(len(alumnos)):
            print(f'{i+1} - {alumnos[i]}')
        print('0 - Cancelar')
        pos=int(input('Ingrese la posición a eliminar : '))
        if 0<pos<=len(alumnos):
            alumnos.pop(pos-1)
            print('Registro eliminado con éxito!')
        else:
            print('No se elimminará ningún registro.')
    else:
        print('No hay alumnos inscritos.')

def ordenar():
    print('     Ordenar lista de alumnos.')
    if len(alumnos)>0:
        alumnos.sort()
        print('El listado de alumnos fue ordenado.')
    else:
        print('No hay alumnos inscritos.')

def limpiar():
    print('     Limpiar lista de alumnos.')
    alumnos.clear()
    print('Los registros fueron borrados.')


def main():
    continuar=True
    while continuar:
        menu()
        opc=int(input('Ingrese una opción del menú : '))
        if opc==1:
            agregar()
        elif opc==2:
            insertar()
        elif opc==3:
            mostrar()
        elif opc==4:
            buscar()
        elif opc==5:
            eliminar()
        elif opc==6:
            ordenar()
        elif opc==7:
            limpiar()
        elif opc==8:
            print('Gracias por utilizar nuestro programa.')
            print('Hasta luego!!')
            continuar=False
        else:
            print('Opción no válida.')
        input('Presione ENTER para continuar...')

if __name__=='__main__':
    main()