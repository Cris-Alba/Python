def menu(titulo,*opciones,**mensajeError):
    print(f'**********  {titulo}  **********')
    for i in range(len(opciones)):
        print(f'          {i+1} - {opciones[i]}')

    opc = int(input('Ingrese una opción del menú : '))
    if 1 <= opc <= len(opciones):
        print(f' Usted eligió {opciones[opc-1]}')
    else:
        if 'error' in mensajeError:
            print(f'{mensajeError["error"]}')


menu('Operaciones aritméticas', 'Suma', 'Resta', 'Multiplicación', 'División', error='Usted eligió una opción incorrecta.')