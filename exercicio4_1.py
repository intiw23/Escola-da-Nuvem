"""
Atividade 4 – Analisador de Números Inteiros

Aula 7 – 26/06/2025
C3 MAR - BRSAO 188 Noite – IA
Autor: Walter
Versão: 1.0

Enunciado:
Crie um programa que solicite ao usuário que insira números inteiros.
O programa deve continuar solicitando números até que o usuário digite 'fim'.
Para cada número inserido, o programa deve informar se é par ou ímpar.
Se o usuário inserir algo inválido, deve informar o erro e continuar.
Ao final, exiba a quantidade de números pares e ímpares válidos.
"""

def analisador_numeros():
    pares = 0
    impares = 0
    tentativas = 0   # Tentativas inválidas
    indice_valido = 1  # Contador de números válidos

    while True:
        try:
            entrada = input("\n -> Digite um número inteiro (ou 'fim' para encerrar): ").strip().lower()

            if entrada == 'fim':
                print(" Entrada final recebida. Encerrando análise...")
                break

            numero = int(entrada)

            if numero % 2 == 0:
                print(f" Número {indice_valido}: {numero} é **par**.")
                pares += 1
            else:
                print(f" Número {indice_valido}: {numero} é **ímpar**.")
                impares += 1

            indice_valido += 1

        except ValueError:
            print(f"\n Tentativa inválida {tentativas + 1}")
            print(" Erro: Digite apenas números inteiros válidos.")
            tentativas += 1

        except Exception as erro:
            print(f"\n Tentativa inválida {tentativas + 1}")
            print(f" Erro inesperado: {erro}")
            tentativas += 1

        # finally:
        #     print(" Verificação concluída nesta tentativa.\n")

    # Resultado final
    print("\n ---- Resultado final da análise ----")
    print(f"✔️ Quantidade de números **pares**: {pares}")
    print(f"✔️ Quantidade de números **ímpares**: {impares}")
    print(f"❌ Tentativas inválidas: {tentativas}")

# Executa a função
analisador_numeros()
