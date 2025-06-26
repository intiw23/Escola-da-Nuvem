"""
Atividade Prática 03 - Escola da Nuvem
Autor: Walter
Versão: 1.01
Data de Início: 25/06/2025

1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).
"""

def classificador_idade():
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Idade inválida.")
        elif idade <= 12:
            print("Categoria: Criança")
        elif idade <= 17:
            print("Categoria: Adolescente")
        elif idade <= 59:
            print("Categoria: Adulto")
        else:
            print("Categoria: Idoso")
    except ValueError:
        print("Por favor, digite uma idade válida.")

if __name__ == "__main__":
    classificador_idade()
