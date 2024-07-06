import game_functions as gf

def main():
    grid = gf.initialize_grid()
    gf.print_grid(grid)

    while True:
        move = input("Enter move (w/a/s/d): ").strip().lower()
        if move not in 'wasd' or len(move) != 1:
            print("Invalid move! Please enter one of w/a/s/d.")
            continue

        if move == 'w':
            grid = gf.move_up(grid)
        elif move == 'a':
            grid = gf.move_left(grid)
        elif move == 's':
            grid = gf.move_down(grid)
        elif move == 'd':
            grid = gf.move_right(grid)

        gf.print_grid(grid)

        if gf.check_win(grid):
            print("Congratulations! You've reached 2048!")
            break
        if gf.check_game_over(grid):
            print("Game over! No more valid moves.")
            break

if __name__ == "__main__":
    main()
