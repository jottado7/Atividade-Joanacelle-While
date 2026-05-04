senha = (input("Digite a senha:"))

senhafixa = str(1234)
while True:
    if senha == senhafixa:
        print("Acesso permitido")
        break
    else:
        print("Senha incorreta, tente novamente")
        senha = (input("Digite a senha"))