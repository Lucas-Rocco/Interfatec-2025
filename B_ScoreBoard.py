def format_time_output(team):           #codigo nao funcionando, gerado pelo gpt
    return f"{team['name']} - {team['fatec']} ({team['solved']},{team['time']})"

def main():
    sede = input().strip()
    V, Ve = map(int, input().split())
    NT = int(input())

    times = []
    for _ in range(NT):
        parts = input().split('|')
        name, fatec, solved, time = parts[0].strip(), parts[1].strip(), int(parts[2]), int(parts[3])
        times.append({'name': name, 'fatec': fatec, 'solved': solved, 'time': time})

    desclassificados = [t for t in times if t['solved'] == 0]
    classificados = []
    resto = []

    # Classificado da sede
    sede_times = [t for t in times if t['fatec'] == sede and t['solved'] > 0]
    if sede_times:
        sede_class = sorted(sede_times, key=lambda x: (-x['solved'], x['time']))[0]
        classificados.append(sede_class)

    # Melhor de cada Fatec
    fatecs = {}
    for t in times:
        if t['solved'] == 0 or t['fatec'] == sede:
            continue
        if t['fatec'] not in fatecs or (t['solved'], -t['time']) > (fatecs[t['fatec']]['solved'], -fatecs[t['fatec']]['time']):
            fatecs[t['fatec']] = t

    classificados.extend(fatecs.values())

    # Ordenar por pontuação para preencher vagas restantes
    usados = set(id(t) for t in classificados)
    restantes = [t for t in times if t['solved'] > 0 and id(t) not in usados]
    restantes = sorted(restantes, key=lambda x: (-x['solved'], x['time']))

    while len(classificados) < V + Ve and restantes:
        classificados.append(restantes.pop(0))

    # Lista de espera: restantes com pontuação
    lista_espera = sorted(restantes, key=lambda x: (-x['solved'], x['time']))

    # Ordenar classificados
    classificados = sorted(classificados, key=lambda x: x['name'])
    print("Classificados para a Final")
    for t in classificados:
        print(format_time_output(t))

    print()
    print("Lista de Espera")
    for t in lista_espera:
        print(format_time_output(t))

    print()
    print("Desclassificados")
    for t in sorted(desclassificados, key=lambda x: x['name']):
        print(format_time_output(t))

    print()
    print("Apuracao concluida!")

if __name__ == "__main__":
    main()
