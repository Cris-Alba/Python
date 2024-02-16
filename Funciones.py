'''Función - Calculo de superficie'''

def area_triangulo(base, altura):
    return base*altura/2

'''Bloque Princial'''
print('Programa para cálculo de área de un triángulo')
base=float(input('Base: '))
altura=float(input('Altura: '))
a= area_triangulo(base,altura)
print(f'Area = {a}')

print('Hasta luego!!')
