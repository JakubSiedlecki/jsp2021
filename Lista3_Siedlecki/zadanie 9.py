m=int(input("Podaj ilość wierszy\n"))
n=int(input("Podaj ilość kolumn\n"))
i=int(1)
for i in range (1,m+1):
    j=int(1)
    for j in range (1,n+1):
        x=i*j
        print(x,"  ",end="")
        j+=1
    print("\r")
