from sympy import symbols, integrate, sympify

# Solicita a expressão e a variável
expressao_str = input ("Digite a função que deseja integrar (ex: x**2 + 3*x): ")
variavel_str = input ("Digite a variável de integração (ex: x): ")

variavel = symbols (variavel_str)
expressao = sympify (expressao_str)

# Pergunta se será definida ou indefinida
tipo = input ("Deseja uma integral definida? (s/n): ")

if (tipo.lower () == 's'):
    limite_inferior = float (input ("Digite o limite inferior: "))
    limite_superior = float (input ("Digite o limite superior: "))
    resultado = integrate (expressao, (variavel, limite_inferior, limite_superior))
else:
    resultado = integrate (expressao, variavel)

print ("Resultado da integral:", resultado)
