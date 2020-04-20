
from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import mrv
from backtrack import backtracking_search


for puzzle in [easy1, harder1]:
    s = Sudoku(puzzle)  # construct a Sudoku problem
    
    # display initial state
    print("\nSudoku puzzle initial state")
    s.display(s.infer_assignment()) 

    # run constraint satisfaction arc consistency 
    AC3(s)
    # iterate through variables and add them to puzzle if possible
    for val in s.domains:
        if len(s.domains[val]) == 1:
            s.suppose(val, s.domains[val][0])
    
    # display state after AC3
    print("\nSudoku puzzle state after AC3")
    s.display(s.infer_assignment()) 
    
    # check if goal has been reached by AC3
    if not s.goal_test(s.curr_domains):
        # run backtracking search if domains need work
        solved = backtracking_search(s)
        print("\nSudoku state after AC3 and backtracking search")
        s.display(s.infer_assignment()) 
        
    
        