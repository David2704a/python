# LISTAS
#list = array
lista1 = ['Python', 53, False]

print(type(lista1)) # = list


print(lista1) # = ['Python', 53, False]
print(lista1[1]) # = [53], porque empieza desde cero
print(lista1[-1]) # = [False], porque si se le pone un numero negativo empieza de atras hacia adelante inicializandose en 1

lista1.append('53') # añadir objeto a la lista
lista1.insert(3, 'hola') # añadir objeto a la lista marcandole su posicion
lista1.remove('hola') # remover objeto de la lista 
lista1.pop(2) # remover objeto de la lista marcandole su posicion
print(lista1.pop(2)) # muestra el objeto removido
lista1.reverse() # pone la lista al reves
lista1.clear() # Vacía la lista
print(lista1)