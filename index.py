import requests


#URL = "https://jsonplaceholder.typicode.com/users/1"
URL = "https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php"
responses = requests.get(URL)

#TODO
if responses.status_code == 200:
    print('Solicitud exitos')
    print('Data:', responses.json())



else:
    print('Error en la solicitud, detalle:', responses.text)
