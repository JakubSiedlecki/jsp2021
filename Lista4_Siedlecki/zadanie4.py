def geometrycnzy(a,q,n):
    pot=int(pow(q,n-1))
    reasult=a*pot
    return reasult

n=int(input("Podaj szukany n-ty element ciągu: "))
x=input("1 - Wprowadź wartośći a,q.\n 2- Wykonaj dla zdefiniowanych wartośći.")

if x=='1':
    a=int(input("Podaj 1-szy element ciągu"))
    q=int(input("Podaj iloczyn ciągu"))
if x=='2':
    a=1
    q=2
print(n, "n-ty element ciągu wynosi:", geometrycnzy(a,q,n))
