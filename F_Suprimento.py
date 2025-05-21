n = int(input())

eventos = [int(input()) for _ in range(n)]

saldo = 0
min_saldo = 0

for evento in eventos:
    saldo += evento
    if saldo < min_saldo:
        min_saldo = saldo

print(-min_saldo)
