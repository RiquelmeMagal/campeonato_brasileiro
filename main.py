import os
import csv
import json
from collections import defaultdict

# Função para realizar o ETL e salvar em JSON
def processar_csv_e_salvar_json(tipo_arquivo, caminho_arquivo_csv):
    # Dicionário para armazenar os dados dos jogadores por time
    dados_por_time = defaultdict(list)

    # Abrir o arquivo CSV
    with open(caminho_arquivo_csv, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            clube = linha["clube"]
            if clube:  # Verificar se o campo "clube" não está vazio
                dados_por_time[clube].append(linha)

    # Criar a pasta do tipo de arquivo se ela não existir
    caminho_pasta_tipo_arquivo = os.path.join("times_data", tipo_arquivo)
    os.makedirs(caminho_pasta_tipo_arquivo, exist_ok=True)

    # Salvar os dados por time em arquivos JSON separados
    for time, dados in dados_por_time.items():
        caminho_arquivo_json = os.path.join(caminho_pasta_tipo_arquivo, f"{time}.json")
        with open(caminho_arquivo_json, "w", encoding="utf-8") as json_file:
            json.dump(dados, json_file, ensure_ascii=False, indent=4)

    print(f"Dados do tipo '{tipo_arquivo}' dos times extraídos, transformados e salvos em JSON por time.")

# Lista de arquivos CSV disponíveis e seus tipos
arquivos_csv_disponiveis = [
    ("campeonato-brasileiro-cartoes.csv", "cartoes"),
    ("campeonato-brasileiro-estatisticas-full.csv", "estatisticas"),
    ("campeonato-brasileiro-full.csv", "full"),
    ("campeonato-brasileiro-gols.csv", "gols")
]

# Mostrar opções ao usuário
print("Escolha um dos tipos de arquivo CSV para processar:")
for i, (arquivo, tipo) in enumerate(arquivos_csv_disponiveis, start=1):
    print(f"{i}. {tipo}")

# Obter a escolha do usuário
escolha = int(input("Digite o número correspondente ao tipo de arquivo escolhido: ")) - 1

# Verificar se a escolha é válida
if 0 <= escolha < len(arquivos_csv_disponiveis):
    arquivo_escolhido, tipo_arquivo = arquivos_csv_disponiveis[escolha]
    caminho_arquivo_csv = os.path.join("estatistica", arquivo_escolhido)
    processar_csv_e_salvar_json(tipo_arquivo, caminho_arquivo_csv)
else:
    print("Escolha inválida.")
