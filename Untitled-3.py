nota = float(input("Digite uma nota entre 0 e 10"))

while nota < 0 or nota > 10:
    print ("valor invalido A nota deve estar 0 e 10")
    nota = float (input("Digite novamente"))

print (f"Nota valida informada : (nota)")