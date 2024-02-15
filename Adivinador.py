#Juego de adivinanzas
import random

numero=random.randint(1,5)
num=int(input('Adivina el número del 1 al 5:'))

if num==numero :
    print("Felicitaciones adivinaste el número!")
else:
    print(f"No adivinaste, el número era {numero}.")
