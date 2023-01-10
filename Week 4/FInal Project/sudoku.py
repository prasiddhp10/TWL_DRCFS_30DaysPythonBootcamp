def is_valid_move(sudoku_grid, row, col, number):
    for x in range(9): 
        if sudoku_grid[row][x] == number:
            return False
    
    for x in range(9): 
        if sudoku_grid[x][col] == number:
            return False

    cor_row = row - row % 3
    cor_col = col - col % 3
    for x in range(3): 
        for y in range(3): 
            if sudoku_grid[cor_row + x] [cor_col+y] == number:
                return False


    return True

def solve(sudoku_grid, row, col):
    
    if col == 9: 
        if row == 8: 
            return True
        row += 1
        col = 0

    if sudoku_grid[row][col] > 0: 
        return solve(sudoku_grid, row, col + 1)

    for num in range(1, 10): 

        if is_valid_move(sudoku_grid, row, col, num): 

            sudoku_grid[row][col] = num

            if solve(sudoku_grid, row, col + 1): 
                return True

            sudoku_grid[row][col] = 0

    return False

sudoku_grid = [[3, 0, 0, 8, 0, 1, 0, 0, 2],
               [2, 0, 1, 0, 3, 0, 6, 0, 4],
               [0, 0, 0, 2, 0, 4, 0, 0, 0],
               [8, 0, 9, 0, 0, 0, 1, 0, 6],
               [0, 6, 0, 0, 0, 0, 0, 5, 0],
               [7, 0, 2, 0, 0, 0, 4, 0, 9],
               [0, 0, 0, 5, 0, 9, 0, 0, 0],
               [9, 0, 4, 0, 8, 0, 7, 0, 5],
               [6, 0, 0, 1, 0, 7, 0, 0, 3],]

if solve(sudoku_grid, 0, 0): 
    for i in range (9): 
        for j in range(9): 
            print(sudoku_grid[i][j], end=" ")
        print()

else: 
    print("No Solution for this suduku")