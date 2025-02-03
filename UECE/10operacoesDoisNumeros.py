numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite mais um número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(f"A soma entre {numero1} e {numero2} é {soma}")
print(f"A subtração entre {numero1} e {numero2} é {subtracao}")
print(f"O produto entre {numero1} e {numero2} é {multiplicacao}")
print(f"O quociente entre {numero1} e {numero2} é {divisao: .2f}")
