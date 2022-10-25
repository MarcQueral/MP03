import random
num = int(input("Introdueix un numero entre 0 i 100: "))
num2 = random.randint(1, 100)
while (num < 1 or num > 100):
    if (num > num2):
        print("T'has passat")
    elif (num < num2):
        print("T'has quedat curt")
    if (num == num2):
        break
print("Acabat!")
#Falta acabar-lo!!