import os
import json
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Definindo a base declarativa
Base = declarative_base()

# Definindo a tabela de proposições
class Proposicao(Base):
    __tablename__ = 'proposicao'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String)
    presentationDate = Column(DateTime)
    ementa = Column(String)
    regime = Column(String)
    situation = Column(String)
    propositionType = Column(String)
    number = Column(String)
    year = Column(Integer)
    city = Column(String)
    state = Column(String)

# Definindo a tabela de tramitações
class Tramitacao(Base):
    __tablename__ = 'tramitacao'
    id = Column(Integer, primary_key=True, autoincrement=True)
    createdAt = Column(DateTime)
    description = Column(String)
    local = Column(String)
    propositionId = Column(Integer, ForeignKey('proposicao.id'))

# Caminho dos arquivos JSON transformados
proposicoes_file_path = 'dados_transformados_proposicoes.json'
tramitacoes_file_path = 'dados_transformados_tramitacoes.json'

# Lendo dados transformados dos arquivos JSON
with open(proposicoes_file_path, 'r', encoding='utf-8') as f:
    proposicoes_data = json.load(f)

with open(tramitacoes_file_path, 'r', encoding='utf-8') as f:
    tramitacoes_data = json.load(f)

# Conectando ao banco de dados
DATABASE_URI = 'postgresql://postgres:061803398@localhost:5432/postgres'
if not DATABASE_URI:
    raise ValueError("DATABASE_URI não está definido corretamente. Verifique a configuração.")

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Inserindo proposições no banco de dados
for proposicao in proposicoes_data:
    session.add(Proposicao(**proposicao))

# Inserindo tramitações no banco de dados
for tramitacao in tramitacoes_data:
    session.add(Tramitacao(**tramitacao))

# Commitando as transações
session.commit()
session.close()
