size = 9

def puzzle(a):
    for i in range(size):
        for j in range(size):
            print(a[i][j], end=" ")
        print()

def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
            
    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def sudoku(grid, row, col):

    if (row == size - 1 and col == size):
        return True
    if col == size:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return sudoku(grid, row, col + 1)
    for num in range(1, size + 1, 1): 
        if solve(grid, row, col, num):
            grid[row][col] = num
            if sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

grid = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

if sudoku(grid, 0, 0):
    puzzle(grid)
