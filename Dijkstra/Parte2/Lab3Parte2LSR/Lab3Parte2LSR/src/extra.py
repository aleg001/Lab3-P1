import sys

def dijkstra(graph, start):
    num_nodes = len(graph)
    distances = [sys.maxsize] * num_nodes
    distances[start] = 0
    visited = [False] * num_nodes
    path = [[] for _ in range(num_nodes)]
    path[start].append(start)

    for _ in range(num_nodes):
        min_distance = sys.maxsize
        min_index = -1

        for i in range(num_nodes):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                min_index = i

        visited[min_index] = True

        for i in range(num_nodes):
            if not visited[i] and graph[min_index][i] > 0:
                if distances[min_index] + graph[min_index][i] < distances[i]:
                    distances[i] = distances[min_index] + graph[min_index][i]
                    path[i] = path[min_index] + [i]

    return distances, path

# Ejemplo de uso:
graph = [[0, 1, 9999, 9999, 1, 1, 1, 9999, 9999], [1, 0, 1, 9999, 9999, 1, 9999, 1, 9999], [9999, 1, 0, 9999, 9999, 9999, 9999, 9999, 9999], [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999], [9999, 9999, 9999, 9999, 9999,
9999, 9999, 9999, 9999], [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999], [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999], [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999], [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999]]

start_node = 0
distances, paths = dijkstra(graph, start_node)

for i in range(len(distances)):
    if i != start_node:
        print(f'Distancia desde el nodo {start_node} al nodo {i}: {distances[i]}')
        print(f'Camino desde el nodo {start_node} al nodo {i}: {paths[i]}')
