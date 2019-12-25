'''На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?'''

def build_grapf(n):
    graph = [[0] * n for element in range(n)]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if i != j:
                graph[i][j] = 1
    return graph

n = int(input("Введите количество друзей : "))
print("Рукопожатия в виде графа :")
print(*build_grapf(n), sep="\n")
print(f"Количество рукопожатий равно n(n-1)/2 = {int(n * (n - 1)/2)}")