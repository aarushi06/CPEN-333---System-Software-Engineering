#student name: Aarushi Mehra
#student number: 82519695

import multiprocessing as mp
import time 
import datetime

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    
    col_numbers_used = set()   #create a set for column numbers used

    for row in puzzle:
        if row[column] not in col_numbers_used:
            valid_col = True     #check for print statement
            col_numbers_used.add(row[column])
        else:
            valid_col = False 
            break                #even one incorrect element should break the loop and invalidate the column
   
    if valid_col == True:
        print('Column ', column, ' valid')
    else:
        print('Column ', column, ' not valid')
 

def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    row_numbers_used = set()            #create a set for numbers used in the row
    
    for col in (puzzle[row]):
        if col not in row_numbers_used:
            valid_row = True             #check for print statement
            row_numbers_used.add(col)
        else:
            valid_row = False 
            break                #even one incorrect element should break the loop and invalidate the row

    if valid_row == True:
        print('Row ', row, ' valid')
    else:
        print('Row ', row, ' not valid')
            

def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """

    mapping_rows = {0:0, 1:0, 2:0, 3:3, 4:3, 5:3, 6:6, 7:6, 8:6}      #dict for mapping rows for manipulation
    mapping_subgrids = {0:0, 1:1, 2:2, 3:0, 4:1, 5:2, 6:0, 7:1, 8:2}  #dict for mapping subgrids for manipulation

    subgrid_used_numbers = set()   #create a set for numbers used in the subgrid
    for row in range(mapping_rows[subgrid], mapping_rows[subgrid]+3):
        for i in range(3):
            if puzzle[row][mapping_subgrids[subgrid] * 3 + i] not in subgrid_used_numbers:
                valid_subgrid = True
                subgrid_used_numbers.add(puzzle[row][mapping_subgrids[subgrid] * 3 + i])
            else:
                valid_subgrid = False
                break                 #break out of the loop when even one element is incorrect to invalidate the subgrid
        else:
            continue
        break
            
    if valid_subgrid == True:
        print('Subgrid ', subgrid, ' valid')
    else:
        print('Subgrid ', subgrid, ' not valid')
        
if __name__ == "__main__":
    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]

    test2 = [ [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ]
            ]
    
    testcase = test1   #modify here for other testcases
    SIZE = 9

    for col in range(SIZE):  #checking all columns
        c = mp.Process(target=checkColumn, args=(testcase, col,))
        c.start()
        c.join()
        
    for row in range(SIZE):  #checking all rows
        r = mp.Process(target=checkRow, args=(testcase, row,))
        r.start()
        c.join()
        
    for subgrid in range(SIZE):   #checking all subgrids
        s = mp.Process(target=checkSubgrid, args=(testcase, subgrid,))
        s.start()    
        c.join()


