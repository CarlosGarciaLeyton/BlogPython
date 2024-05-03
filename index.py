#Objeto
class Auto:
    marca = ""
    color = ""
    encendido = True

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def encender (self):
        self.encendido = True

    def set_velocidad (self, velocidad):
        self.velocidad = velocidad


auto1 = Auto("SEAT", "AZUL")
auto1.encender()
auto1.set_velocidad(30)

if auto1.encendido:
    print(f'el auto esta encendido y va a una velocidad de {auto1.velocidad} km/h')
    auto1.set_velocidad(60)
    print(f'el auto esta encendido y va a una velocidad de {auto1.velocidad} km/h')
else:
    print('el auto esta apagado')

#print(f'Marca: {auto1.marca}, Color: {auto1.color}')
