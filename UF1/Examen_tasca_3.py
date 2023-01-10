'''Escenari
Imagina una llista: no gaire llarga ni gaire complicada, només una llista simple que conté alguns números enters. Alguns d'aquests números poden estar repetits, 
i aquesta és la clau. No volem cap repetició. Volem que siguin eliminats. La teva tasca és escriure un programa que elimini totes les repeticions de números de 
la llista. L'objectiu és tenir una llista on tots els números apareguin no més d'una vegada.

Nota: Assumiu que la llista original ja està dins del codi, no l'heu d'introduir des del teclat. Per descomptat, pots millorar el codi i afegir una part que 
pugui fer una conversa amb l'usuari i obtenir totes les dades.

Consell: Es recomanable que creeu una llista nova com a àrea de treball temporal, no necessiteu actualitzar la llista actual.

Podeu fer servir el següent codi com a plantilla:

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Escriu el teu codi aquí.
#
print("La llista amb elements únics:")
print(my_list)'''

my_list = [1, 2, 4, 4, 1, 4, 6, 2, 9]

for numero in my_list:
    if numero == my_list[0]:
        my_list.remove(numero)
    elif numero == my_list[1]:
        my_list.remove(numero)
    
print("La llista amb elements únics:")
print(my_list)