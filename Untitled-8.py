maior = 0
contador = 0
while True:
    numero = int(input("Digite um numero inteiro:"))
    if numero == 0:
        break
    
    contador += 1
    if contador == 1:
        maior = numero
    else:
        if numero > maior:
            maior = numero 
print(f"o maior numero digitado foi {maior}")