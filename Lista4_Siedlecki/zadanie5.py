import itertools

lista=[]
n = int(input("Podaj ilość elementów w liście: "))
for i in range(0,n):
    element=int(input("Podaj elelemnt (liczba cąłkowita): "))
    lista.append(element)

print(list(itertools.permutations(lista)))