import unittest
import sys
import coverage
import itertools

NO_PATH = sys.maxsize

graph1 = [[0, 7, NO_PATH, 8],
          [NO_PATH, 0, 5, NO_PATH],
          [NO_PATH, NO_PATH, 0, 2],
          [NO_PATH, NO_PATH, NO_PATH, 0]]


def floyd_algorithm(distance):
    MAX_LENGTH = len(graph1[0])
    for intermediate, start_node, end_node \
            in itertools.product \
                (range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        distance[start_node][end_node] = min(distance[start_node][end_node],
                                             distance[start_node][intermediate] + distance[intermediate][end_node])
    print(distance)


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
    cov.save()

    cov.report()
