#TUPLAS

my_tupla = (53, 'perro', 7.4, True)

# LA DIFERENCIA ENTRE TUPLA Y LISTA ES QUE A LAS TUPLAS NO SE LAS PUEDE MODIFICAR COMO SE HACE CON LAS LISTAS ADEMAS DE QUE ESTAS SE CREAN CON PARENTESIS () Y LAS LISTAS CON CORCHETES []

# La tupla funciona de la misma manera que las listas, es decir tienen las mismas funciones a excepcion de la suguiente

print(my_tupla.index('perro')) # Encuentra lo que nosotros queramos, nos marca su posicion aqui daria = 1


# DE ESTA MANERA SE CAMBIA EL TIPADO DE LA TUPLA A LISTA 

my_tupla = list(my_tupla)

print(type(my_tupla))

my_tupla.pop()

print(my_tupla)

my_tupla = tuple(my_tupla) # Cambia de lista a tupla
print(type(my_tupla))
print(my_tupla)