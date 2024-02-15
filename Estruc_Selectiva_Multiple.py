#Estructura selectiva multiple.
#Tenemos que determinar si un alumno aprueba o no lo cursado.
#Los aprobados tienen como nota 6 o mas ... y tienen que tener mas
#de 20 clases de asistencia. Poner si el alumno aprobó y si no
#aprobó, porque no aprobo?

NOTA=6
ASISTENCIA=20

nota_cursada=int(input('Ingrese su nota de cursada: '))
asistencia_cursada=int(input('Ingrese la cantidad de clases que asistió: '))

if (nota_cursada>=NOTA and asistencia_cursada>=ASISTENCIA):
    print('Felicitaciones, usted aprobó la cursada!')
elif(nota_cursada<NOTA and asistencia_cursada>=ASISTENCIA):
    print('Usted no aprobó por nota baja.')
elif(nota_cursada>=NOTA and asistencia_cursada<ASISTENCIA):
    print('Usted no aprobó por baja asistencia.')
else:
    print('Usted no aprobó por nota baja y falta de asistencia.')