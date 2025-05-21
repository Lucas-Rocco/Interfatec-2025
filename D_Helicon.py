n = int(input())
vetorElementos = input().split()
 
soma = 0
maior = 0
kc = 0
for k in range(1, int(n/2)):
    for i in vetorElementos:
        if kc == k:
            soma += int(i)
            kc = 0
        kc += 1    

    if maior < soma:
        maior = soma
    else:
        maior = soma
# soma = negativos + positivos
print(maior)

# for i in vetorElementos:
#     if int(i) < 0: 
#         negativos = int(i)
#     else:
#         positivos = int(i)
