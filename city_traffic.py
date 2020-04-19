
def bfs(graph, node, e):
    visited = []
    queue = []

    visited.append(e)
    visited.append(node)
    queue.append(node)

    total = node
    while queue:
        s = queue.pop(0)

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
                total = total + n
    return total


def get_traffic(traffic):
    result = {}

    for city in traffic.keys():
        h = 0
        for n in traffic[city]:
            total_traffic = bfs(traffic, n, city)
            if h < total_traffic:
                h = total_traffic

        result[city] = h

    return result


traffic = {1: [5], 4: [5], 3: [5], 5: [1, 4, 3, 2], 2: [5, 15, 7], 7: [2, 8], 8: [7, 38], 15: [2], 38: [8]}

print(get_traffic(traffic))
