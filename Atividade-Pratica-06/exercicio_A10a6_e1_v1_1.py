"""
Atividade 6 – Gerador de Senha Aleatória

Aula 10 – 01/07/2025
C3 MAR - BRSAO 188 Noite – IA
Autor: Walter
Versão: 1.0

Exercício 1:
Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais,
possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.
"""

import random
import string

def gerar_senha(tamanho):
    if tamanho < 8:
        raise ValueError("A senha deve ter pelo menos 8 caractere.")
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("|-> Gerador de Senhas Aleatórias <-|")
    print("Digite '[sair]' para encerrar.\n")

    while True:
        entrada = input("|-> Digite o tamanho da senha desejada (ex: 12): ").strip()

        if entrada.lower() == "sair":
            print("Encerrando o gerador. Até logo!")
            break

        try:
            tamanho = int(entrada)
            senha = gerar_senha(tamanho)
            print(f"Senha gerada: {senha}\n")
        except ValueError as erro:
            print(f"Erro: {erro}\n")
        except Exception as e:
            print(f"Erro inesperado: {e}\n")

if __name__ == "__main__":
    main()
