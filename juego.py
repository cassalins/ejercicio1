import random

random.randint(0,10)
import datetime

datetime.datetime.utcnow()
inicio=datetime.datetime.utcnow()
b = 0
m = 0
v = 0
print("escriba el resultado de la siguiente operacion")

for i in range(10):
    z = random.randint(0, 9)
    y = random.randint(0, 9)

    b=z+y
    print ()
    a=input ("{} + {}".format(z,y))

    if int(a) == z+y:
        print ("correcto")
        v=v+1
    else:
        print("Falso")
        m=m+1
fin=datetime.datetime.utcnow()

print("respuestas correctas",v)
print("respuestas falsas",m)
print("tiempo requerido",fin-inicio)
