<h1 align="center">8-Puzzle AI Solver</h1>
<p align="center">
This project discusses the main differences between the different types of AI Search Algorithms like the completeness and the optimality of the algorithm. We used the 8-puzzle problem as an application that demonstrates these differences.
</p>

[![GitHub license](https://img.shields.io/github/license/MuhammedAdelTaha/8-Puzzle-AI-Solver)](https://github.com/MuhammedAdelTaha/8-Puzzle-AI-Solver/LICENSE) 

# Table of contents

- [Depth First Search](#depth-first-search)
- [Breadth First Search](#breadth-first-search)
- [A* Search with Manhattan heuristic](#a-search-with-manhattan-heuristic)
- [A* Search with Euclidean heuristic](#a-search-with-euclidean-heuristic)
- [Test Cases & Comparisons](#test-cases--comparisons)

# Depth First Search

- Data Structure: Stack <br>
- Completeness: Not complete <br>
- Optimality: Not optimal <br>
- Time: O(b ^ m) <br>
- Space: O(b * m) <br>
- b is the branching factor <br>
- m is the maximum possible search tree depth <br>
- DFS is good only when it comes to space complexity

# Breadth First Search

- Data Structure: Queue <br>
- Completeness: Complete <br>
- Optimality: Optimal <br>
- Time: O(b ^ s) <br>
- Space: O(b ^ s) <br>
- b is the branching factor <br>
- s is the level where the goal state is present <br>
- BFS is not very well dealing with space <br>
- BFS can find the optimal solution only if all costs are equal to one

# A* Search with Manhattan heuristic

- Data Structure: Priority Queue <br>
- Completeness: Complete <br>
- Optimality: Optimal <br>
- A* Search Always finds the optimal solution <br>
- A* Search considers the past cost and the upcoming heuristic cost <br>
- Manhattan distance = |x1 - x2| + |y1 - y2|

# A* Search with Euclidean heuristic

- Data Structure: Priority Queue <br>
- Completeness: Complete <br>
- Optimality: Optimal <br>
- A* Search Always finds the optimal solution <br>
- A* Search considers the past cost and the upcoming heuristic cost <br>
- Euclidean distance = sqrt((x1 - x2) ^ 2 + (y1 - y2) ^ 2)

# Test Cases & Comparisons
<img src="images/t1.png" alt="">
<img src="images/t2.png" alt="">
<img src="images/t3.png" alt="">
<img src="images/t4.png" alt="">
<img src="images/t5.png" alt="">
<img src="images/o.png" alt="">
