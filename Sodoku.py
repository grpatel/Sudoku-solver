board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#
def solve(bd):
    find = find_empty(bd)
    #base case indicating solution is found
    if not find:
        return True
    else:
        row, col = find
    #loop through values 1 to 9
    for i in range(1,10):
        #plug in valid num
        if valid(bd, i, (row, col)):
            bd[row][col] = i

            if solve(bd):
                return True
            #if solution does not work, reset cell
            bd[row][col] = 0

    return False

#verify if board is valid
def valid(bd, num, pos):
    # Check row
    for i in range(len(bd[0])):
        #check thr each element in row and ignore position we just entered
        if bd[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bd)):
        if bd[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box, will give values 0, 1, or 2
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    #multiply box (0,1,2) by 3 to get to the correct index in the box 
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bd[i][j] == num and (i,j) != pos:
                return False

    return True
#
def print_board(bd):
    for i in range(len(bd)):
        #horizontal line will be printed after every three rows of the board
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bd[0])):
            #vertical line drawn between col 1 and 2 and col 2 and 3 
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bd[i][j])
            else:
                print(str(bd[i][j]) + " ", end="")

#find empty square/element in sudoku board
def find_empty(bd):
    for i in range(len(bd)):
        for j in range(len(bd[0])):
            if bd[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
solve(board)
print("___________________")
print_board(board)