def dijkstra(graph, start):
    not_visited_yet = graph
    shortest_dist = {}
    
    for node in not_visited_yet:
        shortest_dist[node] = float('inf')
    shortest_dist[start] = 0
    
    while not_visited_yet:
        min_node = None
        for node in not_visited_yet:
            if min_node == None or shortest_dist[node] < shortest_dist[min_node]:
                min_node = node
                
        for child, weight in not_visited_yet[min_node].items():
            if shortest_dist[min_node] + weight < shortest_dist[child]:
                shortest_dist[child] = shortest_dist[min_node] + weight
                
        not_visited_yet.pop(min_node)
        
    return shortest_dist

graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}
print(dijkstra(graph, 'a'))
                
        