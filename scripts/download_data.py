import os
import requests

# URL do dataset público (exemplo: Censo Escolar)
DATA_URL = "https://download.inep.gov.br/dados_abertos/microdados_censo_escolar_2024.zip"

# Caminho local onde o arquivo será salvo
OUTPUT_ZIP_PATH = "data/raw/INSE_2021_escolas.zip"

# Pasta onde será extraído
EXTRACT_DIR = "data/raw/"

def download_file(url, output_path):
    print(f"Baixando arquivo de {url}...")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Download concluído: {output_path}")

def extract_zip(zip_path, extract_to):
    from zipfile import ZipFile
    print(f"Extraindo {zip_path}...")
    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extração concluída em: {extract_to}")

if __name__ == "__main__":
    os.makedirs(EXTRACT_DIR, exist_ok=True)
    download_file(DATA_URL, OUTPUT_ZIP_PATH)
    extract_zip(OUTPUT_ZIP_PATH, EXTRACT_DIR)
