
_cache = {}


def sort_traffic_report(traffic, reverse=True):
    traffic_sorted = {k: v for k, v in sorted(traffic.items(), key=lambda x: x[1], reverse=reverse)}
    return traffic_sorted


def _get_bfs_traffic_sum(graph, root, neighbour_root):
    visited = [neighbour_root, root]
    queue = [neighbour_root]
    traffic_sum = neighbour_root

    while queue:
        node = queue.pop(0)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                cached_traffic_sum = _cache.get('{}:{}'.format(node, neighbour))
                if cached_traffic_sum:
                    traffic_sum = traffic_sum + cached_traffic_sum
                    continue
                queue.append(neighbour)
                traffic_sum = traffic_sum + neighbour
    return traffic_sum


def get_traffic_report(traffic):
    traffic_result = {}

    for city in traffic.keys():
        max_traffic = 0
        for neighbour_city in traffic[city]:
            traffic_sum = _get_bfs_traffic_sum(traffic, city, neighbour_city)
            _cache['{}:{}'.format(city, neighbour_city)] = traffic_sum
            if max_traffic < traffic_sum:
                max_traffic = traffic_sum

        traffic_result[city] = max_traffic

    return traffic_result


traffic_graph = {1: [5], 3: [5], 4: [5], 5: [1, 2, 3, 4], 2: [5, 7, 15], 7: [2, 8], 8: [7, 38], 15: [2], 38: [8]}

traffic_report = get_traffic_report(traffic_graph)
traffic_report_sorted = sort_traffic_report(traffic_report, reverse=True)

print(traffic_report_sorted)
