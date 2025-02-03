# Solicitando os valores correspondentes à largura e à altura de um retângulo:
largura_retangulo = float(input("Digite o valor que corresponde à largura do retângulo: "))
altura_retangulo = float(input("Digite o valor que corresponde à altura do retângulo: "))

# Implementando a fórmula da ára de um retângulo:
area_retangulo = largura_retangulo * altura_retangulo

# Imprimindo para o usuário qual é a área total do retângulo:
# Utilizei o .2f para que a área seja exibida com apenas 2 casas decimais
# A expressão impressa na tela é formatada com o f-strings
print(f"A área do retângulo é {area_retangulo: .2f}")