# Creating the nodes
from bfs import bfs_search
from dfs import dfs_search
from graph import Graph
from node import Node

start_node = Node("Start")
A_node = Node("A")
B_node = Node("B")
C_node = Node("C")
D_node = Node("D")
goal_node = Node("Goal")

# Creating the list of successors for each node
successors_list = {
    start_node: [A_node, B_node, D_node],
    A_node: [start_node, C_node],
    B_node: [start_node, D_node],
    C_node: [A_node, D_node, goal_node],
    D_node: [start_node, B_node, C_node, goal_node],
    goal_node: [C_node, D_node]
}

# Creating the graph
graph_given = Graph(successors_list)



# Performing the BFS search
print('BFS')
path_bfs = bfs_search(graph_given, start_node, goal_node)
