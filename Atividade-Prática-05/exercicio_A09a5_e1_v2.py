"""
Atividade 5 – Cálculo da Gorjeta

Aula 09 – 27/06/2025
C3 MAR - BRSAO 188 Noite – IA
Autor: Walter
Versão: 1.2

Enunciado:
Crie uma função que calcule a gorjeta a ser deixada em um restaurante,
baseada no valor total da conta e na porcentagem de gorjeta desejada.

A função deve receber dois parâmetros:
1. valor_conta (float): o valor total da conta
2. porcentagem_gorjeta (float): a porcentagem desejada de gorjeta (ex: 10 para 10%)

A função deve retornar:
float: o valor da gorjeta calculada

O programa deve solicitar os valores ao usuário e exibir o valor da gorjeta a ser deixada.
"""

"""Calcula a gorjeta baseada no valor da conta e porcentagem."""
def calcular_gorjeta(valor_conta: float, porcentagem: float) -> float:
     return valor_conta * (porcentagem / 100)

"""
ler_float_positivo: Lê e valida um número float positivo do usuário.
Se limite_superior for definido, também valida o máximo.
Faz todo tratamento de exceção e retorna somente valor válido.
"""
def ler_float_positivo(mensagem: str, limite_superior=None) -> float:
    while True:
        entrada = input(mensagem).strip().replace(',', '.')
        try:
            valor = float(entrada)
            if valor <= 0:
                print(" O valor deve ser maior que zero.")
            elif limite_superior is not None and valor > limite_superior:
                print(f" O valor deve ser menor ou igual a {limite_superior}.")
            else:
                return valor
        except ValueError:
            print(" Entrada inválida. Digite apenas números, sem letras ou símbolos.")

def main():
    print("=== -> Calculadora de Gorjeta <- ===")
    conta = ler_float_positivo("Digite o valor total da conta (R$): ")
    porcentagem = ler_float_positivo("Digite a porcentagem da gorjeta (%): ", limite_superior=100)
    gorjeta = calcular_gorjeta(conta, porcentagem)
    print(f"\nGorjeta a ser deixada: R$ {gorjeta:.2f}")

if __name__ == "__main__":
    main()
