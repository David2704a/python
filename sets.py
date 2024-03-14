# SETS

# LOS SETS NO TIENEN NINGUN TIPO DE ORDEN, ES DECIR SI PRIMERO TE LOS MUESTRA ASI EN ESE ORDEN"{'python', 'JacaScript', 'C++'}", LUEGO TE LOS MOSTRARA EN UN ORDEN DIFERENTE, NO TIENE POSICIONES

my_set = {}

print(type(my_set)) # = Diccionario, debe tener un contenido para que sea un set

my_set = {'python', 'JacaScript', 'C++'}

print(type(my_set)) # = set

# print(my_set[0]) # = ERROR

# NO DEJA REPETIR VALORES ES DECIR SI YA TENEMOS C++ Y SE PONE DE ESTA MANERA

my_set.add('C++')
print(my_set)
# SIMPLEMENTE MOSTRARÁ LOS MISMOS TRES VALORES INICALES, ES DECIR NO AÑADIRÁ EL VALOR 'C++' PORQUE YA EXISTE EN EL SET
my_set.add('PHP')
print(my_set)
# SI ES DIFERENTE EL VALOR, SI LO AÑADIRÁ


#DIFERENCIA ENTRE SETS

my_set_0 = {'python', 'JacaScript', 'C++'}

my_set.difference_update(my_set_0) # Esto muestra la diferencia que hay entre los dos sets, por ejemplo en este caso seria PHP y lo almacena en my_set

print(my_set)
