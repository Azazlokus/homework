from Graph import Graph


def reverse_graph(graph: Graph):
	r_graph = Graph()
	for vert in graph:
		for neighbor in vert.getConnections():
			r_graph.addEdge(neighbor.getId(), vert.getId())
	return r_graph


graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(2, 1)
graph.addEdge(1, 3)

print("Заданный граф")
for vert in graph:
	for neighbor in vert.getConnections():
		print("( %s, %s )" % (vert.getId(), neighbor.getId()))

r_graph = reverse_graph(graph)

print("Обращенный граф")
for vert in r_graph:
	for neighbor in vert.getConnections():
		print("( %s, %s )" % (vert.getId(), neighbor.getId()))

