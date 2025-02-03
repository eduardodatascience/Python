distancia = float(input("Digite a distância da viagem em km: "))
velocidadeMedia = float(input("Informe a velocidade média esperada: "))

tempoViagem = distancia / velocidadeMedia 

print(f"Na sua trajetória de {distancia}km a uma velocidade de {velocidadeMedia} km/h, o tempo estimado da viagem seria {tempoViagem}h caso não haja paradas")