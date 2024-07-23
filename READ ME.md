# ETL de Proposições Legislativas da ALMG

Este projeto realiza a extração, transformação e carregamento (ETL) de dados sobre proposições legislativas da Assembleia Legislativa de Minas Gerais (ALMG).

## Como executar

1. Certifique-se de ter o Docker e o Docker Compose instalados.
2. Clone este repositório.
3. Execute `docker-compose up -d --build` para iniciar os containers.

## Estrutura do projeto

- `docker-compose.yml`: Define os serviços Docker (banco de dados e aplicação).
- `Dockerfile`: Instruções para construir a imagem Docker da aplicação.
- `README.md`: Este arquivo de documentação.
- `requirements.txt`: Lista as dependências Python.
