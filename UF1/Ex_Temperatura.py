#Crea un programa que a partir d’una temperatura en Celsius et calculi la temperatura en Fahrenheid.

temperaturaC = float (input("Disme la temperatura que fa en graus Celsius: "))
temperaturaF = ((temperaturaC*1.8)+32)
print("La temperatura que fa en graus Fahrenheit és:" ,temperaturaF)

'''x = input("Temperatura(ºC): \n");
try:
    resultat= float(x)*1,8+32;
except ValueError:
    print("Has d'introduir un número!!")
except:
    print("Hi ha un altre tipus d'error.")
else:
    print(x,"graus Celsius equivalen a",round(resultat,2),"graus Fahrenheit");'''
