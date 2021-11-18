n=9
x=1
for i in range(0, n):
    for j in range(0, i+1):
        print(x,end="")
    print("\r")
    x+=1