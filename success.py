def success(parents, goal_node):
    # Construct the path
    path_found = []
    current_node = goal_node

    while current_node:
        # Add the current node to the path
        path_found.append(current_node)
        # If the current_node is the Start node, then stop
        if current_node.name == "Start": break
        # Update the current node as the parent of the current node
        current_node = parents[current_node]

    # Reverse the path to have from Start node to Goal node
    path_found.reverse()

    print("Path found")
    for node in path_found:
        # Print each node of the path
        print("Node:",
              node.name)
    return path_found
