"""
Atividade 3 – Validador de Senhas

Aula 7 – 26/06/2025
C3 MAR - BRSAO 188 Noite – IA
Autor: Walter
Versão: 1.0

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
tentativas = 0

while True:
    try:
        print(f"\n Tentativa {tentativas + 1}")
        
        senha = input(" Digite uma senha ou 'sair' para terminar: ")

        # Garante que a senha seja uma string (proteção adicional)
        if not isinstance(senha, str):
            raise ValueError("Entrada inválida.")

        senha = senha.strip().lower()  # Limpa espaços e normaliza

        if senha == "sair":
            print(" Encerrando o programa por solicitação do usuário.")
            break

        # Verifica tamanho mínimo
        if len(senha) < 8:
            print(" Senha muito curta! Deve ter no mínimo 8 caracteres.\n")
            continue

        # Verifica se há pelo menos um dígito numérico
        if not any(caractere.isdigit() for caractere in senha):
            print(" Senha fraca! Inclua pelo menos um número.\n")
            continue

        # Se passou por todas as verificações
        print(" Senha válida e forte!\n")
        break

    except ValueError as ve:
        print(f" Erro de valor: {ve}")

    except Exception as erro:
        print(f" Erro inesperado: {erro}")

    finally:
        tentativas += 1  # Incrementa contagem
        print(" Verificação encerrada nesta tentativa.\n")
