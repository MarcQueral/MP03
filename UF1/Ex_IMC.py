#Crea un programa que a partir d’un pes i una altura et calculi l’índex de massa corporal.

pes = float (input("Escriu el teu pes en kilograms és: "))
altura = float (input("Escriu la teva altura en metres és: "))
IMC = (pes/(altura)**2)
print("El seu Índex de Massa Corporal és:" ,IMC)