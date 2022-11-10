import random

print("Benvingut a Trivial Pursuit!\nAquest joc consta d'intentar encertar 3 preguntes de les 10 que es plantejen a continuació.\n")

#El torn d'inici serà aleatori.
jugador1 = str(input("Com et dius? "))
jugador2 = str(input("I tu, com et dius? "))

marcador1 = 0
marcador2 = 0
'''while (marcador1 == 3 or marcador2 == 3):
    print("\nEnhorabona, ets el guanyador, ja has encertat 3 preguntes!!")
    break'''

contador = 1
while (contador == 10):
    print("\nFinal, ja s'han realitzat les 10 preguntes")
    break

#Preguntes
preguntes = [["\nQui es el millor jugador de futbol del món? \n1. Leo Messi\n2. Cristiano Ronaldo\n3. Neymar Jr\n",1],
            ["\nQuin numero portava Xavi Hernandez amb el Barça? \n1. 8\n2. 4\n3. 6\n",3],
            ["\nA quina nacionalitat pertany Zinedine Zidane? \n1. Portugal\n2. Russia\n3. França\n",3],
            ["\nQuantes copes del món té Espanya? \n1. 1\n2. 4\n3. 2\n",1],
            ["\nQui va fer el gol a la final del mundial 2010? \n1. Fernando Torres\n2. Andres Iniesta\n3. David Villa\n",2],
            ["\nQuin equip té més trofeus de la Champions League? \n1. Liverpool\n2. Real Madrid\n3. Bayern de Munic\n",2],
            ["\nQuantes pilotes d'or té Leo Messi? \n1. 7\n2. 5\n3. 3\n",1],
            ["\nQuan es va fundar el FC Barcelona? \n1. L'any 1922\n2. L'any 1891\n3. L'any 1899\n",3],
            ["\nEn quants equips ha jugat Cristiano Ronaldo? \n1. 3\n2. 4\n3. 2\n",2],
            ["\nQuants anys té Earling Haaland? \n1. 20\n2. 22\n3. 25\n",2]]

inici = random.randint(1,2)
if (inici == 1):
    print("Comença", jugador1)
    while (marcador1 <= 3):
        for pregunta in preguntes:
            pregunta = random.choice(preguntes)
            print(pregunta[0])
            resposta = int(input("\nDisme un numero del 1 al 3 segons quin creus que sigui el resultat: "))
            if (resposta == pregunta[1]):
                print("Felicitats, has encertat!!\n")
                marcador1 = marcador1 + 1
                print("\nMARCADOR\n", jugador1, ":\n" , marcador1, "/" ,contador ,"\n" ,jugador2, ":\n", marcador2, "/", contador)
                contador = contador + 1
            else:
                print("Has fallat!!\n")
                print("\nCanvi de jugador!")
                #inici == 2
                print("\nMARCADOR\n", jugador1, ":\n" , marcador1, "/" ,contador ,"\n" ,jugador2, ":\n", marcador2, "/", contador)
                contador = contador + 1
elif (inici == 2):
    print("Comença", jugador2)
    while (marcador2 <= 3):
        for pregunta in preguntes:
            pregunta = random.choice(preguntes)
            print(pregunta[0])
            resposta = int(input("\nDisme un numero del 1 al 3 segons quin creus que sigui el resultat: "))
            if (resposta == pregunta[1]):
                print("Felicitats, has encertat!!\n")
                marcador2 = marcador2 + 1
                print("\nMARCADOR\n", jugador1, ":\n" , marcador1, "/" ,contador ,"\n" ,jugador2, ":\n", marcador2, "/", contador)
                contador = contador + 1
            else:
                print("Has fallat!!\n")
                print("\nCanvi de jugador!")
                #inici == 1
                print("\nMARCADOR\n", jugador1, ":\n" , marcador1, "/" ,contador ,"\n" ,jugador2, ":\n", marcador2, "/", contador)
                contador = contador + 1







