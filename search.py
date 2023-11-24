"""
The state consists of (the state number representation, the zero-digit position in the number representation
                        of the state, the depth of the state)
The initial state depth is zero
"""
import heapq as q
import math

goal_state = 1_2_3_4_5_6_7_8


def print_state(ls):
    """
    This function takes a state list and prints it in a form of table.
    """
    for i in range(0, len(ls), 3):
        print(ls[i], ls[i + 1], ls[i + 2])


def print_path(states):
    """
    This function takes a path to the goal node and prints every state from the initial one to the goal state.
    """
    for i in range(len(states) - 1, -1, -1):
        ls = []
        for j in range(8, -1, -1):
            ls.append((states[i] % pow(10, j + 1)) // pow(10, j))
        print_state(ls)
        print()


def swap_digits(number, zero_pos, digit_pos):
    """
    This function takes a number, the position of the zero-digit on that number, and the position of the digit to be
    swapped with the zero-digit and returns the number after swapping.
    """
    swapped_digit = (number % pow(10, digit_pos + 1)) // pow(10, digit_pos)
    return number + swapped_digit * pow(10, zero_pos) - swapped_digit * pow(10, digit_pos)


def get_neighbors(state: tuple):
    """
    This function takes a state and returns the valid states to go to from this state.
    """
    # state[0] is the board representation number
    # state[1] is the zero position
    # state[2] is the depth to this state
    # digit_pos is the position of the digit to be swapped with the empty space
    # neighbors is a list of tuples every tuple represents a state of the board as (number, position of the empty space)
    number, zero_pos, depth = state
    neighbors = []

    # Up
    digit_pos = zero_pos + 3
    if digit_pos <= 8:
        neighbors.append((swap_digits(number, zero_pos, digit_pos), digit_pos, depth + 1))

    # Left
    if zero_pos % 3 < 2:
        digit_pos = zero_pos + 1
        neighbors.append((swap_digits(number, zero_pos, digit_pos), digit_pos, depth + 1))

    # Down
    digit_pos = zero_pos - 3
    if digit_pos >= 0:
        neighbors.append((swap_digits(number, zero_pos, digit_pos), digit_pos, depth + 1))

    # Right
    if zero_pos % 3 > 0:
        digit_pos = zero_pos - 1
        neighbors.append((swap_digits(number, zero_pos, digit_pos), digit_pos, depth + 1))

    return neighbors


def bfs(initial_state: tuple):
    """
    This function takes the initial state of the 8-puzzle board and returns a tuple containing a dictionary of parents
    and children (None if no solution exists) and the number of expanded nodes and the depth of the tree.
    The frontier is a Queue data structure.
    """
    frontier = []
    explored = set()
    parents = dict()
    frontier.append(initial_state)
    parents[initial_state[0]] = initial_state[0]
    max_depth = 0

    while len(frontier) > 0:
        state = frontier.pop(0)
        explored.add(state)

        if state[0] == goal_state:
            return parents, len(explored), max_depth

        neighbors = get_neighbors(state)
        for neighbor in neighbors:
            number, _, depth = neighbor
            if number not in parents and neighbor not in explored:
                frontier.append(neighbor)
                parents[number] = state[0]
                max_depth = max(max_depth, depth)

    return None, len(explored), max_depth


def dfs(initial_state: tuple):
    """
    This function takes the initial state of the 8-puzzle board and returns a tuple containing a dictionary of parents
    and children (None if no solution exists) and the number of expanded nodes and the depth of the tree.
    The frontier is a Stack data structure.
    """
    frontier = []
    explored = set()
    parents = dict()
    frontier.append(initial_state)
    parents[initial_state[0]] = initial_state[0]
    max_depth = 0

    while len(frontier) > 0:
        state = frontier.pop()
        explored.add(state)

        if state[0] == goal_state:
            return parents, len(explored), max_depth

        neighbors = get_neighbors(state)
        for neighbor in neighbors:
            number, _, depth = neighbor
            if number not in parents and neighbor not in explored:
                frontier.append(neighbor)
                parents[number] = state[0]
                max_depth = max(max_depth, depth)

    return None, len(explored), max_depth


def calc_heuristic(number, heuristic_type):
    """
    This function takes the number representation of the 8-puzzle and calculates its manhattan/Euclidean heuristic
    """
    total = 0
    for i in range(8, -1, -1):
        digit = (number % pow(10, i + 1)) // pow(10, i)
        curr_pos = 8 - i
        x_curr = curr_pos // 3
        y_curr = curr_pos % 3
        x_right_pos = digit // 3
        y_right_pos = digit % 3
        if heuristic_type == "manhattan":
            total += abs(x_right_pos - x_curr) + abs(y_right_pos - y_curr)
        elif heuristic_type == "euclidean":
            total += math.sqrt(pow(x_right_pos - x_curr, 2) + pow(y_right_pos - y_curr, 2))

    return total


def a_star_with_manhattan(initial_state: tuple):
    """
    This function takes the initial state of the 8-puzzle board and returns a tuple containing a dictionary of parents
    and children (None if no solution exists) and the number of expanded nodes and the depth of the tree.
    The frontier is a Priority Queue data structure (its key = manhattan heuristic + cost to reach that state).
    """
    frontier = []
    explored = set()
    parents = dict()
    manhattan = calc_heuristic(initial_state[0], "manhattan")
    q.heappush(frontier, (manhattan, initial_state))
    parents[initial_state[0]] = initial_state[0]
    max_depth = 0

    while len(frontier) > 0:
        _, state = q.heappop(frontier)
        explored.add(state)

        if state[0] == goal_state:
            return parents, len(explored), max_depth

        neighbors = get_neighbors(state)
        for neighbor in neighbors:
            number, _, depth = neighbor
            if number not in parents and neighbor not in explored:
                manhattan = calc_heuristic(number, "manhattan")
                q.heappush(frontier, (manhattan + 2 * depth, neighbor))
                parents[number] = state[0]
                max_depth = max(max_depth, depth)

    return None, len(explored), max_depth


def a_star_with_euclidean(initial_state: tuple):
    """
    This function takes the initial state of the 8-puzzle board and returns a tuple containing a dictionary of parents
    and children (None if no solution exists) and the number of expanded nodes and the depth of the tree.
    The frontier is a Priority Queue data structure (its key = Euclidean heuristic + cost to reach that state).
    """
    frontier = []
    explored = set()
    parents = dict()
    euclidean = calc_heuristic(initial_state[0], "euclidean")
    q.heappush(frontier, (euclidean, initial_state))
    parents[initial_state[0]] = initial_state[0]
    max_depth = 0

    while len(frontier) > 0:
        _, state = q.heappop(frontier)
        explored.add(state)

        if state[0] == goal_state:
            return parents, len(explored), max_depth

        neighbors = get_neighbors(state)
        for neighbor in neighbors:
            number, _, depth = neighbor
            if number not in parents and neighbor not in explored:
                euclidean = calc_heuristic(number, "euclidean")
                q.heappush(frontier, (euclidean + 2 * depth, neighbor))
                parents[number] = state[0]
                max_depth = max(max_depth, depth)

    return None, len(explored), max_depth
