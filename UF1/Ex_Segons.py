#Crea un programa que a partir d’una hora i uns minuts els calculi en segons.

hora = int (input("Disme l'hora que es. "))
minuts = int (input("Disme els minuts també. "))
print("Aquesta hora i minuts equivalen a aquests segons:", (hora * 3600) + (minuts*60))