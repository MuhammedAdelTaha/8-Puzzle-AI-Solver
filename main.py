import time
from search import goal_state, dfs, bfs, a_star_with_manhattan, a_star_with_euclidean, print_path


def get_path(parents):
    if parents is not None:
        state = goal_state
        path = [state]
        while state != parents[state]:
            state = parents[state]
            path.append(state)

        return path
    return None


def search_results(search_technique, initial_state: tuple):
    start = time.time()
    parents, expanded_nodes, depth = search_technique(initial_state)
    running_time = time.time() - start
    path = get_path(parents)
    return path, depth, expanded_nodes, running_time


def display_results_on_terminal(search_technique, test):
    path, depth, expanded_nodes, running_time = search_results(search_technique, test)

    if path is not None:
        print_path(path)
        print("Cost of the path:", len(path) - 1)
    else:
        print("Not Found")
    print("Depth:", depth)
    print("Number of expanded nodes:", expanded_nodes)
    print("Running time:", running_time)


def test_on_terminal(test):
    print("-------------------------")
    print("Using Depth First Search:")
    print("-------------------------")
    display_results_on_terminal(dfs, test)

    print("---------------------------")
    print("Using Breadth First Search:")
    print("---------------------------")
    display_results_on_terminal(bfs, test)

    print("-------------------------")
    print("A* Search with manhattan:")
    print("-------------------------")
    display_results_on_terminal(a_star_with_manhattan, test)

    print("-------------------------")
    print("A* Search with euclidean:")
    print("-------------------------")
    display_results_on_terminal(a_star_with_euclidean, test)


def write_results_on_file(output_file, search_technique, test):
    path, depth, expanded_nodes, running_time = search_results(search_technique, test)

    if path is not None:
        output_file.write("Cost of the path: " + str(len(path) - 1) + '\n')
    else:
        output_file.write("Not Found" + '\n')
    output_file.write("Depth: " + str(depth) + '\n')
    output_file.write("Number of expanded nodes: " + str(expanded_nodes) + '\n')
    output_file.write("Running time: " + str(running_time) + '\n')


def test_on_file(input_file_name, output_file_name):
    with (open(input_file_name, 'rt', encoding='utf-8') as input_file,
          open(output_file_name, 'wt', encoding='utf-8') as output_file
          ):

        for line in input_file:
            test = line.strip()
            if test == '':
                continue

            zero_idx = 8 - test.find('0')
            num = int(test)
            output_file.write('DFS\n')
            write_results_on_file(output_file, dfs, (num, zero_idx, 0))
            output_file.write('\nBFS\n')
            write_results_on_file(output_file, bfs, (num, zero_idx, 0))
            output_file.write('\nA* with Manhattan\n')
            write_results_on_file(output_file, a_star_with_manhattan, (num, zero_idx, 0))
            output_file.write('\nA* with Euclidean\n')
            write_results_on_file(output_file, a_star_with_euclidean, (num, zero_idx, 0))
            output_file.write('\n==============================================\n')


# test case
# ---------
# test_on_terminal((123456870, 0, 0))
# ------------------------------------------
# test_on_terminal((125340678, 3, 0))
# ------------------------------------------
# test_on_terminal((142658730, 0, 0))
# ------------------------------------------
# test_on_terminal((102754863, 7, 0))
# ------------------------------------------
# test_on_terminal((806547231, 7, 0))
# ------------------------------------------
# test_on_terminal((312645078, 2, 0))
# ------------------------------------------
# test_on_terminal((102345678, 7, 0))
# ------------------------------------------
# test_on_terminal((312480657, 3, 0))
# ------------------------------------------
# test_on_terminal((538140276, 3, 0))
# ------------------------------------------
# test_on_terminal((821546037, 2, 0))
# ------------------------------------------
# test_on_file('input.txt', 'output.txt')
