""" Armen un juego de preguntas y respuestas con 3 preguntas.
El usuario puede ir avanzando por las preguntas si las contesta bien.
De lo contrario, termina el juego y le da el resultado.
Si el usuario contesta bien todas las preguntas, se le felicita,
De lo contrario, se le informa hasta que pregunta avanzó.
"""

print('Bienvenid@ al juego de preguntas y respuestas.')
print('_____________________________________________________')
respuesta=int(input('¿Sabes aritmética? ¿Cuánto es 8 + 8 *8?'))

if respuesta==72:
    print('Felicitaciones! Primera pregunta correcta, vamos al segundo nivel!!')
    print('________________________NIVEL 2____________________________________')
    respuesta=int(input('Continuamos ¿Cuanto es 10*10+24/2?'))
    if respuesta==112:
        print('Excelente! Seguimos adelante con el tercer y último nivel!!')
        print('________________________NIVEL 3____________________________________')
        respuesta=int(input('Última pregunta ¿Cúal es el resto de la división 245/3?'))
        if respuesta==2:
            print('Felicitaciones!!! Has ganado la partida!')
        else:
            print('Incorrecto. La respuesta correcta es 2.')
            print('Sigue intentando!!')
    else:
        print('La respuesta es incorrecta. El resultado es (10*10)+((24/2)) => 100+12=> 112.')
        print('Siga participando y no olvide seguir estudiando.')

else:
    print('La respuesta es incorrecta. El resultado es 8+(8*8) => 8+64=> 72')
    print('Intenta más tarde... a seguir estudiando.')
