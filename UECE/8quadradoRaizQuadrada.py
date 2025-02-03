# Calculando o quadrado e a raiz quadrada de um número digitado pelo usuário
numero = float(input("Digite um número: "))

# O quadrado de um número é expresso pelo seu valor elevado a 2
quadrado = numero ** 2

# A raiz quadrada é o inverso da exponenciação. Portanto, se o quadrado do número é ele elevado a 2, então a sua raiz quadrada é esse número elevado a 1/2
raizQuadrada = numero ** (1/2) 

# Informando ao usuário o quadrado do número digitado
print(f"O quadrado de {numero} é {quadrado}")

# Informando ao usuário a raiz quadrada do mesmo número
print(f"Já a sua raiz quadrada é {raizQuadrada}")