print('Hola soy Esteban!')
print("Bienvenidos al curs de Python")
print("""En este video
 veremos el uso de las 
 cadenas de Caracteres""")
nombre="Esteban"
mensaje="Hola bienvenido"
print(mensaje+" "+nombre)

#Concatenar texto + numeros
numero=45
mensaje="La edad del programador es "
print(mensaje + str(numero))

#para buscar un caracter dentro de una cadena
mensaje="Este es el curso de python"
posicion=mensaje.find("curso")
#Nos de vuelve la posicion donde empieza la palabra curso
print(posicion)

#Estraer texto
print(mensaje[11:16])

#Comparación de texto
animal="Perro"
mamifero="Gato"
print(animal==mamifero)