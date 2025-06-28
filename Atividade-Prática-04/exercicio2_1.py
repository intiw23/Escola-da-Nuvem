"""
Atividade 2 – Registro de Notas da Turma

Aula 7 – 26/06/2025
C3 MAR - BRSAO 188 Noite – IA
Autor: Walter
Versão: 1.2

Enunciado:
Crie um programa que permita a um professor registrar as notas de uma turma.
O programa deve continuar solicitando notas até que o professor digite 'fim'.
Notas válidas são de 0 a 10. Notas inválidas devem ser ignoradas.
Ao final, deve ser exibida a média da turma.
"""

notas = []        # Lista de notas válidas
tentativas = 0    # Contador de tentativas com erro
indice_nota = 1   # Numeração das notas válidas

while True:
    try:
        entrada = input("-> Digite a nota da turma ou 'fim' para terminar: ").strip().lower()

        if entrada == "fim":
            print("-> Registro de notas encerrado.")
            break

        nota = float(entrada.replace(",", "."))  # Aceita ponto ou vírgula

        if 0 <= nota <= 10:
            print(f" Nota Válida {indice_nota}: {nota}")
            notas.append(nota)
            indice_nota += 1
        else:
            print(f"\n Tentativa {tentativas + 1}")
            print("-> Nota fora do intervalo permitido (0 a 10).")
            tentativas += 1

    except ValueError:
        print(f"\n Tentativa {tentativas + 1}")
        print("-> Erro: Entrada inválida. Digite um número entre 0 e 10 ou 'fim'.")
        tentativas += 1

    except Exception as erro:
        print(f"\n Tentativa {tentativas + 1}")
        print(f"-> Erro inesperado: {erro}")
        tentativas += 1

    finally:
        print(" Verificação concluída nesta tentativa.\n")

# Impressão final das notas e média
if notas:
    print("-> Notas válidas registradas:")
    for i, valor in enumerate(notas, start=1):
        print(f"   - Nota {i}: {valor:.2f}")

    media = sum(notas) / len(notas)
    print(f"\n -> Média da turma com {len(notas)} nota(s): {media:.2f}")
else:
    print(" Nenhuma nota válida foi registrada.")
