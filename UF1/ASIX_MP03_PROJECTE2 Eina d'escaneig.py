from subprocess import run
import time

'''Executo la comanda ip a per saber les interfícies de xarxa que té l'equip. Després realitzo un diccionari emmagatzemant el nom de la interfície i 
l'adreça ip amb el format següent: {‘eth0’:’192.168.203.100/24’}'''
result = run (["ip", "a"], capture_output = True, text = True) 
linies = result.stdout.split("\n")
lxarxes = {}
for i in range(len(linies)):
    linies[i] = linies[i].strip()
    if (linies[i][:4] == "inet"):
        lxarxes[linies[i].split(" ")[-1]] = linies[i].split(" ")[1]

print(lxarxes)

#En aquest pas demano a l'usuari que escrigui una adreça ip per tal de realitzar un escaneig a un equip amb la comanda nmap -sP.
ip = input("\nDisme una adreça IP de les que es veuen dalt per a fer un ping sweap a la XARXA amb nmap: ")
nmap = run (["nmap","-sP", ip])

#A les línies de codi de sota demano un rang de ports a l'usuari per realitzar un escaneig de ports a l'equip anterior
ports = input("\nEn aquest cas, disme un rang de ports per realitzar un escaneig sobre l'equip anterior (ex. 20-100): ")
nmap1 = run (["nmap","-p", ports, ip])

#Aqui realitzo el mateix que al pas anterior però per realitzar un escaneig de les versions dels serveis
print ("\n\nL'escaneig de les versions dels serveis és el següent: \n")
nmap2 = run (["nmap","-sV", ip])



'''print("Resultats:\n",lxarxes)
print("Codi Retorn:\n",result.returncode)
print("Tipus Error:\n",result.stderr)'''
