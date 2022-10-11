'''Crea un programa que demani una cadena de 4 caràcters (numèrics) a l'usuari, (com "1234") els emmagatzemi a una llista convertits en enters i imprimeixi la 
suma dels números que la formen. Heu d'utilitzar una funció interna per a fer la suma.'''

cadena = input("Escriu una cadena de 4 numeros: ")
llista = [int (cadena[0]), int (cadena[1]), int (cadena[2]), int (cadena[3])]
print("La llista queda aixi:", llista)

suma1 = sum(llista)
print("La suma dels nombres anteriors es:", suma1)

#Demana a l'usuari un número i afegeix-lo al final de la llista amb un mètode de llista.

numero = int (input("Ara dis-me només un nombre: "))
llista.append(numero)
print("La llista queda de la seguent manera:", llista)

#Ara elimina aquest número de la llista amb un mètode de llista.
llista.pop()
print("Quan elimino el darrer numero la llista queda aixi:", llista)

#Ordena la llista amb un mètode de llista.
llista.sort()
print("La llista ordenara queda de la manera següent:", llista)

#Mostra el seu número màxim i el seu mínim, extrets amb funcions internes.
print("El numero màxim de la llista es:", max(llista))
print("El numero mínim de la llista es:", min(llista))

#Calcula la mitjana aritmètica de la llista a partir de les funcions internes sum() i len().
numeros = len(llista)
suma = sum(llista)
print("La mitjana aritmètica és:", suma/numeros)