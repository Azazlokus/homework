from Graph import Graph


graph = Graph()
graph.addEdge("3/4 cup milk", "1 cup mix")
graph.addEdge("1 egg", "1 cup mix")
graph.addEdge("1 oil", "1 cup mix")
graph.addEdge("1 cup mix", "pour 1/4 cup")
graph.addEdge("1 cup mix", "heat syrup")
graph.addEdge("heat griddle", "pour 1/4 cup")
graph.addEdge("pour 1/4 cup", "turn when bubbly")
graph.addEdge("turn when bubbly", "eat")
graph.addEdge("heat syrup", "eat")


def dfs(graph: Graph):
    visited = {}
    unvisited_nodes = list(graph.getVertices())
    for node in unvisited_nodes:
        visited[node] = False
    stack = []

    for node in unvisited_nodes:
        if visited[node] == False:
            dfsUtil(node, visited, stack)
    print(stack)


def dfsUtil(node, visited, stack):
    visited[node] = True

    neighbors = []
    for neighbor in graph.getVertex(node).getConnections():
        neighbors.append(neighbor.getId())

    for neighbor in neighbors:
        if visited[neighbor] == False:
            dfsUtil(neighbor, visited, stack)
    stack.insert(0, node)


dfs(graph)
