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

    print("\nPath found: ", end=" ")
    # Print each node of the path
    for node in path_found:
        # If it is the goal node, then don't add the " - " at the end
        if node.name != goal_node.name:
            print(node.name, end=" - ")
        else:
            print(node.name)
    return path_found
