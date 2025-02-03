valorCompra = float(input("Digite o valor da compra: "))
valorPago = float(input("Digite o valor pago: "))

troco = valorPago - valorCompra

print(f"O troco a ser recebido é {troco: .2f}")