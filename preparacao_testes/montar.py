# etl/montar.py

import pandas as pd
import psycopg2

def inferir_tipo_sql(dtype):
    if pd.api.types.is_string_dtype(dtype):
        return "TEXT"
    elif pd.api.types.is_integer_dtype(dtype):
        return "INTEGER"
    elif pd.api.types.is_float_dtype(dtype):
        return "FLOAT"
    elif pd.api.types.is_bool_dtype(dtype):
        return "BOOLEAN"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "TIMESTAMP"
    else:
        return "TEXT"

def montar_tabela_automatica(csv_path, nome_tabela, conn_params):
    print(f"📥 Lendo CSV de: {csv_path}")
    df = pd.read_csv(csv_path, encoding='latin1', sep=';')

    print("🧠 Inferindo tipos...")
    colunas_sql = []
    for col in df.columns:
        tipo_sql = inferir_tipo_sql(df[col].dtype)
        colunas_sql.append(f'"{col}" {tipo_sql}')
    
    colunas_str = ", ".join(colunas_sql)
    comando_sql = f'CREATE TABLE IF NOT EXISTS "{nome_tabela}" ({colunas_str});'

    print("📡 Conectando ao PostgreSQL...")
    conn = psycopg2.connect(dbname=conn_params.get('dbname'),host= conn_params.get('host'), user=conn_params.get('user') , password=conn_params.get('password'))
    cur = conn.cursor()

    print(f"🚧 Criando a tabela '{nome_tabela}'...")
    cur.execute(comando_sql)
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Tabela criada com sucesso.")

