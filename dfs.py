from queue import LifoQueue
from success import success


def dfs_search(graph, starting_node, goal_node):
    # List of nodes to be explored (works in Last In First Out = LIFO)
    fringe = LifoQueue()
    # List of nodes explored
    explored = set()

    # Insert the starting_node into the fringe
    fringe.put(starting_node)

    # List of parents for each node
    parents = {starting_node: None}

    print("Parsed nodes: ", end="")

    while fringe:
        # Get the current node from last instance in the Queue list
        current_node = fringe.get()
        # Print each explored node
        print(current_node.name, end="")

        # If the node is already explored, don't explore it again
        if current_node in explored:
            continue

        # If the current node is the goal node, reconstruct the path and return it with the success function
        if current_node == goal_node:
            return success(parents, current_node)

        print(" - ", end="")
        # Get all the successors of the current node
        successors = graph.find_successors(current_node)

        # For each successor, put the current_node as a parent and add the successor to the list of nodes to be explored (fringe)
        for successor in successors:
            parents[successor] = current_node
            fringe.put(successor)

        # Add the current node to the explored node
        explored.add(current_node)
    # If we reach this point, there is no solution to go from the starting node to goal node
    return None
