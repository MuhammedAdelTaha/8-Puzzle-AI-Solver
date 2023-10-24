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
    # digit_pos is the position of the digit to be swapped with the empty space
    # neighbors is a list of tuples every tuple represents a state of the board as (number, position of the empty space)
    number = state[0]
    zero_pos = state[1]
    neighbors = []

    # Up
    digit_pos = zero_pos + 3
    if digit_pos <= 8:
        neighbors.append((swap_digits(number, zero_pos, digit_pos), digit_pos))

    # Left
    if zero_pos % 3 < 2:
        digit_pos = zero_pos + 1
        neighbors.append((swap_digits(number, zero_pos, digit_pos), digit_pos))

    # Down
    digit_pos = zero_pos - 3
    if digit_pos >= 0:
        neighbors.append((swap_digits(number, zero_pos, digit_pos), digit_pos))

    # Right
    if zero_pos % 3 > 0:
        digit_pos = zero_pos - 1
        neighbors.append((swap_digits(number, zero_pos, digit_pos), digit_pos))

    return neighbors


def bfs(initial_state: tuple):
    """
    This function takes the initial state of the 8-puzzle board and returns a tuple containing
    a dictionary of parents and children (None if no solution exists) and the number of expanded nodes.
    The frontier is a Queue data structure.
    """
    frontier = []
    explored = set()
    parents = dict()
    frontier.append(initial_state)
    parents[initial_state[0]] = initial_state[0]

    while len(frontier) > 0:
        state = frontier.pop(0)
        explored.add(state)

        if state[0] == goal_state:
            return parents, len(explored)

        neighbors = get_neighbors(state)
        for neighbor in neighbors:
            if neighbor[0] not in parents and neighbor not in explored:
                frontier.append(neighbor)
                parents[neighbor[0]] = state[0]

    return None, len(explored)


def dfs(initial_state: tuple):
    """
    This function takes the initial state of the 8-puzzle board and returns a tuple containing
    a dictionary of parents and children (None if no solution exists) and the number of expanded nodes.
    The frontier is a Stack data structure.
    """
    frontier = []
    explored = set()
    parents = dict()
    frontier.append(initial_state)
    parents[initial_state[0]] = initial_state[0]

    while len(frontier) > 0:
        state = frontier.pop()
        explored.add(state)

        if state[0] == goal_state:
            return parents, len(explored)

        neighbors = get_neighbors(state)
        for neighbor in neighbors:
            if neighbor[0] not in parents and neighbor not in explored:
                frontier.append(neighbor)
                parents[neighbor[0]] = state[0]

    return None, len(explored)


def a_star_with_manhattan(initial_state: tuple):
    """
    This function takes the initial state of the 8-puzzle board and returns a tuple containing
    a dictionary of parents and children (None if no solution exists) and the number of expanded nodes.
    The frontier is a Priority Queue data structure (its key = manhattan heuristic + cost to reach that state).
    """
    frontier = []
    explored = set()
    parents = dict()
    x = initial_state[1] // 3
    y = initial_state[1] % 3
    manhattan = abs(x - 2) + abs(y - 2)
    q.heappush(frontier, (manhattan, (0, initial_state)))
    parents[initial_state[0]] = initial_state[0]

    while len(frontier) > 0:
        _, v = q.heappop(frontier)
        distance = v[0]
        state = v[1]
        if state in explored:
            continue
        explored.add(state)

        if state[0] == goal_state:
            return parents, len(explored)

        neighbors = get_neighbors(state)
        for neighbor in neighbors:
            if neighbor[0] not in parents and neighbor not in explored:
                x = neighbor[1] // 3
                y = neighbor[1] % 3
                manhattan = abs(x - 2) + abs(y - 2)
                q.heappush(frontier, (manhattan + distance + 1, (distance + 1, neighbor)))
                parents[neighbor[0]] = state[0]

    return None, len(explored)


def a_star_with_euclidean(initial_state: tuple):
    """
    This function takes the initial state of the 8-puzzle board and returns a tuple containing
    a dictionary of parents and children (None if no solution exists) and the number of expanded nodes.
    The frontier is a Priority Queue data structure (its key = Euclidean heuristic + cost to reach that state).
    """
    frontier = []
    explored = set()
    parents = dict()
    x = initial_state[1] // 3
    y = initial_state[1] % 3
    euclidean = math.sqrt(pow(x - 2, 2) + pow(y - 2, 2))
    q.heappush(frontier, (euclidean, (0, initial_state)))
    parents[initial_state[0]] = initial_state[0]

    while len(frontier) > 0:
        _, v = q.heappop(frontier)
        distance = v[0]
        state = v[1]
        if state in explored:
            continue
        explored.add(state)

        if state[0] == goal_state:
            return parents, len(explored)

        neighbors = get_neighbors(state)
        for neighbor in neighbors:
            if neighbor[0] not in parents and neighbor not in explored:
                x = neighbor[1] // 3
                y = neighbor[1] % 3
                euclidean = math.sqrt(pow(x - 2, 2) + pow(y - 2, 2))
                q.heappush(frontier, (euclidean + distance + 1, (distance + 1, neighbor)))
                parents[neighbor[0]] = state[0]

    return None, len(explored)
