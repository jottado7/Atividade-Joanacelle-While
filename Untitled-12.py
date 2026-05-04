numerosecreto = 19

palpite = int(input("Digite um numero:"))

while palpite != numerosecreto:
    if palpite < numerosecreto:
        print("O numero secreto é maior")
    else:
        print("O numero secreto é menor")

    palpite = int(input(" Tente novamente:"))

print("Voce acertou")