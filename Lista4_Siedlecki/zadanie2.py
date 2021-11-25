def function(lista):
    lista=list(dict.fromkeys(lista))            #usuwa powtórzenia w liście
    return lista

lista=[]
n = int(input("Podaj ilość elementów w liście: "))
for i in range(0,n):
    element=int(input("Podaj elelemnt (liczba cąłkowita): "))
    lista.append(element)

print("Lista bez powtórzeń: ", function(lista))
