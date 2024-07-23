import re
from datetime import datetime
import json

def clean_text(text):
    if text:
        return re.sub(r'\s+', ' ', text).strip()
    return None

def clean_date(date_str):
    if date_str:
        try:
            return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z').isoformat()
        except ValueError:
            try:
                return datetime.strptime(date_str, '%Y-%m-%d').isoformat()
            except ValueError:
                return date_str
    return None

def transform_data(data):
    proposicoes = []
    tramitacoes = []
    for item in data['resultado']['listaItem']:
        proposicao = {
            'author': clean_text(item.get('autor')),
            'presentationDate': clean_date(item.get('dataPublicacao')),
            'ementa': clean_text(item.get('ementa')),
            'regime': clean_text(item.get('regime')),
            'situation': clean_text(item.get('situacao')),
            'propositionType': clean_text(item.get('siglaTipoProjeto')),
            'number': clean_text(item.get('numero')),
            'year': int(item.get('ano')),
            'city': 'Belo Horizonte',
            'state': 'Minas Gerais'
        }
        proposicoes.append(proposicao)

        if 'listaHistoricoTramitacoes' in item:
            for tram in item['listaHistoricoTramitacoes']:
                tramitacao = {
                    'createdAt': clean_date(tram.get('data')),
                    'description': clean_text(tram.get('historico')),
                    'local': clean_text(tram.get('local')),
                    'propositionId': len(proposicoes)
                }
                tramitacoes.append(tramitacao)
    
    return proposicoes, tramitacoes

# Lendo dados do arquivo JSON
with open('dadosdaapi.json', 'r', encoding='utf-8') as f:
    local_data = json.load(f)

proposicoes_data, tramitacoes_data = transform_data(local_data)

# Salvando dados transformados em novos arquivos JSON para verificação
with open('dados_transformados_proposicoes.json', 'w', encoding='utf-8') as f:
    json.dump(proposicoes_data, f, ensure_ascii=False, indent=4)

with open('dados_transformados_tramitacoes.json', 'w', encoding='utf-8') as f:
    json.dump(tramitacoes_data, f, ensure_ascii=False, indent=4)
