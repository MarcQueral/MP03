'''diccionari = {}
diccionari['one'] = 'un'
diccionari['two'] = 'dos'
diccionari['three'] = 'tres'
print(diccionari ['two'], diccionari ['three'])'''

'''pesos = {}
pesos['Pepe'] = [30,55,57]
pesos['Victor'] = [40,64,59]
pesos['Julia'] = [67,70,65]
print(pesos['Pepe'])'''

'''pesos = {'Pepe':[30,55,57], 'Victor':[40,64,59], 'Julia':[67,70,65]}
print(pesos['Pepe'])
print(len(pesos))
print('Julia' in pesos)'''

'''pesos = {'Pepe':[30,55,57], 'Victor':[40,64,59], 'Julia':[67,70,65]}
x=int(input("Introdueix un nou pes per a Pepe: "))
pesos['Pepe'].append(x)
print("Pesos de Pepe: ",pesos['Pepe'])'''

pesos = {'Pepe':[50,55,57], 'Victor':[60,64,69], 'Julia':[67,70,65]}
persona = input("Dis-me a qui vols afegir-li un pes: ")
x=int(input("Introdueix el nou pes: "))
pesos[persona].append(x)
print("Els pesos de", persona, "són:", pesos[persona])