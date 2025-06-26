"""
Atividade Prática 03 - Escola da Nuvem
Autor: Walter
Versão: 1.01
Data de Início: 25/06/2025

4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100)
que não são divisíveis por 400.
"""

def verificador_ano_bissexto():
    try:
        ano = int(input("Digite o ano: "))
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f" {ano} é um ano bissexto.")
        else:
            print(f" {ano} não é um ano bissexto.")
    except ValueError:
        print(" Por favor, digite um ano válido.")

if __name__ == "__main__":
    verificador_ano_bissexto()
