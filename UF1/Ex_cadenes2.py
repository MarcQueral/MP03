'''Consulta els mètodes "built-in" que teniu disponibles per a cadenes i crea un 
programa que a partir d'una frase donada per l'usuari calculi:
- Número de caràcters.
- Número de paraules.
- Frase  amb totes les paraules en majúscula.
- Frase  amb totes les paraules en minúscula.
- Preguntat un caràcter a l'usuari retorni la posició de la primera coincidència 
trobada a la frase.
- Preguntat un caràcter a l'usuari retorni la posició de la darrera coincidència 
trobada a la frase.
- Preguntat un caràcter a l'usuari retorni el número de coincidències trobades a 
la frase.
- Mostri el número de vocals del text (has d'optimitzar al màxim aquest codi!!).
- Modifica el primer programa per a que abans de donar el resultat mostri si és 
cert que la cadena només conté números.'''

frase = input("Escriu una frase: ")
print("El numero de caràcters d'aquesta frase és:", len(frase))
print("El numero de paraules d'aquesta frase és:", len(frase.split()))
print("La frase amb les paraules en majúscula queda així:", frase.upper())
print("La frase amb les paraules en minúscula queda així:", frase.lower())

caracter = input("Escriu un caràcter: ")
print("La primera coincidència d'aquest caràcter trobada a la frase és:", (frase.find(caracter)))
print("La darrera coincidència d'aquest caràcter trobada a la frase és:", (frase.rfind(caracter)))
print("El numero de coincidències d'aquest caràcter trobada a la frase és:", (frase.count(caracter)))

a = frase.count("a")
A = frase.count("A")
e = frase.count("e")
E = frase.count("E")
i = frase.count("i")
I = frase.count("I")
o = frase.count("o")
O = frase.count("O")
u = frase.count("u")
U = frase.count("U")

vocals = a+A+e+E+i+I+o+O+u+U
print("El numero de vocals d'aquesta frase és:", vocals)
