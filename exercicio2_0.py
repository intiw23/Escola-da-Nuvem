"""
Atividade 2 – Registro de Notas da Turma

Aula 7 – 26/06/2025
C3 MAR - BRSAO 188 Noite – IA
Autor: Walter
Versão: 1.0

Enunciado:
Crie um programa que permita a um professor registrar as notas de uma turma.
O programa deve continuar solicitando notas até que o professor digite 'fim'.
Notas válidas são de 0 a 10. Notas inválidas devem ser ignoradas.
Ao final, deve ser exibida a média da turma.
"""

notas = []      # Lista para armazenar as notas válidas
tentativas = 0  # Contador de tentativas

while True:
    try:
        print(f"\n📌 Tentativa {tentativas + 1}")
        entrada = input("✏️ Digite a nota da turma ou 'fim' para terminar: ").strip().lower()

        if entrada == "fim":
            print("✅ Registro de notas encerrado.")
            break

        nota = float(entrada.replace(",", "."))  # Aceita ponto ou vírgula

        # Verifica se está dentro da faixa permitida
        if 0 <= nota <= 10:
            notas.append(nota)
            print(f"✔️ Nota registrada: {nota}")
        else:
            print("❌ Nota fora do intervalo permitido (0 a 10).")

    except ValueError:
        print("⚠️ Erro: Entrada inválida. Digite um número entre 0 e 10 ou 'fim'.")

    except Exception as erro:
        print(f"⚠️ Erro inesperado: {erro}")

    finally:
        tentativas += 1
        print("🔁 Verificação concluída nesta tentativa.\n")

# Cálculo da média (após o laço)
if notas:
    media = sum(notas) / len(notas)
    print(f"📊 Média da turma com {len(notas)} nota(s): {media:.2f}")
else:
    print("⚠️ Nenhuma nota válida foi registrada.")
