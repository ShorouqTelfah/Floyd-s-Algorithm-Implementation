# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:27:48 2024

@author: shoro
"""

import timeit
import sys

NO_PATH = sys.maxsize
graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
]
def floyd_algorithm(graph):

    n = len(graph)

    def recursive_floyd_algorithm(i, j, k):

        if k == 0:
            return graph[i][j]
        else:
            return min(recursive_floyd_algorithm(i, j, k-1),
                       recursive_floyd_algorithm(i, k, k-1) + recursive_floyd_algorithm(k, j, k-1))

    result = [[recursive_floyd_algorithm(i, j, n-1) for j in range(n)] for i in range(n)]
    return result


iteration_num = 1000


execution_time = timeit.timeit(lambda: floyd_algorithm(graph), number=iteration_num)
print("Average execution time per iteration:", execution_time / iteration_num, "seconds")
