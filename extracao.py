import requests
import json

# URL da API
url = "https://dadosabertos.almg.gov.br/ws/proposicoes/pesquisa/direcionada?tp=1000&formato=json&ano=2023&ord=3"

# Requisição à API
response = requests.get(url)
data = response.json()

# Salvando os dados em um arquivo JSON para análise local
with open('dadosdaapi.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
