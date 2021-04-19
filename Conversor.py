print("Bem vindo. Este programa vai ajudar-te a converter km's em milhas.")

repeticao = True

while repeticao:
    valor = float(input("Por favor insere o número de km's que queres converter: "))
    print(str(valor) + " km's são " + str(valor*0.621371) + " milhas")

    avancar = input("Desejas fazer mais conversões? (S/N) ")
    avancar = avancar.lower()

    if avancar == "n":
        print("Espero ter sido util. Adeus")
        repeticao = False


