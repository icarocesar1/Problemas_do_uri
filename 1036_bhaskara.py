import math

a,b,c = input().split(" ")
a = float (a)
b = float(b)
c = float (c)

delta = b*b - 4*a*c 

if a!= 0 and delta >= 0 :
    r1 = (-b + math.sqrt(delta) )/ (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)
    print("R1 = %.5f" %r1)
    print ("R2 = %.5f"%r2)
else:
    print("Impossivel calcular")
