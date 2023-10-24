import time
from search import goal_state, bfs, dfs, a_star_with_manhattan, a_star_with_euclidean, print_path


def display_results(solution, time_taken):
    parents = solution[0]
    expanded_nodes = solution[1]
    if parents is not None:
        state = goal_state
        path = [state]
        while state != parents[state]:
            state = parents[state]
            path.append(state)

        print_path(path)
        print("Depth:", len(path) - 1)
        print("Cost of the path:", len(path) - 1)

    print("Number of expanded nodes:", expanded_nodes)
    print("Running time:", time_taken)


def bfs_test(initial_state: tuple):
    print("---------------------------")
    print("Using Breadth First Search:")
    print("---------------------------")
    start = time.time()
    sol = bfs(initial_state)
    end = time.time()
    display_results(sol, end - start)


def dfs_test(initial_state: tuple):
    print("-------------------------")
    print("Using Depth First Search:")
    print("-------------------------")
    start = time.time()
    sol = dfs(initial_state)
    end = time.time()
    display_results(sol, end - start)


def a_star_with_manhattan_test(initial_state: tuple):
    print("-------------------------")
    print("A* Search with manhattan:")
    print("-------------------------")
    start = time.time()
    sol = a_star_with_manhattan(initial_state)
    end = time.time()
    display_results(sol, end - start)


def a_star_with_euclidean_test(initial_state: tuple):
    print("-------------------------")
    print("A* Search with euclidean:")
    print("-------------------------")
    start = time.time()
    sol = a_star_with_euclidean(initial_state)
    end = time.time()
    display_results(sol, end - start)


# test case
# ---------
# bfs_test((123456870, 0))
# dfs_test((123456870, 0))
# a_star_with_manhattan_test((123456870, 0))
# a_star_with_euclidean_test((123456870, 0))
# ------------------------------------------
# bfs_test((125340678, 3))
# dfs_test((125340678, 3))
# a_star_with_manhattan_test((125340678, 3))
# a_star_with_euclidean_test((125340678, 3))
# ------------------------------------------
# bfs_test((142658730, 0))
# dfs_test((142658730, 0))
# a_star_with_manhattan_test((142658730, 0))
# a_star_with_euclidean_test((142658730, 0))
# ------------------------------------------
# bfs_test((102754863, 7))
# dfs_test((102754863, 7))
# a_star_with_manhattan_test((102754863, 7))
# a_star_with_euclidean_test((102754863, 7))
# ------------------------------------------
# bfs_test((806547231, 7))
# dfs_test((806547231, 7))
# a_star_with_manhattan_test((806547231, 7))
# a_star_with_euclidean_test((806547231, 7))
