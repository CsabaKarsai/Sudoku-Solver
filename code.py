#grid1 has one solution
grid1 = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

#grid2 has two solutions
grid2 = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,0,0]
]

#unsolvable, check last row
grid3 = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,7,0,8,0,0,7,9]
]

#prints the sudoku board in a readable format
def print_grid(grid):
    for x in range(0,9):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - -")
        for y in range(0,9):
            if y % 3 == 0 and y != 0:
                print("| ", end="")
            if y == 8:
                print(grid[x][y])
            else:
                print(str(grid[x][y]) + " ", end="")

#checks whether the candidate number could be put at position (x,y)
def check(grid, x, y, candidate):
    if check_row(grid, x, candidate) == False:
        return False
    elif check_column(grid, y, candidate) == False:
        return False
    elif check_block(grid, x, y, candidate) == False:
        return False
    return True

#checks if the row x has a number equal to candidate
def check_row(grid, x, candidate):
    for i in range(9):
        if grid[x][i] == candidate:
            return False

#check if the column y has a number equal to candidate
def check_column(grid, y, candidate):
    for i in range(9):
        if grid[i][y] == candidate:
            return False
        
#checks if the block corresponding to position (x,y) has a number equal to candidate
def check_block(grid, x, y, candidate):
    #compute coordinates (x0,y0) of upper left corner of block corresponding to position (x,y)
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    #check each position in the block
    for i in range(3):
        for j in range(3):
            if grid[x0+i][y0+j] == candidate:
                return False
    
#find an empty cell
def find_empty(grid):
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                return (x, y)
    return None
            
#solve the sudoku using backtracking
def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    x, y = find
    for candidate in range(1,10):
        if check(grid, x, y, candidate):
            grid[x][y] = candidate
            if solve(grid):
                return True
            grid[x][y] = 0
    return False      
    
#final program
def run(grid):
    print("Input:")
    print_grid(grid)
    solvable = solve(grid)
    if solvable:
        print("Solution:")
        print_grid(grid)
    else:
        print("This Sudoku is unsolvable!")

#run the program
run(grid1)
run(grid2)
run(grid3)

"""
#alernative, printing all solutions or nothing if sudoku is unsolvable
def solve2(grid):    
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for candidate in range(1,10):
                    if check(grid, x, y, candidate):
                        grid[x][y] = candidate
                        solve2(grid)
                        grid[x][y] = 0
                return
    print("Solution:")
    print_grid(grid)
   
#run the program
def run2(grid):
    print("Input:")
    print_grid(grid)
    solve2(grid)
"""