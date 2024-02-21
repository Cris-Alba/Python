'''Crear un script en Python, simulando una Agenda.
En donde el usuario pueda registrar cada evento en su agenda, cada evento se
agregará a una cola de prioridad de forma tal que aquellos con mayor prioridad
salgan primero de la estructura.
Para manejar la agenda se le mostrará al usuario un menú con las opciones de
agregar evento y atender evento.'''

import os
import queue

'********  Constantes ************'
AGENDAR = 1
ATENDER = 2
SALIR = 0

'*****  Menú *****'


def mostrar_menu():
    os.system('cls')
    print(f'''             ******  MI AGENDA *****
    {AGENDAR} -  Agendar evento.
    {ATENDER} -  Atender evento.
    {SALIR} -  Salir.''')


'***** Agendar Evento *****'


def agendar(ag):
    print('      AGENDAR EVENTO')
    evento = input('Evento : ')
    ag.put(evento)
    input('Presione ENTER para volver al menu!')


'***** Atender Evento *****'


def atender(ag):
    print('      ATENDER EVENTO')
    if ag.empty():
        print('No hay eventos en la agenda por atender.')
        input('Presione ENTER para volver al menu!')
    else:
        evento = ag.get()
        print(f'Evento atendido : {evento}')
        input('Presione ENTER para volver al menu!')


'***** Bloque principal *****'


def main():
    agenda = queue.PriorityQueue()
    continuar = True
    while continuar:
        mostrar_menu()
        opc = int(input('Elija una opción del menú : '))
        if opc == AGENDAR:
            agendar(agenda)
        elif opc == ATENDER:
            atender(agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print('Elija una opción válida.')
            input('Presione ENTER para volver al menu!')
    print('Hasta luego!!')


if __name__ == '__main__':
    main()
