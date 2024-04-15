from queue import LifoQueue

from success import success


def dfs_search(graph, starting_node, goal_node):
    fringe = LifoQueue()
    explored = set()

    fringe.put(starting_node)

    parents = {starting_node: None}

    print("Parsed nodes: ")

    while fringe:
        current_node = fringe.get()
        print("Node: " + current_node.name)
        if current_node in explored:
            continue
        if current_node == goal_node:
            return success(parents, current_node)

        successors = graph.find_successors(current_node)
        for successor in successors:
            parents[successor] = current_node
            fringe.put(successor)
        explored.add(current_node)
    return None
