'''Escenari
Un mag júnior ha elegit un número secret. Ho ha amagat en una variable anomenada secret_number. 
Vol que tots els que executen el seu programa juguin el joc Endevina el número secret. Qui no endevini el número quedarà atrapat en un bucle sense fi per sempre! 
Malauradament, no sap com completar el codi. La teva tasca és ajudar el mag a completar el codi a l'editor de manera que el codi:

Demanarà a l'usuari que introdueixi un número enter.
Utilitzarà un bucle while.
Comproveu si el número ingressat per l'usuari és el mateix que el número escollit pel mag. Si el número escollit per l'usuari és diferent del número secret del mag, 
l'usuari hauria de veure el missatge "Ha, ha! Estàs atrapat al meu bucle!" i se us demanarà que torneu a introduir un número. Si el número ingressat per l'usuari 
coincideix amb el número escollit pel mag, el número s'ha d'imprimir a la pantalla, i el mag ha de dir les paraules següents: "Ben fet, muggle! Ets lliure ara".
El mag compta amb tu! No el decepcionis.'''

import random

secret_number = random.randint(1, 10)

while True:
    pregunta = int(input("Dis-me un numero de l'1 al 10: "))
    if pregunta == secret_number:
        print("Ben fet, muggle! Ets lliure ara")
        print("El numero secret era el", secret_number)
        break
    else:
        print("Ha, ha! Estàs atrapat al meu bucle!")