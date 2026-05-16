class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        # this is for connecting dest->src
        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

        # this is for connecting src-> dest
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n ")


if __name__ == "__main__":
    _Vertex = 5
    graph = Graph(_Vertex)
    # graph is allocated for 5 vertices
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
