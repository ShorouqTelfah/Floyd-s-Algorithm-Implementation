"""floyd warshall algorithm in iterative way without negative """
import sys
import itertools
"""assign the the maximum value (infinite) to NO_PATH variable """
NO_PATH = sys.maxsize
# the weighted graph matrix
graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]
# git the number of vertices in the graph
MAX_LENGTH = len(graph[0])

"""define floyd warshall function to find the shortest distance """ 


def floyd_algorithm(distance):

    """iterate over all possible pairs"""
    for intermediate, start_node, end_node \
            in itertools.product\
            (range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        """to update the shortest distance between the start_node and the 
        end_node via intermediate node """
        distance[start_node][end_node] = min(distance[start_node][end_node], distance[start_node][intermediate] + distance[intermediate][end_node] )
        # print the result
    print(distance)

# call the function


floyd_algorithm(graph)
