# Calculando o troco que um cliente receberá a partir do valor de compra e do valor pago

# Solicitando ao usuário qual é o valor de compra e o valor pago
valorCompra = float(input("Digite o valor da compra: "))
valorPago = float(input("Digite o valor pago: "))

# Implementando o cálculo do troco
troco = valorPago - valorCompra

# Imprimindo na tela do usuário qual é o valor do troco
# Utiliza-se o f-strings para formatar a expressão
# O .2f indica que o número correspondente ao troco terá de ser impressa com 2 casas decimais
print(f"O troco a ser recebido é {troco: .2f}")