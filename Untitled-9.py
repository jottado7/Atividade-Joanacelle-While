soma = 0
contador = 0

nota= float(input("Digite uma nota (-1 para sair):"))

while nota != -1:
    if 0 <=nota <= 10:
        soma += nota
        contador += 1
    else:
        print("Valor invalido")
    nota = float(input("Digite uma nota (-1 para sair):"))

if contador > 0:
    media = soma / contador
    print("A media das notas é:", media)
else:
    print("Nenhuma nota valida")