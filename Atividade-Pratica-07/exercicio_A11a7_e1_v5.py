"""
Atividade Prática 07 - Escola da Nuvem
Autor: Walter
Versão: 1.5
Data de Início: 25/06/2025

1- Atividade 1 - Estatísticas de treinamentos ML com Pandas

Objetivo:
Ler um arquivo CSV contendo dados de log de tempo de execução de modelos de Machine Learning.
Calcular:
- Média dos tempos de execução
- Desvio padrão dos tempos de execução

Formato esperado do CSV:
modelo,tempo_execucao
ModeloA,120
ModeloB,150
ModeloC,130
ModeloD,110
ModeloE,140
"""

import pandas as pd


def ler_csv(nome_base: str) -> pd.DataFrame | None:
    caminho = nome_base if nome_base.lower().endswith('.csv') else f"{nome_base}.csv"
    try:
        return pd.read_csv(caminho)
    except FileNotFoundError:
        print(f"Arquivo '{caminho}' não encontrado.")
    except pd.errors.EmptyDataError:
        print("O arquivo está vazio.")
    except pd.errors.ParserError:
        print("Erro de formatação no CSV.")
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
    return None

# Calcula média e desvio padrão da coluna 'tempo_execucao'.
def calcular_estatisticas(df: pd.DataFrame) -> tuple[float, float]:
    
    if 'tempo_execucao' not in df.columns:
        raise ValueError("Coluna 'tempo_execucao' não encontrada.")

    col = df['tempo_execucao'].dropna()
    if col.empty:
        raise ValueError("Coluna 'tempo_execucao' está vazia.")
    
    if len(col) < 2:
        raise ValueError("Precisa ao menos 2 valores válidos para calcular o desvio padrão.")

    return col.mean(), col.std()


def main():
    nome = input("Informe o nome do arquivo (.csv): ").strip()
    df = ler_csv(nome)
    if df is None:
        return

    try:
        media, desvio = calcular_estatisticas(df)
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio:.2f} segundos")
    except ValueError as e:
        print(f"Erro ao processar dados: {e}")


if __name__ == "__main__":
    main()
