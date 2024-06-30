# -*- coding: utf-8 -*-

def reverse_list(l:list):

    """

    TODO: Reverse a list without using any built in functions

 

    The function should return a sorted list.

    Input l is a list which can contain any type of data.

    """

    return l[::-1]

print(reverse_list([1,'2',3,'4',[1,2,3]]))






from copy import deepcopy
def solve_sudoku(matrix): # suppose the matrix is like : List[List[int]], and the output is like so.
    """

    TODO: Write a programme to solve 9x9 Sudoku matrix.

 

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.

 

    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    """
    matrix = deepcopy(matrix)
    # The list to contain the grid location (i,j) to be filled
    to_fill_list = []
    # row_check_list[i][n] = True means we can fill number n in the row no.i, otherwise we cannot, which is similar for column_check_list and block_check_list
    row_check_list = [[True]*9 for i in range(9)]
    column_check_list = [[True]*9 for i in range(9)]
    block_check_list = [[True]*9 for i in range(9)]
    # In the following loop we detect every elements in the matrix and the above lists are filled.
    for i in range(9):
        for j in range(9):
            tmp_num = matrix[i][j]
            if tmp_num == 0: # suppose 0 means "to be filled" in the matrix
                to_fill_list.append((i,j))
            else:
                row_check_list[i][tmp_num-1] = False
                column_check_list[j][tmp_num-1] = False
                block_check_list[j//3+i//3*3][tmp_num-1]  = False
    
    # The function to check if we can fill num at matrix[row][num]
    def check_val(row,col,num):
        return row_check_list[row][num-1] and column_check_list[col][num-1] and \
        block_check_list[col//3+row//3*3][num-1]
    
    # The function to input num at matrix[row][num] and update the xxx_check_list
    def input_num(row,col,num):
        matrix[row][col] = num
        row_check_list[row][num-1] = False
        column_check_list[col][num-1] = False
        block_check_list[col//3+row//3*3][num-1]  = False
    
    # The function to draw back the modification done by function input_num
    def roll_back(row,col,num):
        matrix[row][col] = 0
        row_check_list[row][num-1] = True
        column_check_list[col][num-1] = True
        block_check_list[col//3+row//3*3][num-1]  = True
    
    '''
    Here we use the idea of recursion and DFS;
    That the return of check_val_recur(n) is True means we can successfully fill grid recorded in to_fill_list[n:]
    Otherwise we fail to do so
    At every grid we try number 1-9 and if we can, we will test if we can fill the rest of grids successfully. Otherwise we roll back.
    '''
    def check_val_recur(index):
        row,col = to_fill_list[index]
        if index  == len(to_fill_list)-1:
            for num in range(1,10):
                if check_val(row,col,num):
                    input_num(row,col,num)
                    return True
            else:
                return False
        else:
            for num in range(1,10):
                if check_val(row,col,num) :
                    input_num(row,col,num)
                    if check_val_recur(index+1):
                        return True
                    else:
                        roll_back(row,col,num)
            else:
                return False
    solve_or_not = check_val_recur(0)
    
    if solve_or_not:
        return matrix
    else:
        return "This sudoku cannot be solved"
# example matrix, number 0  means to be filled.   
matrix_1 = \
[[5, 3, 0, 0, 7, 0, 0, 0, 0], \
 [6, 0, 0, 1, 9, 5, 0, 0, 0], \
 [0, 9, 8, 0, 0, 0, 0, 6, 0], \
 [8, 0, 0, 0, 6, 0, 0, 0, 3], \
 [4, 0, 0, 8, 0, 3, 0, 0, 1], \
 [7, 0, 0, 0, 2, 0, 0, 0, 6], \
 [0, 6, 0, 0, 0, 0, 2, 8, 0], \
 [0, 0, 0, 4, 1, 9, 0, 0, 5], \
 [0, 0, 0, 0, 8, 0, 0, 7, 9]] 

print(solve_sudoku(matrix_1))

# matrix_2 [0][0] cannot be filled
matrix_2 = \
[[0, 2, 3, 4, 5, 6, 7, 8, 9], \
 [1, 0, 0, 1, 9, 5, 0, 0, 0], \
 [0, 9, 8, 0, 0, 0, 0, 6, 0], \
 [8, 0, 0, 0, 6, 0, 0, 0, 3], \
 [4, 0, 0, 8, 0, 3, 0, 0, 1], \
 [7, 0, 0, 0, 2, 0, 0, 0, 6], \
 [0, 6, 0, 0, 0, 0, 2, 8, 0], \
 [0, 0, 0, 4, 1, 9, 0, 0, 5], \
 [0, 0, 0, 0, 8, 0, 0, 7, 0]] 
print(solve_sudoku(matrix_2))
