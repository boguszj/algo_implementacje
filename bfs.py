def bfs(graph, start_node, end_node):
    queue = []
    route = []
    visited = [False] * len(graph)
    queue.append(start_node)
    visited[start_node] = True
    while queue:
        start_node = queue.pop(0)
        route.append(start_node)
        if end_node in route: return route # for traversal until end node found
        for node in graph[start_node]:
            if visited[node] == False:
                queue.append(node)
                visited[node] = True
    # return route # for full traversal

print(bfs(
    {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]   
    },
    2,
    1
))
    