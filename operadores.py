# OPERADORES ARITMÉTICOS

print(6 + 3)
print(6 - 3)
print(6 * 3)
print(6 / 3)
print(6 // 3) # División de flor, borra la parte despues del punto para convertirlo en un int
print(6 % 3) # Resto de la división, es decir si, en la división de 7 / 3 sobra 1, el resultado de 7 % 3 será 1
print(6 ** 3) # Exponente = (6 * 6 * 6)

# Tambien se pueden utilizar los operadores para strings

a = 6
print("Hola " + "mundo") # Añade mundo enfrete de hola y se le añade un espaciado 
print("Hola " * 3) # Pone 3 veces hola
print('hola ' + str(6)) # Para añadir el 6 a la cadena de texto 'hola'
print('hola ' + str(a)) # Debe de ponerse así si es con variable


# OPERADORES OPERATIVOS 

print(6 < 3)
print(6 > 3)
print(6 <= 3)
print(6 == 3) # Un igual es para asignar
print(6 >= 3)
print(6 != 3)

print('hola' > 'mundo') # = False, cuenta el orden en el alfabeto
print('hola' > 'bolas') # = True, cuenta el orden en el alfabeto

print(len('hola') > len('holas')) # len() = Cuenta la cantidad de caracteres de la cadena de texto


# OPERADORES LOGICOS 

print(6 < 3 and 7 > 9) # and, si uno es false el resultado será false
print(6 < 3 and (True or False)) # se le pueden poner varios operadores 
print(6 < 3 and 7 > 9) # or, si uno es true, el resultado será true
print(not(4 > 6)) # not, cambia, es decir si es true = false, y si es false = true


# ejercicio

print('ejericico: ', not(7 != 7  and 6 > 5) and ('rozar' < 'rotar' or not(3 == 5))) # = true
