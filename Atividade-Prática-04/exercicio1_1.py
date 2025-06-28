"""
Exercício Prático 1 – Aula 7 (26/06/2025)
C3 MAR - BRSAO 188 Noite – IA
Autor: Walter
Versão: 1.0

Calculadora com tratamento de erros e controle

EXERCÍCIO PRÁTICO 1
Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração,
multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos
tipos de erros de entrada e operação. Siga as especificações abaixo:

1.A calculadora deve solicitar ao usuário que insira dois números e uma operação.
2.As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
3.0 programa deve continuar solicitando entradas até que uma operação válida seja concluída.
4. Trate os seguintes erros:
o Entrada inválida (não numérica) para os números
o Divisão por zero
· Operação inválida
5.Use try/except para capturar e tratar os erros apropriadamente.
6.Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
7.Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.

"""
tentativa = 0

while True: #for tentativa in range(100):  # Até 100 tentativas
    try:
        print(f"\n -> Tentativa {tentativa + 1}")

        # Entrada dos números
        num1 = float(input("Digite o primeiro número: ").replace(",", "."))
        num2 = float(input("Digite o segundo número: ").replace(",", "."))

        # Entrada da operação
        operacao = input("Escolha a operação (+, -, *, /): ").strip()

        # Verifica se a operação é válida
        if operacao not in ['+', '-', '*', '/']:
            print("❌ Operação inválida! Use apenas +, -, * ou /.")
            continue  # Volta para a próxima tentativa

        # Verifica divisão por zero antes de calcular
        if operacao == '/' and num2 == 0:
            raise ZeroDivisionError

        # Cálculo da operação
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2
        #else:
        #    raise ValueError("Operação inválida")

        # Exibe resultado e interrompe o laço
        print(f" Resultado: {num1} {operacao} {num2} = {resultado:.2f}")
        break  # Finaliza o for

    except ValueError:
        print(" Erro: Entrada inválida! Digite apenas números válidos.")

    except ZeroDivisionError:
        print(" Erro: Não é possível dividir por zero.")

    except Exception as erro:
        print(f" Erro inesperado: {erro}")

    finally:
        tentativa += 1  # Atualise se caiou em alguma exeption
        print(" Tentativa concluída.\n")  # Mostra mesmo com erro ou acerto
