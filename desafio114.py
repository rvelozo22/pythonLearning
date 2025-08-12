import requests

url = 'http://www.pudim.com.br'

try:
    response = requests.get(url)
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print('A URL de destino não está acessível')

else:
    print('A URL de destino está acessível')