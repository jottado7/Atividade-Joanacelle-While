soma = 0
while True:
    numero = int(input("digite um numero inteiro:"))

    if numero < 0:
        break

    soma += numero
print(f"a soma dos numeros e: {soma}")