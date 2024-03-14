# STRINGS

mi_primer_string = 'stirng con comillas simples'

#concatenar texto

print(f'si se pone asi, "{mi_primer_string}" puede seguir el texto despues de la variable')


#strings

segundo_string = 'hola'

a,b,c,d = segundo_string

print(a) #agarra la primera letra de la cadena de texto de la variable "segundo_string", es decir "a,b,c,d" estas variables puestas agarran una letra del texto en orden

# FUNCIONES PARA STRINGS

print(mi_primer_string.upper()) # Convierte la cadena de texto en mayúsculas
print(mi_primer_string.capitalize()) # Convierte la primera letra de la cadena de texto en mayúsculas
print(mi_primer_string.lower()) # Convierte la cadena de texto en minúscula
print(len(mi_primer_string)) # Contar la cantidad de caracteres
print(mi_primer_string.find('l')) # Encontrar la letra que se le pida, el numero que muestra es las posiciones es decir si "hola" y pides l será igual a 2 ya que está a dos pociones de la letra pedida
print(mi_primer_string.count('l')) # Cuenta la cantidad que se repite el mismo caracter, funciona hasta con numeros
print(mi_primer_string.upper().isupper()) # Pregunta si esta todo en mayúscula 