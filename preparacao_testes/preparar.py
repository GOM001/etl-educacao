from montar import montar_tabela_automatica
import os

base_dir = os.path.dirname(__file__)

csv_path = os.path.abspath(os.path.join(base_dir, "..", "data", "raw","dados_educacao.csv"))

nome_tabela = "escolas"

conn_params = {
    "dbname": "etl_escolas",
    "user": "postgres",
    "password": "Il0v3luc4s",
    "host": "database-1.cklqusaq41x8.us-east-1.rds.amazonaws.com",
    "port": "5432"
}

montar_tabela_automatica(csv_path, nome_tabela, conn_params)
