status = True

while status == True :
    entrada = input()
    possition = 0
    soma = 0
    resutado = 0

    for i in entrada:
        if i == " ":
            possition += 1

    if possition == 0:
        for i in entrada:
            if i == "*":
                soma += 0
                status = False
            if i == ".":
                soma += 1
            if i == "-":
                soma +=5
        resutado = resutado + (soma * (20**possition))
    else:
        for i in entrada:
            if i == " ":
                resutado = resutado + (soma * (20**possition))
                soma = 0
                possition = possition - 1
            if i == "*":
                soma += 0
            if i == ".":
                soma += 1
            if i == "-":
                soma += 5
        resutado = resutado + (soma * (20**possition))

    print(resutado)