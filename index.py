#Objeto
'''class Auto:
    marca = ""
    color = ""
    encendido = True

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def encender(self):
        self.encendido = True

    def set_velocidad(self, velocidad):
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


#print(f'Marca: {auto1.marca}, Color: {auto1.color}')'''


#HERENCIA

class persona:
    def __init__(self, nombre, edad:float, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self) :
        print('nombre', self.nombre, 'edad:', self.edad, 'residencia', self.residencia)

    def valores(self):
            print('nombre', self.nombre, 'edad:', self.edad, 'residencia', self.residencia)


class empleado(persona):
    def __init__(self, salario, antiguedad, nombreEmpleado, resideciaEmpleado):
        super().__init__("jose", 23, "chile")
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):

        super().descripcion()
        print("salario: ", self.salario, "antiguedad: ", self.antiguedad)



class empleado_externo(persona):
    def __init__(self, salario, antiguedad, nombreEmpleado, resideciaEmpleado):
        super().__init__("jose_externo", 23, "peru")
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):

        super().descripcion()
        print("salario: ", self.salario, "antiguedad: ", self.antiguedad)

jose = empleado(1500.4, 15, "jose", "chile")
jose.descripcion()  #no puede tener la herecia de descripcion porque esta en empleado
jose1= empleado_externo(15001, 14, "jose_externo", "peru")
jose1.descripcion()

print(isinstance(jose, empleado))
print(isinstance(jose1, empleado_externo))
