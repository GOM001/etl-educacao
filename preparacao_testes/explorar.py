# explorar.py

import pandas as pd
from typing import List, Tuple, Any

# -----------------------------
# 1. Explorar um arquivo CSV
# -----------------------------

def explorar_csv(caminho_arquivo: str, n_linhas: int = 5) -> None:
    """
    Mostra as colunas e as primeiras n_linhas do CSV.
    """
    df = pd.read_csv(caminho_arquivo)
    print("\n📌 Colunas:")
    print(df.columns.tolist())
    
    print(f"\n📊 Primeiras {n_linhas} linhas:")
    print(df.head(n_linhas))


# --------------------------------------
# 2. Explorar resultado do PostgreSQL
# --------------------------------------

def explorar_resultado_pg(colunas: List[str], linha: Tuple[Any]) -> None:
    """
    Exibe o conteúdo de uma linha do banco PostgreSQL com os nomes das colunas.
    """
    print("\n📋 Resultado da linha do banco:")
    for nome, valor in zip(colunas, linha):
        print(f"{nome}: {valor}")
