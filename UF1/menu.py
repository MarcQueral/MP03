print("1. Temperatura")
print("2. IMC")
print("3. Mitjana aritmètica")
print("4. Segons")
menu = input("Disme un numero del 1 al 4 en funció de l'exercici que vulguis realitzar. ")

if (menu=="1"):
    temperaturaC = float (input("Disme la temperatura que fa en graus Celsius: "))
    temperaturaF = ((temperaturaC*1.8)+32)
    print("La temperatura que fa en graus Fahrenheit és:" ,temperaturaF)

elif (menu=="2"):
    pes = float (input("Escriu el teu pes en kilograms és: "))
    altura = float (input("Escriu la teva altura en metres és: "))
    IMC = (pes/(altura)**2)
    print("El seu Índex de Massa Corporal és:" ,IMC)

elif (menu=="3"):
    numero1 = int (input("Escriu un nombre aleatori: "))
    numero2 = int (input("Escriu un altre numero: "))
    resultat=((numero1+numero2)/2)
    print("La mitjana aritmètica d'aquests dos nombres és:" ,resultat)

elif (menu=="4"):
    hora = int (input("Disme l'hora que es. "))
    minuts = int (input("Disme els minuts també. "))
    print("Aquesta hora i minuts equivalen a aquests segons:", (hora * 3600) + (minuts*60))