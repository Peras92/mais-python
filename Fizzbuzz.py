validacao = True

while validacao:
    intervalo = int(input("Escolhe um número de 1 a 100: "))

    if intervalo <=0 or intervalo > 100:
        print("Escolheste um número fora do intervalo. Por favor volta a escolher")

    else:
        validacao = False

for numero in range(intervalo):
    div3 = ((numero+1) % 3) #diz se é divisivel por 3
    div5 = ((numero+1) % 5) #diz se é divisivel por 5

    if div3 == 0 and div5 == 0:
        print("fizzbuzz")

    elif div3 == 0:
        print("fizz")

    elif div5 == 0:
        print("buzz")

    else:
        print(numero+1)
