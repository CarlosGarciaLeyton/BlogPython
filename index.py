import requests


#URL = "https://jsonplaceholder.typicode.com/users/1"
#URL = "https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php"
#response = requests.get(URL)

#responses = requests.get(files=local_id)


#TODO
'''if response.status_code == 200:
    if response.text == "quilpue":
        print('Solicitud exitosa local')
    print('Solicitud exitosa')
    print('Data:', response.json())

else:
    print('Error en la solicitud, detalle:', response.text)'''

"""number = int(input("Ingresa un número: "))
number1 = int(input("ingresa otro numero"))
resultado = 0
if number > 0 and number1 > 0:
    resultado = number + number1
    print ("la suma es:",resultado)
else:
    print("alguno de estos números no es mayor a 0")"""

#FOR
'''table = float(input ('¿Que tabla quieres ver?'))
nums = range (0,5)'''

'''for num in nums:
    print(num)
    print (f'{table} - {num} = ?')
    print (f'{table} - {num} = {table - num}')'''

opc = int(input('¿Que deseas seleccionar ?'))
def seleccion_usuario(opc):
    match opc:
        case 1:
            ordenar_lista()


def ordenar_lista():
    lis = list()
    number_range = int(input('¿Que rango quieres ?'))
    for i in range(1,number_range):
      numeros = int(input('¿Que tabla quieres ver?'))
      lis.append(numeros)
      lis.sort()
      print(f'la lista ordenada es : {lis}')

ordenarLista()
opc = int(input('¿Que deseas seleccionar ?'))
def seleccion_usuario(opc):
    match opc:
        case 1:
            ordenar_lista()


def ordenar_lista():
    lis = list()
    number_range = int(input('¿Que rango quieres ?'))
    for i in range(1,number_range):
      numeros = int(input('¿Que tabla quieres ver?'))
      lis.append(numeros)
      lis.sort()
      print(f'la lista ordenada es : {lis}')

ordenarLista()




#print(f'lista normal : {lis}')
#print(f'la lista ordenada es : {lis}')
    #lista.append((i*number))
#print ("la tabla del numero es", number,"es",lista)


