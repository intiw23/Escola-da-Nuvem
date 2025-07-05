"""
Atividade 6 – Consulta de Endereço via CEP

Aula 10 – 01/07/2025
C3 MAR - BRSAO 188 Noite – IA
Autor: Walter
Versão: 1.0

Exercício 3

Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário,
utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
"""

import requests
import re

def consultar_cep(value):
    url = f"https://viacep.com.br/ws/{value}/json/"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        dados = response.json()

        if dados.get("erro"):
            return None  # CEP não existe
        else:
            return f"""
Endereço encontrado:
Logradouro: {dados.get('logradouro', 'N/A')}
Bairro: {dados.get('bairro', 'N/A')}
Cidade: {dados.get('localidade', 'N/A')}
Estado: {dados.get('uf', 'N/A')}
""".strip()

    except requests.exceptions.RequestException as e:
        return f"Erro na requisição: {e}"
    except Exception as e:
        return f"Erro inesperado: {e}"

def main():
    print("|-> Consulta de Endereço via CEP <-|")
    print("Digite '[sair]' para encerrar.\n")

    while True:
        entrada = input("Digite o CEP (ex: 21941-070): ").strip()
        
        if entrada.lower() == "sair":
            print("Encerrando o programa.")
            break

        cep = re.sub(r"\D", "", entrada)

        if len(cep) != 8:
            print("CEP inválido. Deve conter exatamente 8 números.\n")
            continue

        resultado = consultar_cep(cep)

        if resultado is None:
            print("CEP não encontrado. Tente novamente.\n")
        elif isinstance(resultado, str):
            print(resultado)
            break
        else:
            print("Ocorreu um erro inesperado. Tente novamente.\n")

if __name__ == "__main__":
    main()
