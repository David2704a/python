# DICCIONARIOS = objeto

# MANERA DE LLENAR UN DICCIONARIOS

my_dict = {
        'Nombre' : 'Johan',
        3 : 'Bolaños',
        'Apodo' : 'David'}

print(type(my_dict))

print(my_dict['Nombre']) # = Johan, tambien se puede con numeros

print(my_dict[3]) # = Bolaños

print(my_dict.keys()) # = Trae todas las llaves
print(my_dict.values()) # = Trae todos los valores

#se pueden convertir en lista, set o tuplas, pero se guardarian son las llaves del diccionario(obejo)

my_dict = list(my_dict)

print(my_dict)