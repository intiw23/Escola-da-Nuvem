"""
Atividade Prática 03 - Escola da Nuvem
Autor: Walter
Versão: 1.01
Data de Início: 25/06/2025

3- Conversor de Temperatura

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja
converter.

As fórmulas matemáticas para a conversão entre as escalas Celsius, Fahrenheit e Kelvin.
Para converter Celsius em Fahrenheit: ºF = (9/5 x ºC) + 32.
Para converter Fahrenheit em Celsius: ºC = 5/9 x (ºF - 32).
Para converter Celsius em Kelvin: K = ºC + 273,15.
Para converter Kelvin em Celsius: ºC = K - 273,15.
Para converter Fahrenheit em Kelvin: K = (5/9 x (ºF - 32)) + 273,15.
Para converter Kelvin em Fahrenheit: ºF = (9/5 x (K - 273,15)) + 32."

"""

def conversor_temperatura():
    try:
        temp_input = input("Digite a temperatura: ").replace(",", ".")
        temp = float(temp_input)

        origem = input("Unidade de origem [°C]/[°F]/[°K] (C/F/K): ").strip().upper()
        destino = input("Unidade de destino [°C]/[°F]/[°K] (C/F/K): ").strip().upper()
        
        print("\n --------- cálculo -------------")
        print(f" Temperatura informada: {temp:.2f} °{origem}")
        
        if origem == destino:
            print(" A unidade de origem e destino são iguais. Nada a converter.")
            return

        if origem == "C":
            resultado = (temp * 9/5 + 32) if destino == "F" else (temp + 273.15)
        elif origem == "F":
            resultado = (temp - 32) * 5/9 if destino == "C" else ((temp - 32) * 5/9 + 273.15)
        elif origem == "K":
            resultado = (temp - 273.15) if destino == "C" else ((temp - 273.15) * 9/5 + 32)
        else:
            print(" Unidade de origem inválida. Use C, F ou K.")
            return

        print(f" Temperatura convertida: {resultado:.2f} °{destino}")
    except ValueError:
        print(" Valor de temperatura inválido. Use ponto (.) ou vírgula (,) como separador decimal.")

if __name__ == "__main__":
    conversor_temperatura()
