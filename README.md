https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2024/IRD_2024_ESCOLAS.zip

etl-educacao/
├── README.md
├── requirements.txt
├── config/
│   └── aws_config.json
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
│   ├── download_data.py
│   ├── etl_pyspark.py
│   └── load_to_postgres.py
└── utils/
    └── s3_helper.py
