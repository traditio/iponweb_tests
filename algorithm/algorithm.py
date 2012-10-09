from heapq import heappop, heappush, heapify


class Infinity(object):
    pass


def _change_priority(priority_queue, new_priority, item):
    assert isinstance(priority_queue, list)
    changed = False
    for entry in priority_queue:
        if entry[-1] == item:
            entry[0] = new_priority
            changed = True
            break
    if not changed:
        priority_queue.append([new_priority, item])
    heapify(priority_queue)


def _priority(priority_queue, item):
    assert isinstance(priority_queue, list)
    for p, i in priority_queue:
        if i == item:
            return p


def _traverse_path(graph, path, current_node, path_weight=0, path_str=''):
    assert isinstance(graph, dict)
    assert isinstance(path, dict)
    if path[current_node] != current_node:
        edge_weight = graph[current_node][path[current_node]]
        return _traverse_path(
            graph,
            path,
            path[current_node],
            path_weight + edge_weight,
            ' '.join((path_str, current_node, '->')))
    else:
        return ' '.join((path_str, path[current_node], '=', str(path_weight)))[1:] #cut first space


def shortest_path(graph, start_node, end_node):
    """searching shortest path length in weighted graph (aka Dijkstra) in nlog(n) time."""
    path = dict()
    path[start_node] = start_node
    priority_queue = []
    for v in graph.iterkeys():
        if v != start_node:
            heappush(priority_queue, [Infinity, v])
    heappush(priority_queue, [0, start_node])
    marks = set()
    while len(marks) < len(graph):
        priority, u = heappop(priority_queue)
        marks.add(u)
        for v in graph[u].iterkeys():
            if v not in marks and _priority(priority_queue, v) > priority + graph[u][v]:
                _change_priority(priority_queue, priority + graph[u][v], v)
                path[v] = u
    return _traverse_path(graph, path, end_node)


if __name__ == '__main__':
    Graph = {}
    with open('path_data.csv') as f:
        for edge in f.readlines():
            if len(edge) <= 1 or edge.find('#') == 0:
                continue
            (node_start, node_end, weight) = edge.strip().split(',')
            if node_start not in Graph:
                Graph[node_start] = {}
            Graph[node_start][node_end] = int(weight)
            if node_end not in Graph:
                Graph[node_end] = {}
            Graph[node_end][node_start] = int(weight)
    print shortest_path(Graph, '1', '7')