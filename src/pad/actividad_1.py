import json
import requests


class Ingestiones():
    def __init__(self):
        self.ruta_static="src/pad/static/"

    def leer_api(self, url):
        response = requests.get(url)
        return response.json()
    
    def escribir_json(self):
        pass

# vamos crea una intancia de la clase
ingestion = Ingestiones()
#datos_json = ingestion.leer_api("https://api.github.com/users/octocat")
#"https://api.nbp.pl/api/exchangerates/tables/{table}/"
datos_json = ingestion.leer_api("https://api.nbp.pl/api/exchangerates/tables/B/")
print("esta es la ruta statica :",ingestion.ruta_static)
print("datos json:",datos_json)



    