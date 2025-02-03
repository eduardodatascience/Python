# Programa para transformar a temperatura de Celsius para Fahrenheit:

# Requerendo ao usuário a temperatura em Celsius
temperaturaCelsius = float(input("Digite a temperatura em Celsius: "))

# Fazendo a conversão de Celsius para Fehrenheit por meio da fórmula
temperaturaFahrenheit = (temperaturaCelsius * (9 / 5) + 32)

# Mostrando ao usuário qual a temperatura em Fahrenheit que corresponde à temperatura em Celsius
# Utiliza-se o f-strings para formatar a expressão impressa
print(f"{temperaturaCelsius}°C em Fahrenheit é {temperaturaFahrenheit} °F")