"""
Atividade Prática 07 - Escola da Nuvem
Autor: Walter
Versão: 1.21
Data de Início: 25/06/2025

Atividade 4 – Leitura e Escrita de arquivos JSON com pandas

Objetivo:
Criar um script Python que leia e escreva dados em um arquivo JSON utilizando a biblioteca pandas.
O arquivo deve conter informações sobre uma pessoa com os campos: nome, idade e cidade.
O script deve:
1. Escrever esses dados em um arquivo JSON.
2. Ler o conteúdo e exibir os dados da pessoa.
"""

import pandas as pd
from pathlib import Path

def escrever_json_com_pandas(caminho_arquivo: str, dados: dict) -> None:
    try:
        df = pd.DataFrame([dados])  # lista com um único dicionário
        df.to_json(caminho_arquivo, orient='records', indent=4, force_ascii=False)
        print(f"Arquivo '{caminho_arquivo}' criado com sucesso.")
    except Exception as e:
        print(f"Erro ao escrever o arquivo JSON com pandas: {e}")

def ler_json_com_pandas(caminho_arquivo: str) -> None:
    if not Path(caminho_arquivo).is_file():
        print(f"Arquivo '{caminho_arquivo}' não encontrado.")
        return

    try:
        df = pd.read_json(caminho_arquivo)
        for index, row in df.iterrows():
            print("Dados carregados:")
            print(f"Nome: {row.get('nome', 'Desconhecido')}")
            print(f"Idade: {row.get('idade', 'Desconhecida')}")
            print(f"Cidade: {row.get('cidade', 'Desconhecida')}")
    except Exception as e:
        print(f"Erro ao ler o arquivo JSON com pandas: {e}")

def main():
    pessoa = {
        "nome": "Lucas Lima",
        "idade": 23,
        "cidade": "Curitiba"
    }

    nome_arquivo_base = input("Digite o nome que será salvo (sem extensão): ").strip().replace("-", "_").replace(" ", "_")
    
    if not nome_arquivo_base:
        print("Nome de arquivo inválido.")
        return

    nome_arquivo = f"{nome_arquivo_base}.json"
    escrever_json_com_pandas(nome_arquivo, pessoa)
    ler_json_com_pandas(nome_arquivo)

if __name__ == "__main__":
    main()
