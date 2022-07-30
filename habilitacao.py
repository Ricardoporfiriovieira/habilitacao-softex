def habilitacao(rod, peso, pessoa):
    if(rod < 4):
        return "A"
    elif(rod == 4 and pessoa <= 8 and peso <= 3500):
        return "B"
    else:
            if(peso >= 3500 and peso <= 6000 and pessoas <= 8):
                return "C"
            elif(pessoa > 8 and peso >= 3500 and peso <= 6000):
                return "D"
            else:
                return "E"

rodas = int(input("Digite a quantidade de rodas do veiculo: "))
pesoBruto = float(input("Digite o peso bruto em quilogramas: "))
pessoas = int(input("Digite a quantidade de pessoas no veículo: "))

print(f"a melhor categoria para o veículo informado é: {habilitacao(rodas, pesoBruto, pessoas)}")


