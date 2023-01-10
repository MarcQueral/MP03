'''Amb el que sabeu fins ara,crearem una eina d'escaneig per a Dummies!!

1. Escriviu un Script en python que en executar-se obtingui les ips de les interfícies i crei un diccionari amb el nom de la interfície com a clau 
   i la ip com a valor {‘eth0’:’192.168.203.100/24’}
2. L’script mostra els resultats per pantalla i l’usuari pot escollir una d’aquestes adreces per a fer un ping sweap a la XARXA amb nmap.
3. S’emmagatzema els resultats de les ips disponibles en una llista.
4. L’script mostra els resultats per pantalla i l’usuari pot escollir un equip per a realitzar un escaneig de ports i les versions dels serveis 
   que s’estan executant en ells. Els resultats s’emmagatzemen en un diccionari amb el format {port:versio_servei}
5. Els resultats es mostren per pantalla i l’usuari pot escollir un port per a realitzar un escaneig de vulnerabilitats.'''

from subprocess import run
import time

'''for i in range(10):
    print("Hola, com va tot?", i)
    time.sleep(2)
    run('clear')'''

result = run (["ip", "a"], capture_output = True, text = True) 
linies = result.stdout.split("\n")
lxarxes = []
for i in range(len(linies)):
    linies[i] = linies[i].strip()
    if (linies[i][:4] == "inet"):
        lxarxes.append(linies[i].split(" ")[-1])
        lxarxes.append(linies[i].split(" ")[1])


print(lxarxes)
resposta = input("\nSelecciona la interfície que vulguis saber: ")




'''print("Resultats:\n",lxarxes)
print("Codi Retorn:\n",result.returncode)
print("Tipus Error:\n",result.stderr)'''
