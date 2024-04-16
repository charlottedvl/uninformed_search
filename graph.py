class Graph:
    # Definition of a graph
    def __init__(self, successors):
        self.successors_list = successors

    # Find all successors for a given node
    def find_successors(self, node):
        return self.successors_list[node]
