# Mid_Module_Assignment
This repository to submit my work on Floyd's algorithm.  

                                              Floyd's Algorithm Implementation

This repository contains the work to implement both the recursive and iterative cods for the Floyd’s algorithm to find the shortest paths between all pairs of vertices in a given graph:
•	Input graph (adjacency matrix)
graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
] 


Which represent list of lists each value represent the distance between vertex ‘i’(rows) to vertex ’j’ (column),NO_PATH indicate that there is no path between this pair of vertices.
Full recursive code with document in this repository will calculate the shortest distance between all pairs of vertices in addition to other cod used the iterative way to return the same result.
Both codes were tested against their performance and compared to each other. Moreover the unit test with coverage was conducted to each of them.     

•	Installation
To use this project, you must install Python on your system. Clone the repository to your local machine:

```bash
-git clone https://github.com/your_username/floyds-algorithm.git

Navigate to the project directory:
-cd mid_module_assignment

•	Usage
You can use both the iterative and recursive implementations of Floyd's algorithm by importing the corresponding functions from the mid_module_assignment module.

•	Use the iterative implementation
          floyd_algorithm(distance)

•	Use the recursive implementation
      floyd_algorithm(graph)

•	License
This project is licensed under the MIT License - see the LICENSE file for details
