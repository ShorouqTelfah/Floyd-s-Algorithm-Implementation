# Mid_Module-Assignment
This repository to submit my work on Floyd's algorithm.  
                                        Floyd's Algorithm Implementation

This repo shows the work of Floyd's algorithm to find the shortest paths between all pairs of vertices in a given graph. With both iterative and recursive implementations of the algorithm.
•	Installation

To use this project, you must install Python on your system. Clone the repository to your local machine:
```bash
git clone https://github.com/your_username/floyds-algorithm.git
Navigate to the project directory:
cd mid_module_assignment

•	Usage
You can use both the iterative and recursive implementations of Floyd's algorithm by importing the corresponding functions from the mid_module_assignment module.

•	Create a graph (adjacency matrix)
graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
] 
# Use the iterative implementation
floyd_algorithm(distance)

# Use the recursive implementation
floyd_algorithm(graph)

•	Running Tests
To run unit tests, execute the following command:

pytest

To run performance tests, execute:

pytest --benchmark-autosave

This project is licensed under the MIT License - see the LICENSE file for details.
In this README file:
- Installation instructions guide users on how to clone the repository, install dependencies, and set up the project.
- The usage section demonstrates how to use the implemented functions in Python code.
- Running Tests section explains how to run unit tests and performance tests using pytest.
- License section provides information about the project's license.
