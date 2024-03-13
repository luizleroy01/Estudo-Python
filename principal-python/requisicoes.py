#use of requisition with python

print("Importação e uso de modulos de terceiros")

import requests

url = "https://example.com"
response = requests.get(url)

print(f"Solicitação HTTP para a url : {url} retornou status :{response.status_code}")