import requests


URL = "https://jsonplaceholder.typicode.com/users/1"
responses = requests.get(URL)

if responses.status_code == 400:
    print('Solicitud exitos')
    print('Data:', responses.json())
else:
    print('Error en la solicitud, detalle:', responses.text)
