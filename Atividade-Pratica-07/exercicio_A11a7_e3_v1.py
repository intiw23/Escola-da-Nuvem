"""
Atividade Prática 07 - Escola da Nuvem
Autor: Walter
Versão: 1.2
Data de Início: 25/06/2025

Atividade 03 – Leitura de CSV

Objetivo:
Criar um script Python que leia dados de um arquivo CSV com informações de pessoas,
e exiba essas informações no terminal, com tratamento de exceções.

Ler dados de um arquivo CSV contendo Nome, Idade e Cidade.
"""

import csv

# Lê dados de um arquivo CSV e retorna uma lista de registros.
def leitor_csv(nome_arquivo):
    caminho = nome_arquivo if nome_arquivo.lower().endswith('.csv') else f"{nome_arquivo}.csv"

    try:
        with open(caminho, mode="r", encoding="utf-8") as f:
            return list(csv.reader(f))
    except FileNotFoundError:
        print(f" Arquivo '{caminho}' não encontrado.")
    except Exception as e:
        print(f" Erro ao ler o arquivo: {e}")
    return []

def main():
    arquivo = input("Digite o nome do arquivo CSV (ex: pessoas_5.csv): ").strip()
    dados = leitor_csv(arquivo)

    if dados:
        print("\nConteúdo do arquivo:\n")
        for i, linha in enumerate(dados, 1):
            print(f"{i:02d}) {', '.join(linha)}")
    else:
        print("Nenhum dado a exibir.")

if __name__ == "__main__":
    main()
