"""
Validador de Senhas
Aula 7 – 26/06/2025
C3 MAR - BRSAO 188 Noite – IA
Autor: Walter
"""

while True:
    try:
        senha = input("🔐 Digite uma senha ou 'sair' para terminar: ").lower()

        if senha == "sair":
            print("🚪 Encerrando...")
            break

        # Verifica tamanho mínimo
        elif len(senha) < 8:
            print("❌ Sua senha deve ter pelo menos 8 caracteres.")
            continue

        # Verifica se possui pelo menos um número
        if not any(caractere.isdigit() for caractere in senha):
            print("⚠️ Esta senha é fraca: deve conter pelo menos 1 número.")
            continue

        # Se passou por todas as verificações
        print("✅ Senha válida e forte!")
        break

    except ValueError:
        print("❌ Erro: Operação inválida!")

    finally:
        print("🔁 Verificação finalizada.\n")
