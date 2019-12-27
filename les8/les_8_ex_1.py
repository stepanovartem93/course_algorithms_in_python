'''На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?'''
'''
Задача решена 2 способами. Первый строит таблицу смежности графа. Вторая строит сам граф.
'''
# def build_graph(n):
#     graph = [[0] * n for el in range(n)]
#     for i in range(len(graph)):
#         for j in range(len(graph[i])):
#             if i != j:
#                 graph[i][j] = 1
#     return graph


# def count_handsakes(graph):
#     count = 0
#     for i in range(len(graph)):
#         for j in range(len(graph[i])):
#             if graph[i][j] == 1:
#                 count += 1
#     return count

# n = int(input("Введите количество друзей : "))
# print("Рукопожатия в виде графа: ")
# print(*build_graph(n), sep="\n")
# print(f'Количество рукопожатий: {int(count_handsakes(build_graph(n))/2)}.')

def friend(num):
    if num < 2:
        return "Слишком мало друзей"

    graph = []

    for i in range(num):
        for j in range(num):
            if i != j:
                graph.append((i, j))

    print(graph)

    return len(graph) // 2

print(friend(int(input(('Сколько друзей встретилось: ')))))