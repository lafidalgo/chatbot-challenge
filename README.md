# Projeto de Protótipo de LLM e Microsserviços para Hotmart
Este projeto é parte do desafio proposto pela Hotmart, focado na criação de dois microsserviços utilizando um Vector Database e um Large Language Model (LLM) para processamento e busca de documentos de texto.

## Descrição do Projeto
O objetivo deste projeto é desenvolver dois microsserviços:

1. **Microsserviço de Processamento e Armazenamento**:
    * Recebe um documento de texto extraído de uma fonte específica.
    * Realiza o processamento desse documento e o armazena em um Vector Database open-source.

2. **API de Busca e Resposta**:
    * Dado um texto de entrada no formato de pergunta, busca no Vector Database os trechos relevantes.
    * Utiliza um LLM para gerar uma resposta com base nos trechos recuperados.

## Tecnologias Utilizadas
* **FastAPI**: Framework para desenvolvimento de APIs em Python.
* **Docker**: Para containerizar os microsserviços e o Vector Database.
* **OpenAI API**: Utilizada para geração de respostas usando um Large Language Model (LLM).
* **Vector Database**: Utilizar um Vector Database open-source para armazenar e recuperar informações relevantes.

## Estrutura do Projeto
```bash
.
├── api_search_response/
│   ├── app.py            # Código do microsserviço de busca e resposta
│   └── Dockerfile        # Dockerfile para construir o microsserviço
├── document_processor/
│   ├── app.py            # Código do microsserviço de processamento e armazenamento
│   └── Dockerfile        # Dockerfile para construir o microsserviço
├── vector_database/
│   ├── ...               # Configuração e scripts do Vector Database
├── docker-compose.yaml   # Arquivo Docker Compose para orquestrar os serviços
├── README.md             # Documentação do projeto
└── examples/             # Exemplos de entrada para testes (Postman, cURL, etc)
    ├── example_postman_collection.json
    └── ...
```


## Como Executar
Para executar este projeto localmente via Docker Compose, siga os passos abaixo:

1. **Configuração inicial**:
* Clone este repositório em sua máquina local.

2. **Configuração do ambiente**:
* Certifique-se de ter o Docker instalado em seu sistema.

3. **Construir e iniciar os serviços**:
* Navegue até o diretório raiz do projeto onde está o arquivo `docker-compose.yaml`.
* Execute o seguinte comando:

```bash
docker-compose up --build
```

4. **Testando os microsserviços**:
* Utilize os exemplos de entrada fornecidos na pasta `examples/` para testar as APIs.
* Você pode importar a coleção de exemplos no Postman (examples/example_postman_collection.json) para facilitar os testes.

## Exemplos de Entrada
Na pasta `examples/`, você encontrará exemplos de entrada para cada microsserviço, incluindo comandos cURL e scripts de shell para testes e reprodutibilidade.