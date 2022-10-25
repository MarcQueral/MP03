'''x = int (input("Escriu un numero: "))

if (x>0):
    print(x,"és positiu")
elif (x==0):
    print(x,"és zero")
else:
    print(x,"és negatiu o igual a zero")'''

num=18
candidat=int(input("Tria un numero entre 1 i 100: "))

if (candidat>100 or num<0):
    print("T'he dit entre 0 i 100.")
elif (candidat>num):
    print("T'has passat.")
elif (candidat==num):
    print("L'has encertat!!")
else:
    print("El numero es més gran.")

