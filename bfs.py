from success import success


def bfs_search(graph, starting_node, goal_node):
    fringe = []
    explored = set()

    fringe.append(starting_node)

    parents = {starting_node: None}

    print("Parsed nodes: ")
    while fringe:
        current_node = fringe[0]
        print("Node: " + current_node.name)

        if current_node == goal_node:
            return success(parents, current_node)

        successors = graph.find_successors(current_node)
        for successor in successors:
            if successor in explored or successor in fringe:
                continue
            fringe.append(successor)
            parents[successor] = current_node
        explored.add(current_node)
        fringe.remove(current_node)
    return None
