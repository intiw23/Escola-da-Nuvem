"""
Atividade 5 – Verificador de Palíndromo

Aula 09 – 27/06/2025
C3 MAR - BRSAO 188 Noite – IA
Autor: Walter
Versão: 1.2

Enunciado:
Crie uma função que verifique se uma palavra ou frase é um palíndromo.
Um palíndromo é uma sequência que pode ser lida da mesma forma de trás para frente,
ignorando espaços e pontuação.

A função deve retornar:
- "Sim" se for palíndromo
- "Não" caso contrário

Esse exercício desenvolve habilidades com strings e manipulação de texto.
"""

"""
eh_palindromo: Retorna "Sim" se a frase for palíndromo, "Não" caso contrário.
Ignora espaços e pontuação.
"""
def eh_palindromo(frase: str) -> str:
    if not isinstance(frase, str) or not frase.strip():
        raise ValueError("A entrada deve ser uma palavra ou frase não vazia.")
    texto = ''.join(c.lower() for c in frase if c.isalnum())
    return "Sim" if texto == texto[::-1] else "Não"

def main():
    print("=== -> verifica se uma palavra ou frase é um palíndromo <- ===")
    exemplos = [
        "O lobo ama o bolo",
        "Amor a Roma",
        "Python é legal",
        "123+wer K rew-321"
    ]
    for frase in exemplos:
        print(f'"{frase}": {eh_palindromo(frase)}')

if __name__ == "__main__":
    main()

# Uso individual:
# frase = "O lobo ama o bolo"
# resultado = eh_palindromo(frase)
# print("É palíndromo?", resultado)