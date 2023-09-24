import sys
'''
Implementation of the Djxtra algorithm based on the adjacent lists (key-value pairs)
'''
class Node:
    childs = None
    def __init__(self, val, childs):
        self.val = val
        if childs is None:
            self.childs = {}
        else:
            self.childs = childs

    def has_childs(self):
        if len(self.childs) == 0:
            return False
        return True

    def num_of_childs(self):
        return len(self.childs)

    def get_childs(self):
        return self.childs

    def add_child(self, child):
        return self.childs.append(child)

class Graph:
    # class creation
    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []

    # add node to graph
    def add_node(self, value, childs):
        nod = Node(value, childs)

        if nod.val in self.nodes:
            return
        self.nodes.append(nod)

    def find_node(self, value):
        for n in self.nodes:
            if n.val == value:
                return n
        return None

    def num_of_nodes(self):
        return f"Graph has {len(self.nodes)} nodes"

    def are_connected(self, node1, node2):
        node1 = self.find_node(node1)
        node2 = self.find_node(node2)

        for n in node1.childs:
            if n == node2.val:
                return True
        return False

    def get_neibhour_nodes(self, n):
        return n.childs

    def shortest_search(self, start, end):

        distances = {} # distances (list of connetions with weights - as hash table)
        for node1 in self.nodes:
            distances[node1.val] = node1.childs
        # fill out with all node vals and max value for neighbours like {NODE : sys.maxsize ... }
        unvisited = {n: sys.maxsize for n in [val.val for val in self.nodes]}
        unvisited[start] = 0
        visited = {} # save all visited nodes
        vertexes = [] # save all vertexes to get path

        while unvisited:
            min_vertex = None
            for n in unvisited:
                if min_vertex == None:
                    min_vertex = n
                elif unvisited[n] < unvisited[min_vertex]:
                    min_vertex = n
            for neighbour in distances[min_vertex].keys():
                if neighbour in visited:
                    continue
                temp_value = unvisited[min_vertex] + distances[min_vertex].get(neighbour)
                if temp_value < unvisited[neighbour]:
                    unvisited[neighbour] = temp_value
            visited[min_vertex] = unvisited[min_vertex]
            unvisited.pop(min_vertex)
            vertexes.append(min_vertex)
            if min_vertex == end:
                break
        return visited, vertexes

    def print_graph(self):

        for n in self.nodes:
            if n.has_childs():
                    print(n.val, '->', n.get_childs())
            else:
                print(n.val, '-> None')


if __name__ == '__main__':

    graph = Graph()
    graph.add_node('A', {'B' : 2, 'C' : 3})
    graph.add_node('B', {'A' : 2, 'E' : 5, 'D' : 3})
    graph.add_node('C', {'A' : 3, 'E' : 5, 'D' : 6})
    graph.add_node('D', {'B' : 3, 'E' : 3, 'F' : 4})
    graph.add_node('E', {'B' : 5, 'D' : 3, 'F' : 4})
    graph.add_node('F', {'E' : 4, 'D' : 4})

    print(graph.num_of_nodes())
    print(graph.are_connected('B', 'E'))

    if graph.find_node('G'):
        print("Node exists!")
    else:
        print("Node does not exist!")

    start = 'B'
    end = 'C'
    vis, vrtxs = graph.shortest_search(start, end)
    print("Shortest distance from %s to %s is: %.2f" % (start, end, vis[end]))
    res = ''
    for v in vrtxs:
        res += v+'->'
    print("The path made by the algorithm: ", res[:-2])

    print("\nDone!")
