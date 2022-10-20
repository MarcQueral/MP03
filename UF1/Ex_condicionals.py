print("1. Tasca 1")
print("2. Tasca 2")
print("3. Tasca 3")
exercici = int(input("Disme un numero del 1 al 3 en funció de l'exercici que vulguis realitzar. "))

#Tasca 1
#Escriu un programa que sol·liciti una puntuació entre 0 i 10. Si la puntuació és fora d'aquest rang, mostra un missatge 
#d'error. Si la puntuació està entre 0 i 10, mostra la qualificació usant la taula següent:
#Puntuació Qualificació
#    >= 9 Excel·lent
#    >= 8 Notable
#    >= 7 Bé
#    >= 5 Suficient
#    < 5 Insuficient

if (exercici == 1):
    
    nota = float(input("Escriu una nota entre 0 i 10. "))
    
    if (nota >= 9):
        print("Excel·lent")
    elif (nota == 8):
        print("Notable")
    elif (nota == 7):
        print("Bé")
    elif (nota >= 5):
        print("Suficient")
    elif (nota < 5):
        print("Insuficient")
    else:
        print("T'he dit un numero entre 0 i 10!!!")

#Tasca 2
#Escriu un programa que demani l'any actual i un altre any qualsevol. El resultat ha de mostrar quants anys han passat 
#des de l'any introduït o quants anys falten.
#Ara milloreu el programa per a fer que quan la diferència sigui només d'un any, ens digui que només falta un any.

elif (exercici == 2):
    
    any1 = int(input("Dis-me l'any actual. "))
    any2 = int(input("Ara dis-me un any qualsevol. "))
    resultat = any1 - any2

    if (resultat > 0):
        print("Han passat", resultat, "anys.")
    elif (resultat < 0):
        print("Falten", resultat * -1, "anys")

#Tasca 3
#Creeu un joc de daus on es generi una tirada per a cadascun dels jugadors, quan escriguin la paraula "tirar" en un input
#i posteriorment es mostri el resultat de la partida.
#Podeu utilitzar la funció randint() de la llibreria random:
#Exemple d'ús:
#   import random
#   numero = random.randint(1, 6)

elif (exercici == 3):
    import random
    
    numero = random.randint(1, 6)
    print("\nJugador 1")
    jugador1 = input("")
    print("\nJugador 2")
    jugador2 = input("")

    if (jugador1 == "tirar" and jugador2 == "tirar"):
        jugador1 = random.randint(1, 6)
        jugador2 = random.randint(1, 6)
        if (jugador1 > jugador2):
            print ("\nHa guanyat el jugador 1")
        elif (jugador1 < jugador2):
            print ("\nHa guanyat el jugador 2")
        elif (jugador1 == jugador2):
            print("\nHeu empatat")
        elif (jugador1 != "tirar" or jugador2 != "tirar"):
            print("\nHeu de tirar els daus!!")