from Graph import Graph
from Graph import Vertex

def dijkstra(graph: Graph, start_node: Vertex):
	unvisited_nodes = list(graph.getVertices())
	shortest_path = {}
	prev_nodes = {}
	infinity = float("inf")
	for node in unvisited_nodes:
		shortest_path[node] = infinity
	shortest_path[start_node.getId()] = 0
	
	while unvisited_nodes:
		current_min_node = None
		for node in unvisited_nodes:
			if current_min_node == None:
				current_min_node = node
			elif shortest_path[node] < shortest_path[current_min_node]:
				current_min_node = node
		
		neighbors = []
		for neighbor in graph.getVertex(current_min_node).getConnections():
			neighbors.append(neighbor.getId())
		for neighbor in neighbors:
			nbr = graph.getVertex(neighbor)

			tentative_value = shortest_path[current_min_node] + graph.getVertex(current_min_node).getWeight(nbr)
			if tentative_value < shortest_path[neighbor]:
				shortest_path[neighbor] = tentative_value
				prev_nodes[neighbor] = current_min_node
		unvisited_nodes.remove(current_min_node)
	return prev_nodes, shortest_path

def print_path(prev_nodes: dict, shortest_path: dict, start_node: str, end_node: str):
	path = []
	node = end_node
	while node != start_node:
		path.append(node)
		try:
			node = prev_nodes[node]
		except:
			print("Нет подходящего маршрута")
			return
		
	path.append(start_node)
	path.reverse()
	print("Лучший маршрут:", end=" ")
	print(" -> ".join(path))
	print("Расстояние:", shortest_path[end_node])

graph = Graph()
graph.addEdge("Мариинск", "Яя", 139)
graph.addEdge("Мариинск", "Юрга", 183)
graph.addEdge("Мариинск", "Яшкино", 240)
graph.addEdge("Яя", "Юрга", 109)
graph.addEdge("Яя", "Анжеро-Судженск", 27)
graph.addEdge("Яшкино", "Юрга", 43)
graph.addEdge("Юрга", "Анжеро-Судженск", 91)
graph.addEdge("Юрга", "Кемерово", 97)
graph.addEdge("Анжеро-Судженск", "Кемерово", 80)
graph.addEdge("Яшкино", "Томск", 239)
graph.addEdge("Юрга", "Томск", 106)
graph.addEdge("Томск", "Кемерово", 217)

startNode = graph.getVertex("Яя")
endNode = graph.getVertex("Яшкино")

prev_nodes, shortest_path = dijkstra(graph, startNode)
print_path(prev_nodes, shortest_path, startNode.getId(), endNode.getId())
