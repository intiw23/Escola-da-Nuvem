"""
Atividade Prática 07 - Escola da Nuvem
Autor: Walter
Versão: 1.2
Data de Início: 25/06/2025

Atividade 2 – Escrita de CSV

Objetivo:
Criar um script Python que escreva dados de pessoas em um arquivo CSV. 
O arquivo conterá informações como Nome, Idade e Cidade, organizadas em colunas.

Formato esperado:
Nome,Idade,Cidade
Alice,30,Salvador
Bruno,25,Fortaleza
Carla,28,Belo Horizonte
"""

import csv
from typing import List, Dict

#  Classe responsável por escrever uma lista de dicionários em um arquivo CSV
class EscritorCSV:

    def __init__(self, nome_arquivo: str, campos: List[str]):
        self.nome_arquivo = nome_arquivo
        self.campos = campos

    def escrever(self, dados: List[Dict[str, any]]) -> None:
        try:
            with open(self.nome_arquivo, mode='w', encoding='utf-8', newline='') as arquivo_csv:
                escritor = csv.DictWriter(arquivo_csv, fieldnames=self.campos)
                escritor.writeheader()
                escritor.writerows(dados)
            print(f"Arquivo '{self.nome_arquivo}' criado com sucesso.")
        except FileNotFoundError:
            print(f"Erro: caminho '{self.nome_arquivo}' inválido.")
        except PermissionError:
            print("Erro: permissão negada ao tentar escrever o arquivo.")
        except Exception as e:
            print(f"Erro inesperado ao criar o arquivo: {e}")


def obter_nome_arquivo() -> str:
    entrada = input("Digite o nome final do arquivo (.csv): ").strip().replace("-", "_").replace(" ", "_")
    
    if not entrada:
        raise ValueError("Nome do arquivo não pode ser vazio.")
    nome_formatado = entrada.replace(" ", "_")
    if not nome_formatado.endswith(".csv"):
        nome_formatado += ".csv"
    return nome_formatado


def obter_dados_exemplo() -> List[Dict[str, any]]:
    return [
        {"Nome": "Alice", "Idade": 30, "Cidade": "Salvador"},
        {"Nome": "Bruno", "Idade": 25, "Cidade": "Fortaleza"},
        {"Nome": "Carla", "Idade": 28, "Cidade": "Belo Horizonte"}
    ]


def main():
    try:
        nome_arquivo = obter_nome_arquivo()
        dados = obter_dados_exemplo()
        campos = ["Nome", "Idade", "Cidade"]
        escritor = EscritorCSV(nome_arquivo, campos)
        escritor.escrever(dados)

    except ValueError as ve:
        print(ve)
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()
