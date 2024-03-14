# En una lista de numeros retorna el segundo número más grande; respuesta = 8

# my_list = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11]
# my_list.sort()
# print(my_list[-2])

# Crea una funcion que reciba días, horas, minutos y segundos (como list) y reotrne su resultado en milisegundos 

# def milisegundos(day = 0, horas = 0, minutos = 0, segundos = 0):
#     final_time = 0
#     horas =+ day * 24
#     minutos =+ horas * 60
#     segundos =+ minutos * 60
#     final_time =+ segundos * 1000
#     print(final_time)
    
# milisegundos(1)

# for number in range(100):
#     if number % 3 == 0 :
#         print('fizz')
#     if number % 5 == 0:
#         print('buzz')
#     if number % 3 == 0 and number % 5 == 0:
#         print('fizzbuzz') 
#     print(number)   


import random


def jugar():
    print('1 : Piedra')
    print('2 : Papel')
    print('3 : tijera')
    
    opciones = ['Piedra', 'Papel', 'Tijera']
    opciones_usuario = int(input('Elije una opcion (1,2,3)'))
    opciones_bot = random.randint(1,3)
    
    if opciones_usuario < 1 or opciones_usuario > 3:
        print('Esa opción no es valida')
        return
    print('Elegiste', opciones[opciones_usuario - 1])
    print('El bot eligió', opciones[opciones_bot - 1])
    
    if opciones_usuario == opciones_bot:
        print('Empate')
    elif (opciones_usuario == 1 and opciones_bot == 3) or (opciones_usuario == 2 and opciones_bot == 1) or (opciones_usuario == 3 and opciones_bot == 2):
        print('Ganaste')
    else:
        print('La maquina gana')


jugar()

