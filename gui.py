import tkinter as tk
from tkinter import ttk
from search import dfs, bfs, a_star_with_manhattan, a_star_with_euclidean, search_results


def validate_input(value):
    # This function is called during validation to check if the input is valid (1 to 8 or empty)
    if not value:
        return True  # Empty string is considered valid
    if len(value) > 1:
        return False
    try:
        number = int(value)
        return 0 <= number <= 8
    except ValueError:
        return False


class ResultsScreen:
    def __init__(self, root, results):
        self.root = root
        root.title("8-Puzzle-AI-Solver Results")

        # Set fixed width and height for the window
        self.root.geometry("700x600")

        # Disable window resizing
        self.root.resizable(False, False)

        # Set window position in the top-left corner
        root.geometry("+0+0")

        # Create Back button in the top left corner with margin 10px
        back_button = ttk.Button(root, text="Back", command=self.back_to_main, style='My.TButton')

        # Configure the style for the button
        self.root.style = ttk.Style()
        self.root.style.configure('My.TButton', font=('Arial', 16), padding=(5, 5))

        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Display results on labels
        path, depth, expanded_nodes, running_time = results

        if path is not None:
            ttk.Label(root, font=('Arial', 14), text="Cost: {}".format(len(path))).grid(row=1, column=1)
        else:
            ttk.Label(root, font=('Arial', 14), text="No Solution!").grid(row=1, column=1)

        ttk.Label(root, font=('Arial', 14), text="Depth: {}".format(depth)).grid(row=2, column=1)
        ttk.Label(root, font=('Arial', 14), text="Expanded Nodes: {}".format(expanded_nodes)).grid(row=3, column=1)
        ttk.Label(root, font=('Arial', 14), text="Time: {:.6f} seconds".format(running_time)).grid(row=4, column=1)
        if path is None:
            return

        # Display initial state
        self.path = path
        # Starting from the last state
        self.current_index = len(path) - 1
        # Adjust the speed (in milliseconds) for smoother transitions
        self.transition_speed = 200
        # First display the initial state
        self.display_state()

        # Add buttons for navigation
        navigation_frame = ttk.Frame(root)
        navigation_frame.grid(row=8, column=1, pady=10)

        previous_button = ttk.Button(navigation_frame, text="Previous", command=self.show_previous_state, width=10)
        previous_button.grid(row=0, column=0, ipadx=5, ipady=5, padx=5, pady=10)

        next_button = ttk.Button(navigation_frame, text="Next", command=self.show_next_state, width=10)
        next_button.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, pady=10)

    def display_state(self):
        # Display the current state on the grid
        state = self.path[self.current_index]
        self.display_grid(state)

    def display_grid(self, state):
        # Create a frame to hold the grid
        grid_frame = ttk.Frame(self.root)
        grid_frame.grid(row=5, column=1, padx=5, pady=10)

        # Reshape the state string into a 2D list for easier indexing
        grid_values = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                # from right bottom to left top
                cell_idx = 8 - (i * 3 + j)
                grid_values[i][j] = (state % pow(10, cell_idx + 1)) // pow(10, cell_idx)

        # Create labels for each cell in the grid
        for i in range(3):
            for j in range(3):
                cell_value = grid_values[i][j]
                label_text = ' ' if cell_value == 0 else str(cell_value)

                cell_label = ttk.Label(grid_frame, text=label_text, font=('Arial', 14), relief=tk.GROOVE, width=10)
                cell_label.grid(row=i, column=j, ipadx=15, ipady=30)

    def show_previous_state(self):
        # Show the previous state in the list
        if self.current_index < len(self.path) - 1:
            self.current_index += 1
            self.root.after(self.transition_speed, self.display_state)

    def show_next_state(self):
        # Show the next state in the list
        if self.current_index > 0:
            self.current_index -= 1
            self.root.after(self.transition_speed, self.display_state)

    def back_to_main(self):
        # Destroy the current results screen and go back to the main screen
        self.root.destroy()


class EightPuzzleGUI:
    def __init__(self, root):
        self.root = root
        root.title("8-Puzzle-AI-Solver")

        # Set fixed width and height for the window
        self.root.geometry("700x600")

        # Disable window resizing
        self.root.resizable(False, False)

        # Set window position in the top-left corner
        root.geometry("+0+0")

        # Create a frame to hold the grid
        grid_frame = ttk.Frame(root)
        grid_frame.grid(row=0, column=0, padx=10, pady=10)

        # Initialize the grid cells
        self.grid_cells = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                cell = ttk.Entry(grid_frame, width=10, font=('Arial', 14), justify='center', validate='key',
                                 validatecommand=(root.register(validate_input), '%P'))
                cell.grid(row=i, column=j, ipadx=50, ipady=50)
                self.grid_cells[i][j] = cell

        # Set the initial focus on the center cell
        self.grid_cells[0][0].focus_set()

        # Create the radio choices
        radio_frame = ttk.Frame(root)
        radio_frame.grid(row=1, column=0, padx=10, pady=10)

        self.choice_var = tk.StringVar(value='DFS')
        choices = ['DFS', 'BFS', 'A* Manhattan', 'A* Euclidean']
        for i, choice in enumerate(choices):
            radio_button = ttk.Radiobutton(radio_frame, text=str(choice), variable=self.choice_var, value=choice)
            radio_button.pack(side='left', padx=5)

        # Create the Solve button
        solve_button = ttk.Button(root, text="AI Solver", command=self.solve, width=20, style='My.TButton')
        solve_button.grid(row=2, column=0, pady=10, ipadx=10, ipady=10)

        # Configure the style for the button
        self.root.style = ttk.Style()
        self.root.style.configure('My.TButton', font=('Arial', 16), padding=(5, 5))

        # Center the grid and the button within the window
        self.center_grid_and_button()

    def center_grid_and_button(self):
        # Center the grid frame within the window
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Center the Solve button within the window
        self.root.grid_rowconfigure(1, weight=1)

    def solve(self):
        # Extract user input from the grid cells and validate it
        user_input = ''
        for row in self.grid_cells:
            for cell in row:
                user_input += cell.get()

        test_str = ''.join(set(user_input))
        check = len(test_str) == len(user_input) and len(user_input) == 9
        if not check:
            return

        # The index of the zero in the input grid
        zero_idx = 8 - user_input.find('0')
        # the initial state of the game
        initial_state = (int(user_input), zero_idx, 0)
        # The chosen search technique
        choice = self.choice_var.get()
        # The results from applying this search on the initial state
        results = tuple()

        if choice == 'DFS':
            results = search_results(dfs, initial_state)
        elif choice == 'BFS':
            results = search_results(bfs, initial_state)
        elif choice == 'A* Manhattan':
            results = search_results(a_star_with_manhattan, initial_state)
        elif choice == 'A* Euclidean':
            results = search_results(a_star_with_euclidean, initial_state)

        # Create the result screen and pass the results along with the width and height of the main window
        ResultsScreen(tk.Toplevel(self.root), results)


if __name__ == "__main__":
    gui = tk.Tk()
    app = EightPuzzleGUI(gui)
    gui.mainloop()
