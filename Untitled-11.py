positivos = 0
negativos = 0

numero = float(input("Digite um numero (ou 0 para sair):"))

while numero != 0:
    if numero > 0:
        positivos += 1
    else:
        negativos += 1

    numero = float(input("Digite um numero ( ou 0 para sair):"))

print("Quantidade de numeros positivos:", positivos)

print("Quantidade de numeros negativos:", negativos)