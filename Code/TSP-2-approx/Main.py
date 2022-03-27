from GraphsMST import Graph
import CSVHandler

def main():
    adjacency_matrix = CSVHandler.read_csv_file("input/graph.csv")
    graph = Graph(adjacency_matrix)
    print()
    print("------------------------------------------------------------------------------")
    print("The graph built from reading graph.csv has " + str(graph.vertices_num) + " vertices.")
    print("The vertices are " + str(graph.vertices) + ", and they form the following adjacency matrix: ")
    graph.print_matrix()
    print("After applying Prim's algorithm to find an MST based on the graph, we get that the MST is: ")
    print()
    graph.prims_mst()
    print("------------------------------------------------------------------------------")
    print()

if __name__ == "__main__":
    main()
