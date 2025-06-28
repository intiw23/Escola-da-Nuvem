"""
Atividade Prática 03 - Escola da Nuvem
Autor: Walter
Versão: 1.01
Data de Início: 25/06/2025

2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""

def calculadora_imc():
    try:
        peso_input = input("Digite seu peso (kg): ").replace(",", ".")
        altura_input = input("Digite sua altura (m): ").replace(",", ".")

        peso = float(peso_input)
        altura = float(altura_input)

        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser valores positivos.")
            return

        print(f" Peso informado: {peso:.2f} kg")
        print(f" Altura informada: {altura:.2f} m")

        imc = peso / (altura ** 2)
        print(f" Seu IMC é: {imc:.2f}")
        if imc < 18.5:
            print(" Classificação: Abaixo do peso")
        elif imc < 25:
            print(" Classificação: Peso normal")
        elif imc < 30:
            print(" Classificação: Sobrepeso")
        else:
            print(" Classificação: Obeso")

    except ValueError:
        print(" Entrada inválida. Use números válidos como 72.3 ou 1.75")

if __name__ == "__main__":
    calculadora_imc()
