# Pedindo ao usuário para que digite 3 números:

# Requerer ao usuário a entrada de 3 números quaisquer
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um outro número: "))
numero3 = float(input("Digite mais um número: "))

# Aplica-se a expressão matemárica para calcular a média entre os 3 números
media = (numero1 + numero2 + numero3) / 3

# Imprimindo na tela do usuário a frase relacionada ao resultado da média entre os três números digitados
print(f"A média entre {numero1}, {numero2} e {numero3} é {media}")