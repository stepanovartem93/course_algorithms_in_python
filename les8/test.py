n = int(input("Введите размер графа: "))

graph = [[0] * n for el in range(n)]

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if i != j:
            graph[i][j] = 1

print(*graph, sep="\n")

count = 0

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            count += 1
print(f'Количество рукопожатий равно: {int(count/2)}')