'''num = int(input("Introdueix un numero entre 1 i 5: "))
while (num < 1 or num > 5):
    num = int(input("Torna a provar: "))
print("El programa ha acabat")'''


while True:
    linea = input("input> ")
    if linea(0) == '#':
        continue
    if linea == "fi":
        break
    print(linea.upper())
print("Acabat!")