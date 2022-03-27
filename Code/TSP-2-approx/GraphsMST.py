# Traveling Sales Man (TSP) premise states:
# "Given a set of cities and distance between every pair of cities, the problem is to find the shortest possible 
#  route that visits every city exactly once and returns to the starting point."

# Two important things about the problem statement: 
# Visit every city exactly once
# Cover the shortest path

# The Algorithm :
# Let 0 be the starting and ending point for salesman.
# Construct Minimum Spanning Tree with 0 as root using Prim’s Algorithm.
# List vertices visited in preorder walk/Depth First Search of the constructed MST and add source node at the end.

# Triangle-Inequality: The least distant path to reach a vertex j from i is always to reach j directly from i, rather than through some
# other vertex k (or vertices), i.e., dis(i, j) is always less than or equal to dis(i, k) + dist(k, j).

# Graph is based on adjacency matrix.

import sys


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.vertices = [i for i in range(len(self.graph))]
        self.vertices_num = len(self.vertices)

    def add_vertex(self, v):
        """Adds a vertex to the graph."""
        if v in self.vertices:
            print("Vertex", v, "is already in the graph.")
            return
        else:
            self.vertices.append(v)
            self.vertices_num += 1
            if self.vertices_num > 1:
                for vertex in self.graph:
                    vertex.append(0)
            temp = []
            for i in range(self.vertices_num):
                temp.append(0)
            self.graph.append(temp)

    def add_edge(self, v1, v2, weight):
        """Sets a weighted edge between vertices v1 and v2."""
        if v1 not in self.vertices:
            print("Vertex", v1, "does not exist.")
            return
        elif v2 not in self.vertices:
            print("Vertex", v2, "does not exist.")
            return
        else:
            v1_index = self.vertices.index(v1)
            v2_index = self.vertices.index(v2)
            self.graph[v1_index][v2_index] = weight
            self.graph[v2_index][v1_index] = weight
            # Edge is set in both directions since our graph is a weighted non-directional one.

    def print_graph(self):
        """Prints the graph in a format that shows which vertex leds to the other ones."""
        for i in range(self.vertices_num):
            for j in range(self.vertices_num):
                if self.graph[i][j] != 0:
                    print(self.vertices[i], "->", self.vertices[j], "| edge weight:", self.graph[i][j])

    def print_matrix(self):
        """Prints the adjacency matrix of the graph."""
        print()
        for row in self.graph:
            print(row)
        print()

    def min_key(self, key, mst_set):
        """A utility function to find the vertex with minimum distance value, from the set of vertices."""
        minimum = sys.maxsize  # Initialize min value
        min_index = 0
        for vertex in range(self.vertices_num):
            if key[vertex] < minimum and mst_set[vertex] is False:
                minimum = key[vertex]
                min_index = vertex
        return min_index

    def prims_mst(self):
        """Function to construct and print MST for a graph represented using adjacency matrix representation."""
        key = [sys.maxsize] * self.vertices_num  # Key values used to pick minimum weight edge.
        parent = [None] * self.vertices_num  # Array to store constructed MST.
        key[0] = 0  # Make key 0 so that this vertex is picked as first vertex.
        mst_set = [False] * self.vertices_num
        parent[0] = -1  # First node is always the root of tree.
        for count in range(self.vertices_num):
            min_dst = self.min_key(key, mst_set)  # Pick the minimum distance vertex from the set of vertices
                                                  # not yet processed.
            mst_set[min_dst] = True  # Put minimum distance vertex in the shortest path tree.
            for vertex in range(self.vertices_num):
                if 0 < self.graph[min_dst][vertex] < key[vertex] and mst_set[vertex] is False:
                    key[vertex] = self.graph[min_dst][vertex]
                    parent[vertex] = min_dst
        self.print_mst(parent)
        return parent, key

    def print_mst(self, parent):
        """Prints what the Prim's algorithm MST looks like."""
        print("Edge \tWeight")
        for i in range(1, self.vertices_num):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
