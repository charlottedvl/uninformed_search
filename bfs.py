from success import success


def bfs_search(graph, starting_node, goal_node):
    # List of nodes to be explored (works in First In First Out = FIFO)
    fringe = []
    # List of explored nodes
    explored = set()

    # Initialize the fringe with the starting node
    fringe.append(starting_node)

    # List of parent for each node
    parents = {starting_node: None}

    print("Parsed nodes: ", end="")
    while fringe:
        # Get the current node from the first position of the nodes to be explored
        current_node = fringe[0]
        # Print each node that is explored
        print(current_node.name, end="")

        # If the current node is the goal node, reconstruct the path and return it with the success function
        if current_node == goal_node:
            return success(parents, current_node)

        print(" - ", end="")
        # Get all the successors of the current node
        successors = graph.find_successors(current_node)
        for successor in successors:
            # If the successor is already explored or is already in fringe, then pass to the next successor
            if successor in explored or successor in fringe:
                continue
            # Add the current node as the successor parent
            parents[successor] = current_node
            # Add the successor to the fringe list of node to be explored
            fringe.append(successor)
        # Add the current node to the explored nodes
        explored.add(current_node)
        # Remove the current node from the fringe list
        fringe.remove(current_node)
    # If we reach this point, there is no solution to go from the starting node to goal node
    return None
