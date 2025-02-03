# Solicitando ao usuário dois números para calcular a soma, diferença, produto e quociete entre eles:

# Pedindo ao usuário para que digite dois números
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite mais um número: "))

# Soma de dois números
soma = numero1 + numero2

# Subtração entre os dois números
subtracao = numero1 - numero2

# Produto entre os dois números
multiplicacao = numero1 * numero2

# Quociente entre os dois números
divisao = numero1 / numero2

# Imprimindo na tela do usuário o resultado das operações supracitadas
print(f"A soma entre {numero1} e {numero2} é {soma}")
print(f"A subtração entre {numero1} e {numero2} é {subtracao}")
print(f"O produto entre {numero1} e {numero2} é {multiplicacao}")
print(f"O quociente entre {numero1} e {numero2} é {divisao: .2f}")
