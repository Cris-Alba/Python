#Determinar el gentilicio de una persona según las distintas opciones.

nombre=input('Ingrese su nombre: ')
print(" ")
print(" 1 - Argentina.")
print(" 2 - Uruguay.")
print(" 3 - Bolivia.")
print(" 4 - Chile.")
print(" 5 - Otro país.")
print(" ")
opcion=int(input('Ingrese la opción del país donde nació: '))


if (opcion==5):
    print(f'{nombre} no podemos determinar su gentilicio.')
elif(opcion==1):
    print(f'{nombre} usted es Argentina/o.')
elif(opcion==2):
    print(f'{nombre} usted es Uruguaya/o.')
elif(opcion==3):
    print(f'{nombre} usted es Boliviana/o.')
elif(opcion==4):
    print(f'{nombre} usted es Chilena/o.')
else:
    print('Usted debe elegir un número del 1 al 5.')