# floyd's Warshall code in recursion way without negative value
import sys
# assign the infinity (maximum value )to the NO_PATH variable to represent the absence of direction
NO_PATH = sys.maxsize
# the input graph matrex
graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
]

""" defining the floyd_algorithm function to calculate the shortest distance between all pairs of vertices in the graph
- argument is the graph  which is a list of lists, each element is an integer representing the distance
 between two vertices in the graph 'i' and 'j'.
 - the return value is the shortest distance between the two vertices after
  all vertices have been treated as intermediate nodes"""


def floyd_algorithm(graph):

    # to calculate the number of vertices in the graph
    n = len(graph)
    """ defining a nested loop to find the shortest distance between all pairs of vertices in the graph 
    where the function recursively finds the shortest distance between 'i': the starting vertex and 'j': the destination 
    vertex considering 'k' as an intermediate"""
    def recursive_floyd_algorithm(i, j, k):
        # base case
        if k == 0:
            return graph[i][j]
        # recursive case
        else:
            return min(recursive_floyd_algorithm(i, j, k-1),
                       recursive_floyd_algorithm(i, k, k-1) + recursive_floyd_algorithm(k, j, k-1))

    # initialise the result matrix
    result = [[recursive_floyd_algorithm(i, j, n-1) for j in range(n)] for i in range(n)]
    return result


# calling the floyd_algorithm
for row in floyd_algorithm(graph):
    print(row)
