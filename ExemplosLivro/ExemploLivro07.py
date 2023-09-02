numero = 1

#Estruturas de repetição - While
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")
