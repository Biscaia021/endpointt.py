import requests

url = "http://127.0.0.1:8000/"

response = requests.get(url)

if response.status_code == 200:
    print("Resposta do servidor:", response.json())
else:
    print("Erro na requisição:", response.status_code)
