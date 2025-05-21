from collections import defaultdict, deque #codigo errado, gerado pelo gpt
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    # Parte 1: Construção do grafo
    n = int(data[0])  # Número de conexões
    grafo = defaultdict(list)

    i = 1
    while data[i] != "-":
        a, b = data[i].split()
        grafo[a].append(b)
        grafo[b].append(a)
        i += 1

    # Parte 2: Consultas
    i += 1
    while data[i] != "* *":
        nome1, nome2 = data[i].split()
        resultado = bfs_distancia(grafo, nome1, nome2)
        if resultado == -1:
            print(f"{nome1}-{nome2} = sem conexao")
        else:
            print(f"{nome1}-{nome2} = {resultado}")
        i += 1

def bfs_distancia(grafo, inicio, destino):
    if inicio == destino:
        return 0

    visitados = set()
    fila = deque([(inicio, 0)])

    while fila:
        atual, dist = fila.popleft()
        if atual == destino:
            return dist
        if atual in visitados:
            continue
        visitados.add(atual)
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                fila.append((vizinho, dist + 1))
    return -1  # sem conexão

if __name__ == "__main__":
    main()
