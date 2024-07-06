import random

def initialize_grid():
    grid = [[0]*4 for _ in range(4)]
    add_new_number(grid)
    add_new_number(grid)
    return grid

def add_new_number(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if not empty_cells:
        return
    i, j = random.choice(empty_cells)
    grid[i][j] = 2

def print_grid(grid):
    for row in grid:
        print('\t'.join(str(cell) if cell != 0 else '.' for cell in row))
    print()

def merge_left(grid):
    new_grid = []
    for row in grid:
        new_row = [num for num in row if num != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [num for num in new_row if num != 0]
        new_row += [0] * (4 - len(new_row))
        new_grid.append(new_row)
    return new_grid

def rotate_grid(grid):
    return [list(row) for row in zip(*grid[::-1])]

def move_left(grid):
    new_grid = merge_left(grid)
    if new_grid != grid:
        add_new_number(new_grid)
    return new_grid

def move_right(grid):
    grid = [row[::-1] for row in grid]
    new_grid = merge_left(grid)
    new_grid = [row[::-1] for row in new_grid]
    if new_grid != grid:
        add_new_number(new_grid)
    return new_grid

def move_up(grid):
    grid = rotate_grid(grid)
    grid = rotate_grid(grid)
    grid = rotate_grid(grid)
    new_grid = merge_left(grid)
    new_grid = rotate_grid(new_grid)
    if new_grid != grid:
        add_new_number(new_grid)
    return new_grid

def move_down(grid):
    grid = rotate_grid(grid)
    new_grid = merge_left(grid)
    new_grid = rotate_grid(new_grid)
    new_grid = rotate_grid(new_grid)
    new_grid = rotate_grid(new_grid)
    if new_grid != grid:
        add_new_number(new_grid)
    return new_grid

def check_win(grid):
    return any(2048 in row for row in grid)

def check_game_over(grid):
    if any(0 in row for row in grid):
        return False
    for row in grid:
        for i in range(3):
            if row[i] == row[i + 1]:
                return False
    for col in zip(*grid):
        for i in range(3):
            if col[i] == col[i + 1]:
                return False
    return True
