# CONDICIONALES
numero = 7


my_set_1 = {
    'Johan',
    'Bolaños'
}

my_set_2 = {
    'Johan',
    'Bolaños',
    'David'
}

if my_set_1 == my_set_2:
    print("Los diccionarios son iguales")
elif my_set_1 != my_set_2:
    my_set_2.difference_update(my_set_1)
    print(my_set_2)
else:
    print("Los diccionarios son distintos")

# texto = 'orozco loca'
# if 4 > 6: 
#     print("4 es menor que 6")
# elif numero == 7:
#     print("numero es igual a 7")
# else:
#     print("numero es diferente de 7")

    
# if len(texto) >= 10: 
#     print("texto tiene 6 caracteres")
# else: 
#     print("texto no tiene 6 caracteres")
    