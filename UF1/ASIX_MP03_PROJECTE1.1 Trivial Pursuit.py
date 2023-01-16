import random

#Benvinguda al programa
print("Benvingut a Trivial Pursuit!\nAquest joc consta d'intentar encertar 3 preguntes de les 10 que es plantejen a continuació.\n")

#Creo una llista per als jugadors i amb el random.shuffle els barrejo per tal que el torn sigui al·leatòri
jugadors = [str(input("Com et dius? ")), str(input("I tu, com et dius? "))]
random.shuffle(jugadors)

#Creo una llista per al contador, d'aquesta manera contaré les preguntes encertades per això des d'un principi ho igualo a 0 
contadors = [0,0]
torn=0

#Creo la llista de les preguntes, on a la posició 0 està la pregunta i les 3 opcions de resposta i a la posició 1 està la resposta correcta
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

#Realitzo un random.shuffle de preguntes i d'aquesta manera surtiran de forma al·leatòria
random.shuffle(preguntes)

print("Comença", jugadors[torn])

#Ara ve la part important del codi, faig un print de pregunta[0] per mostrar les preguntes amb les seves opcions
for pregunta in preguntes:
    print(pregunta[0])
    resposta = int(input("\nDisme un numero del 1 al 3 segons quin creus que sigui el resultat: "))
    #Aqui indiquem que quan la resposta es igual a la posició 1 de preguntes la resposta es correcta i sumem 1 al contador 
    if (resposta == pregunta[1]):
        print("Felicitats, has encertat!!\n")
        contadors[torn] += 1
        print("Portes", contadors[torn], "preguntes encertades")
        #Aqui indiquem que quan el contador arribi a 3, executi que el jugador que ha encertat les preguntes es el guanyador
        if (contadors[torn] == 3):
            print("\nEnhorabona", jugadors[torn], "ets el guanyador, ja has encertat 3 preguntes!!")
            break
    #En canvi, si no es respon la pregunta correcta realitzo un print indicant que la pregunta s'ha fallat i també mostro el contador però no sumo cap punt
    else:
        print("Has fallat!!\n")
        print("\nPortes", contadors[torn], "preguntes encertades")
        #Aqui realitzo el canvi de torn, així quan un jugador falla el torn passa a l'altre jugador i així successivament fins que s'encerten 3 preguntes o es realitzen les 10
        print("\nCanvi de torn")
        if (jugadors[torn] == 1):
            jugadors[torn] == 0
        elif (jugadors[torn] == 0):
            jugadors[torn] == 1
