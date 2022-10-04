'''Crea un programa que a partir d'una cadena de 4 caràcters (numèrics) preguntada
a l'usuari, (com "123456") imprimeixi la suma dels números que la formen. 
Teniu en compte que només s'ha d'utilitzar un input, estem treballant les cadenes.'''

numero = input("Escriu un numero de 4 caràcters: ")
resultat = (int(numero[0]) + int(numero[1]) + int(numero[2]) + int(numero[3]))
print("La suma dels 4 caràcters és:", resultat)