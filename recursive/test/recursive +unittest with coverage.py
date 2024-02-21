# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:08:51 2024

@author: shoro
"""

import unittest
import sys
import coverage

NO_PATH = sys.maxsize
graph1= [
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
            return min(recursive_floyd_algorithm(i, j, k - 1),
                       recursive_floyd_algorithm(i, k, k - 1) + recursive_floyd_algorithm(k, j, k - 1))

    result = [[recursive_floyd_algorithm(i, j, n - 1) for j in range(n)] for i in range(n)]
    return result

class TestFloydAlgorithm(unittest.TestCase):

    def test_floyd_algorithm(self):
        expected_result1 = [
            [0, 7, 12, 8],
            [sys.maxsize, 0, 5, 7],
            [sys.maxsize, sys.maxsize, 0, 2],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0]
        ]
        result = floyd_algorithm(graph1)
        self.assertEqual(result, expected_result1)
    def test_floyd_algorithm2(self):
        expected_result2 = [
            [0, 7, 12, 8],
            [sys.maxsize, 0, 3, 7],
            [sys.maxsize, sys.maxsize, 0, 2],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0]
        ]
        result2 = floyd_algorithm(graph1)
        self.assertEqual(result2, expected_result2)



if __name__ == '__main__':
    
    cov = coverage.Coverage()

   
    cov.start()


    unittest.main()

  
    cov.stop()

    
    cov.save()

    cov.report()