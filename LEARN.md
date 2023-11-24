# Python version

I used version 3.11 for this project, because it's the fastest version in the running time, but you can use any version of python3.

# Project files description

After cloning the repository on your local machine, you will find two python files (main.py, search.py).

The search.py file contains the used search algorithms in this project.

The main.py file contains test functions to test these algorithms and a display function to display the results on the terminal.

In main.py you will find commented test cases you could try to run them to see their results and to ensure they work correctly.

You could also try your own tests and let me know if something went wrong.

# How to write your own test

The state of the 8-puzzle board could be represented as a 2D matrix on the following form: 

|   |   |   |
|---|---|---|
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |

Also, the state could be represented like this: 0 1 2 3 4 5 6 7 8

The state consists of (the state number representation, the zero-digit position in the number representation of the state, the depth of the state).

So, when you write a test you shall write it on the following form:

`search_test((int that represents the state, the zero position in the number representation of the state, 0)))`
