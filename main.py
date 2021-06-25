import sys


def adicao(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def multiplicacao(num1, num2):
    return num1 * num2


def divisao(num1, num2):
    return num1 / num2


def modulo(num1, num2):
    return num1 % num2


def pergunta_num(text):
    numero = input(text)
    if numero.lower() == "sair":
        sys.exit(" ")

    return int(numero)


def pergunta_operador(text):
    operador = input(text)

    while operador.lower() not in ["+", "-", "*", "/", "%", "sair"]:
        print("SELECIONE A OPERAÇÃO NOVAMENTE")
        operador = input(text)

    if operador.lower() == "sair":
        sys.exit(" ")

    return operador


flag_primeira_vez = True

print("digite 'sair' a qualquer momento para desligar a calculadora.")

numero1 = pergunta_num("Escolha o primeiro numero: ")

while True:
    if not flag_primeira_vez:
        print()
        print(f"Memoria 1: {numero1}")
        pergunta = input("Pressione \"S\" para nova operaçao, caso queira manter a memoria presione \"M\": ")

        if pergunta == "sair":
            break

        if pergunta.lower() == "s":
            numero1 = pergunta_num("Escolha o primeiro numero: ")

    operador = pergunta_operador("Escolha a operacao (+ = adição)(- = subtração)(* = multiplicação)(/ = divisão)(% = "
                                 "resto): ")

    numero2 = pergunta_num("Escolha o segundo numero: ")

    if operador == "+":
        resultado = adicao(numero1, numero2)

    elif operador == "-":
        resultado = subtracao(numero1, numero2)

    elif operador == "*":
        resultado = multiplicacao(numero1, numero2)

    elif operador == "/":
        resultado = divisao(numero1, numero2)

    elif operador == "%":
        resultado = modulo(numero1, numero2)

    print(f"O Resultado é: {resultado}")
    numero1 = resultado
    print()
    print("==-==-==-==-==-==-==-==-==-==-==-==")
    flag_primeira_vez = False
