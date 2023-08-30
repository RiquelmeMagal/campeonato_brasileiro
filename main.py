import os
import csv
import json
from collections import defaultdict

# Caminho relativo para o arquivo CSV
caminho_arquivo_csv = "estatistica/campeonato-brasileiro-gols.csv"

# Dicionário para armazenar os dados dos jogadores por time
dados_por_time = defaultdict(list)

# Abrir o arquivo CSV
with open(caminho_arquivo_csv, "r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for linha in csv_reader:
        clube = linha["clube"]
        if clube:  # Verificar se o campo "clube" não está vazio
            dados_por_time[clube].append(linha)

# Caminho para a pasta onde os JSONs por time serão salvos
caminho_pasta_times = "times_data"

# Criar a pasta se ela não existir
os.makedirs(caminho_pasta_times, exist_ok=True)

# Salvar os dados por time em arquivos JSON separados
for time, dados in dados_por_time.items():
    caminho_arquivo_json = os.path.join(caminho_pasta_times, f"{time}.json")
    with open(caminho_arquivo_json, "w", encoding="utf-8") as json_file:
        json.dump(dados, json_file, ensure_ascii=False, indent=4)

print("Dados dos times extraídos, transformados e salvos em JSON por time.")
