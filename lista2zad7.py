list=[(2, 8),(5, 5),(9, 3),(1, 0),(3, 2),(6, 4),(1, 9),(10, 3),(2, 3),(1, 7)]     #używałem infromacji z tej strony https://www.kite.com/python/answers/how-to-sort-a-list-of-tuples-by-the-second-value-in-python
print(list)
list.sort(key=lambda x:x[1])                                                      #key=lambda, definiuje względem którego elementu jest sortowana nasza lista  
print(list)