from collections import deque
from Graph import Graph


def person_is_seller(name):
    return name.getId()[0] == 'a'


graph = Graph()
graph.addEdge("you", "alice")
graph.addEdge("you", "bob")
graph.addEdge("you", "claire")
graph.addEdge("bob", "anuj")
graph.addEdge("bob", "peggy")
graph.addEdge("claire", "thom")
graph.addEdge("claire", "jonny")


def search(name):
    search_queue = deque()
    search_queue += graph.getVertex(name).getConnections()
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person.getId() + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False


search("you")
