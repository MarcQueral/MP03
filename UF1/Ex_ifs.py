menu = {}
menu['1']="Temperatura" 
menu['2']="IMC"
menu['3']="Mitjana aritmètica"
menu['4']="Segons"
exercici=input("Quin exercici vols fer?")

if (exercici=='1'):
    print("Has elegit fer l'exercici 1.")
temperaturaC = float (input("Disme la temperatura que fa en graus Celsius: "))
temperaturaF = ((temperaturaC*1.8)+32)
print("La temperatura que fa en graus Fahrenheit és:" ,temperaturaF)

if (exercici=='2'):
    print("Has elegit fer l'exercici 2.")
pes = float (input("Escriu el teu pes en kilograms és: "))
altura = float (input("Escriu la teva altura en metres és: "))
IMC = (pes/(altura)**2)
print("El seu Índex de Massa Corporal és:" ,IMC)

if (exercici=='3'):
    print("Has elegit fer l'exercici 3.")
numero1 = int (input("Escriu un nombre aleatori: "))
numero2 = int (input("Escriu un altre numero: "))
resultat=((numero1+numero2)/2)
print("La mitjana aritmètica d'aquests dos nombres és:" ,resultat)

if (exercici=='4'):
    print("Has elegit fer l'exercici 4.")
hora = int (input("Disme l'hora que es. "))
minuts = int (input("Disme els minuts també. "))
print("Aquesta hora i minuts equivalen a aquests segons:", (hora * 3600) + (minuts*60))