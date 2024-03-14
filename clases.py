# CLASES

class Persona:
    #self es la manera en que se guardan
    
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def comer(self):
        print(f'Las personas de {self.edad} años de edad, podrán comer')
        if self.edad == 18:
            print(f'Las personas de {self.edad} años de edad estan comiendo')
        else:
            print(f'Las personas de menos de 18 años de edad, mueranse de hambre')
        
humano_1 = Persona('Johan', 'Bolaños', 17)

print(humano_1 )
humano_1.comer()