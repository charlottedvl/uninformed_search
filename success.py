def success(parents, goal_node):
    # Construct the path
    path_found = []
    current_node = goal_node

    while current_node:
        path_found.append(current_node)
        if current_node.name == "Start": break
        current_node = parents[current_node]

    # Reverse the path to have from start node to goal node
    path_found.reverse()

    print("Path found")
    for node in path_found:
        # Print each node of the path
        print("Node:",
              node.name)
    return path_found