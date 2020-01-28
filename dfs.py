def dfs_recursive(graph, visited_nodes, current_node, route, end_node):
    if end_node in route: return # for traversal until end node found
    visited_nodes[current_node] = True
    route.append(current_node)
    for node in graph[current_node]:
        if visited_nodes[node] == False:
            dfs_recursive(graph, visited_nodes, node, route, end_node)

def dfs(graph, start_node, end_node):
    visited_nodes = [False] * len(graph)
    route = []
    dfs_recursive(graph, visited_nodes, start_node, route, end_node)
    return route

print(dfs(
    {
        0: [1, 2],
        1: [2, 4],
        2: [0, 3],
        3: [3],
        4: [0]
    },
    2,
    3
))