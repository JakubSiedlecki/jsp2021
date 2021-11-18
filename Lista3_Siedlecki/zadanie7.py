n=int(input("Podaj zakres\n"))
x=[0,1]
x[:] = list(map(int, x))            
i=2
print(x[0],x[1],sep="\n")
while x[i-1]+x[i-2]<=n:
    x.append(x[i-2]+x[i-1])
    print(x[i])
    i+=1
    