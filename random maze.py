import random

ROWS = 25
COLS = 10

class Cell:
    def __init__(self):
        self.visited = False
        self.walls = [True, True, True, True] # UP, RIGHT, DOWN, LEFT

def print_maze(maze):
    for i in range(ROWS):
        for j in range(COLS):
            if maze[i][j].walls[0]: # UP wall
                print("+---", end="")
            else:
                print("+   ", end="")
        print("+")
        for j in range(COLS):
            if maze[i][j].walls[3]: # LEFT wall
                print("|   ", end="")
            else:
                print("    ", end="")
        print("|")
    for j in range(COLS):
        print("+---", end="")
    print("+")

def is_valid_cell(row, col):
    return row >= 0 and row < ROWS and col >= 0 and col < COLS

def remove_wall(maze, row, col, dir):
    if dir == 0: # UP
        maze[row][col].walls[0] = False
        maze[row-1][col].walls[2] = False
    elif dir == 1: # RIGHT
        maze[row][col].walls[1] = False
        maze[row][col+1].walls[3] = False
    elif dir == 2: # DOWN
        maze[row][col].walls[2] = False
        maze[row+1][col].walls[0] = False
    elif dir == 3: # LEFT
        maze[row][col].walls[3] = False
        maze[row][col-1].walls[1] = False

def generate_maze(maze, row, col):
    maze[row][col].visited = True
    directions = [0, 1, 2, 3] # UP, RIGHT, DOWN, LEFT
    random.shuffle(directions)
    for dir in directions:
        next_row = row
        next_col = col
        if dir == 0: # UP
            next_row -= 1
        elif dir == 1: # RIGHT
            next_col += 1
        elif dir == 2: # DOWN
            next_row += 1
        elif dir == 3: # LEFT
            next_col -= 1
        if is_valid_cell(next_row, next_col) and not maze[next_row][next_col].visited:
            remove_wall(maze, row, col, dir)
            generate_maze(maze, next_row, next_col)

maze = [[Cell() for j in range(COLS)] for i in range(ROWS)]
generate_maze(maze, 0, 0)
print_maze(maze)
