# Entrando com o valor de um número e encontrando o dobro dele:

# Solicita-se ao usuário um número real qualquer
numero = float(input("Digite um número: "))

# Aplica-se uma fórmula para calcular o dobro do número digitado pelo usuário:
dobro = numero * 2

# Imprimindo ao usuário o dobro do número utilizado como entrada
# Utiliza-se o f-strings para concatenar a expressão impressa
print(f"O dobro de {numero} é {dobro}")