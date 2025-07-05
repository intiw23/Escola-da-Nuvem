"""
Atividade 6 – Consulta de Cotação de Moeda Estrangeira

Aula 10 – 01/07/2025
C3 MAR - BRSAO 188 Noite – IA
Autor: Walter
Versão: 1.0

Exercício 4

Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL).
O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual,
máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
"""

import requests
from datetime import datetime

def obter_cotacao(moeda: str) -> str:
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        dados = response.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            return "Moeda não encontrada ou não suportada pela API."

        cotacao = dados[chave]
        timestamp = int(cotacao.get("timestamp", 0))
        data_hora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")

        resultado = f"""
Cotação e {moeda} para BRL:
Valor atual: R$ {float(cotacao['bid']):.2f}
Valor máximo: R$ {float(cotacao['high']):.2f}
Valor mínimo: R$ {float(cotacao['low']):.2f}
Data/Hora da requisição: {data_hora}
Registro da cotação: datetime.strptime({cotacao['create_date', ""]}, "%Y-%m-%d %H:%M:%S")
"""
#Registro da cotação: {cotacao['create_date']}
        return resultado.strip()

    except requests.exceptions.Timeout:
        return "Erro: tempo de resposta excedido."
    except requests.exceptions.RequestException as e:
        return f"Erro de requisição: {e}"
    except KeyError:
        return "Dados inesperados na resposta da API."
    except ValueError:
        return "Erro ao converter dados numéricos."
    except Exception as e:
        return f"Erro inesperado: {e}"

def validar_codigo_moeda(codigo: str) -> bool:
    return codigo.isalpha() and len(codigo) == 3

if __name__ == "__main__":
    moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").strip().upper()
    if validar_codigo_moeda(moeda):
        resultado = obter_cotacao(moeda)
        print(resultado)
    else:
        print("Código de moeda inválido. Use exatamente 3 letras, como USD ou EUR.")
