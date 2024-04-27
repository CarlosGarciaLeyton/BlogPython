#funcion que guarda resulta xxxx
'''def suma_lista():
    x = list()
    z = list()
    for i in range(0,3):
      b = int(input('Ingresa numero 1 :'))
      c = int(input('Ingresa numero 2 :'))
      d = int(input('Ingresa numero 3 :'))
      a = b + c + d
      lis.append(resultado_suma)
    lista_suma.append(lis)
    print(f'la suma : {lista_suma}')

suma_lista()'''

'''def suma():
  numero1 = int(input("Ingrese primer numero: "))
  numero2 = int(input("Ingrese segundo numero: "))
  numero3 = int(input("Ingrese tercer numero: "))
  return numero1 + numero2 + numero3

resultados = list()

resultados.append(suma())
print("La suma es:", resultados[-1])
resultados.append(suma())
print("La suma es:", resultados[-1])
resultados.append(suma())
print("La suma es:", resultados[-1])
print("Todos los resultados:", resultados)'''

secret_number = 20

while True:
    number = input('Ingresa un número:')

    try:
        number = int(number)
    except:
        print('Disculpa')
        continue
    if number != secret_number:
        if number > secret_number:
            print(number, 'Biennnnn')
        elif number < secret_number:
            print(number, 'ups')
    else:
        print('tu ', secret_number)
        break
