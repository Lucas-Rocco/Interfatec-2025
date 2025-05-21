def calcular_tempo_total(T, V, C, M):
    
    tempo_vale = 0 * V + 2 * T * C + 4 * T * M
    tempo_colina = 2 * T * V + 0 * C + 2 * T * M
    tempo_montanha = 4 * T * V + 2 * T * C + 0 * M

    return min(tempo_vale, tempo_colina, tempo_montanha)

T = int(input())
V = int(input())
C = int(input())
M = int(input())


print(calcular_tempo_total(T, V, C, M))