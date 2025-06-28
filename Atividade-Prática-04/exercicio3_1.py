"""
Atividade 3 – Validador de Senhas

Aula 7 – 26/06/2025
C3 MAR - BRSAO 188 Noite – IA
Autor: Walter
Versão: 1.2

Enunciado:
Crie um programa que verifique se uma senha é forte.
Uma senha forte deve ter:
- Pelo menos 8 caracteres
- Pelo menos um número

O programa deve continuar pedindo senhas até que uma senha válida seja inserida
ou o usuário digite 'sair'.

O programa deve utilizar apenas os laços estudados:
- while, - for, - if, - break, - continue,
- try / except (com erros específicos),
- finally
"""

tentativas = 0  # Contador de tentativas

while True:
    try:
        print(f"\n -> Tentativa {tentativas + 1}")
        senha = input("-> Digite uma senha ou ['sair'] para terminar: ")

        if not isinstance(senha, str):
            raise ValueError("Entrada inválida.")

        senha = senha.strip().lower()

        if senha == "sair":
            print(" Encerrando o programa por solicitação do usuário.")
            break

        erros = []  # Lista para mensagens de erro

        if len(senha) < 8:
            erros.append("- Senha muito curta! Deve ter no mínimo 8 caracteres.")

        if not any(c.isdigit() for c in senha):
            erros.append("- Senha fraca! Inclua pelo menos um número.")

        if erros:
            print("\n".join(erros))  # Mostra todos os erros encontrados
            continue

        print("-> Senha válida e forte!\n")
        break

    except ValueError as ve:
        print(f"-> Erro de valor: {ve}")

    except Exception as erro:
        print(f"-> Erro inesperado: {erro}")

    finally:
        tentativas += 1
        print(" Verificação encerrada nesta tentativa.\n")
