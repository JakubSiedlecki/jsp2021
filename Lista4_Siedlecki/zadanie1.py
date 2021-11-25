def iloczyn(list):
    result = 1
    for x in list:
        result = result*x
    return result


list=[]
n = int(input("Podaj ilość elementów w liście: "))
for i in range(0,n):
    element=int(input("Podaj elelemnt (liczba cąłkowita): "))
    list.append(element)

suma=sum(list)
print("Suma wszystkich elemntów listy: ") 
print(suma)

print("Iloczyn wsyzstkich elementów listy: ")
print(iloczyn)



    
