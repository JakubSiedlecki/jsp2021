import math

a=int(input("Podaj współczynnik a: "))
b=int(input("Podaj współczynnik b: "))
c=int(input("Podaj współczynnik c: "))

if(a!=0):
    delta = b**2-4*a*c
    x1 = (-b+(delta)**(1/2))/(2*a)
    x2 = (-b-(delta)**(1/2))/(2*a)
    print(x1, x2)
else:
    print("Współczynnik a nie może być równy 0")