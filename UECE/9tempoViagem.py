# Calculando o tempo de viagem a partir da distância a ser percorrida e da velocidade média:

# Solicita-se a distância entre a sua casa e o destino
distancia = float(input("Digite a distância da viagem em km: "))

# Depois pergunta-se qual é a velocidade média
velocidadeMedia = float(input("Informe a velocidade média esperada: "))

# Escrevendo a fórmula para calcular o tempo a partir da distância e da velocidade média
tempoViagem = distancia / velocidadeMedia 

# Imprimindo na tela do usuário o tempo de viagem sem paradas
print(f"Na sua trajetória de {distancia}km a uma velocidade de {velocidadeMedia} km/h, o tempo estimado da viagem seria {tempoViagem}h caso não haja paradas")