# 🏫 Projeto ETL - Dados da Educação

Este projeto é um pipeline de ETL (Extração, Transformação e Carga) para dados públicos da educação brasileira, utilizando ferramentas modernas e escaláveis como **AWS S3**, **PySpark** e **PostgreSQL**. É uma base para demonstrar conhecimentos técnicos em engenharia de dados e boas práticas de versionamento e organização de projetos.

## ⚙️ Tecnologias Utilizadas

- 🐍 Python 3.10.4
- ⚡ PySpark
- 🐘 PostgreSQL
- ☁️ AWS S3 (armazenamento de dados)
- 📦 Pandas (para testes e validações locais)

## 🗂️ Estrutura do Projeto

```
etl-educacao/
│
├── data/                # NÃO VERSIONADO - Dados brutos e processados
│
├── preparacao_testes/
│   ├── explorar                    # Explora o arquivo csv e o resultado do BD
│   ├── montar.py                   # Monta a estrutura da tabela do BD de acordo com o dataset
│   ├── preparar.py                 # Orquestra a preparação do BD
│   ├── spark_test.py               # Execução de testes locais com spark
│   └── testes_processamento_spark  # Testes locais com spark ultilizando o Jupyter Labs
│
├── scripts/
│   ├── download_data.py     # Script (exemplo) de extração de dados
│   ├── upload_to_s3.py      # Envio de dados brutos para o S3
│   └── etl_pyspark.py       # Job ETL principal com PySpark
│
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Executando o Projeto Localmente


### 1. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 2. Configure o acesso à AWS

Você precisa de uma conta AWS e das credenciais salvas localmente (via `aws configure`) para que o PySpark acesse o S3.

### 3. Execute o ETL

```bash
python scripts/etl_pyspark.py
```

> ⚠️ Certifique-se de que o Spark está corretamente instalado e configurado localmente.

## 📊 Fontes dos Dados

Os dados utilizados neste projeto vêm do **Censo Escolar da Educação Básica**, fornecido pelo **INEP (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira)**.

Link: [https://www.gov.br/inep/pt-br/assuntos/educacao-basica/censo-escolar](https://www.gov.br/inep/pt-br/assuntos/educacao-basica/censo-escolar)


## 📝 TODO

- [ ] Criar transformações adicionais (limpeza, joins, agregações)
- [ ] Configurar chaves de acesso para local não versionado
