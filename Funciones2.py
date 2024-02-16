'''En una función en la cual se le pasa los segundos, la misma nos tiene
que devolver la cantidad de minutos y segundos'''

def segundos_a_minutos(segundos):
    m=segundos//60
    s=segundos%60
    return m,s

'''Bloque principal'''
print('Convierto segundos en minutos')
tiempo=int(input('Ingrese el tiempo en segundos a convertir: '))
min,seg=segundos_a_minutos(tiempo)

print(f'El equivalente es {min}:{seg}')
print('Hasta luego!!')
