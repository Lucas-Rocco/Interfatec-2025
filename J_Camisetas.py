import math
t = int(input())

lines = 0
maximo = 0

while lines < 3:
    
    q, l = map(int, input().split())
    soma = math.floor(t / q) * l

    if soma > maximo:
        maximo = soma
    lines += 1

print(int(maximo))