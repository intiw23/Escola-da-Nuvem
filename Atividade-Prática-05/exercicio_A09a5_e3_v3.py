"""
Atividade 5 – Cálculo da Idade em Dias

Aula 09 – 27/06/2025
C3 MAR - BRSAO 188 Noite – IA
Autor: Walter
Versão: 1.3

Enunciado:
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
A função deve considerar o ano atual como referência (obtido dinamicamente pelo módulo datetime).
Não é necessário considerar meses ou dias exatos — apenas o cálculo aproximado baseado em anos.

O programa deve solicitar o ano de nascimento ao usuário e exibir a idade estimada em dias.

- release v3 - inclui anos bissextos no cálculo

"""

from datetime import datetime

# contar_bissextos: Conta quantos anos bissextos existem entre dois anos (exclusivo do ano final).
def contar_bissextos(ano_inicio, ano_fim):
    bissextos = 0
    for ano in range(ano_inicio, ano_fim):
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            bissextos += 1
    return bissextos

# idade_em_dias: Calcula idade aproximada em dias considerando anos bissextos.
def idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    bissextos = contar_bissextos(ano_nascimento, ano_atual)
    return idade_anos * 365 + bissextos


# obter_ano_nascimento: Solicita e valida o ano de nascimento digitado pelo usuário.
def obter_ano_nascimento():
    ano_atual = datetime.now().year
    entrada = input("Digite o ano de nascimento: ").strip()
    if not entrada.isdigit():
        raise ValueError("Ano deve ser um número inteiro.")
    ano = int(entrada)
    if ano < 1900 or ano > ano_atual:
        raise ValueError(f"O ano deve estar entre 1900 e {ano_atual}.")
    return ano

def main():
    try:
        ano_nascimento = obter_ano_nascimento()
        dias = idade_em_dias(ano_nascimento)
        print(f"Você tem aproximadamente {dias} dias de vida.")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
