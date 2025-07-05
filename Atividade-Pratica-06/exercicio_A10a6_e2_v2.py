"""
Atividade 6 – Gerador de Perfil Aleatório

Aula 10 – 01/07/2025
C3 MAR - BRSAO 188 Noite – IA
Autor: Walter
Versão: 2.0

Exercício 2 (Alternativo com biblioteca Faker)

Crie um programa que gera um perfil de usuário aleatório utilizando a biblioteca 'Faker'.
O programa deve exibir:
- Nome completo
- E-mail
- CPF (no caso estamos no Brasil)
- País

Este exercício simula dados realistas para testes e desenvolvimento de aplicações.
"""

from faker import Faker
import sys

fake = Faker("pt_BR")

def gerar_usuario():
    try:
        nome = fake.name()
        email = fake.email()
        cpf = fake.cpf()
        pais = fake.current_country()

        user = f"""
|-> Perfil Aleatório Gerado com Faker <-|
Nome : {nome}
Email: {email}
CPF  : {cpf}
País : {pais}
"""
        return user

    except Exception as e:
        return f"Ocorreu um erro ao gerar o perfil: {e}"

def main():
    usuario = gerar_usuario()
    print(usuario)

if __name__ == "__main__":
    main()
