# 1. Entrada de dados
num1 = float(input())
num2 = float(input())
operador = input()

# 2. Tomada de decisão e exibição do resultado
if operador == "+":
    print(num1 + num2)

elif operador == "-":
    print(num1 - num2)

elif operador == "*":
    print(num1 * num2)

elif operador == "/":
    if num2 == 0:
        print("Não é possível dividir por zero")
    else:
        print(num1 / num2)

else:
    print("Operador inválido")