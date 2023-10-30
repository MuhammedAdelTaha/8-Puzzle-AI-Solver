<!DOCTYPE html>
<html lang="en">
    <body>
        <h1>AI Search Algorithms</h1>
        <p>This project discuss the main differences between the
            different types of AI Search Algorithms like the completeness
            and the optimality of the algorithm.
            We used the 8-puzzle problem as an application that demonstrates
            these differences.
        </p>
        <hr>
        <h2>Table of contents</h2>
        <ul>
            <li><a href="#dfs">Depth First Search</a></li>
            <li><a href="#bfs">Breadth First Search</a></li>
            <li><a href="#a-star-man">A* Search with Manhattan heuristic</a></li>
            <li><a href="#a-star-euc">A* Search with Euclidean heuristic</a></li>
            <li><a href="#comp">Test Cases & Comparisons</a></li>
        </ul>
        <hr>
        <h2 id="dfs">Depth First Search</h2>
        <p>
            - Data Structure: Stack <br>
            - Completeness: Not complete <br>
            - Optimality: Not optimal <br>
            - Time: O(b ^ m) <br>
            - Space: O(b * m) <br>
            - b is the branching factor <br>
            - m is the maximum possible search tree depth <br>
            - DFS is good only when it comes to space complexity
        </p>
        <hr>
        <h2 id="bfs">Breadth First Search</h2>
        <p>
            - Data Structure: Queue <br>
            - Completeness: Complete <br>
            - Optimality: Optimal <br>
            - Time: O(b ^ s) <br>
            - Space: O(b ^ s) <br>
            - b is the branching factor <br>
            - s is the level where the goal state is present <br>
            - BFS is not very well dealing with space <br>
            - BFS can find the optimal solution only if all costs are equal to one
        </p>
        <hr>
        <h2 id="a-star-man">A* Search with Manhattan heuristic</h2>
        <p>
            - Data Structure: Priority Queue <br>
            - Completeness: Complete <br>
            - Optimality: Optimal <br>
            - A* Search Always finds the optimal solution <br>
            - A* Search considers the past cost and the upcoming heuristic cost <br>
            - Manhattan distance = |x1 - x2| + |y1 - y2|
        </p>
        <hr>
        <h2 id="a-star-euc">A* Search with Euclidean heuristic</h2>
        <p>
            - Data Structure: Priority Queue <br>
            - Completeness: Complete <br>
            - Optimality: Optimal <br>
            - A* Search Always finds the optimal solution <br>
            - A* Search considers the past cost and the upcoming heuristic cost <br>
            - Euclidean distance = sqrt((x1 - x2) ^ 2 + (y1 - y2) ^ 2)
        </p>
        <hr>
        <h2 id="comp">Test Cases & Comparisons</h2>
        <img src="images/t1.png" alt=""> <hr>
        <img src="images/t2.png" alt=""> <hr>
        <img src="images/t3.png" alt=""> <hr>
        <img src="images/t4.png" alt=""> <hr>
        <img src="images/t5.png" alt=""> <hr>
        <img src="images/o.png" alt="">
    </body>
</html>