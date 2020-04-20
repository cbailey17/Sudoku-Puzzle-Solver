

from csp_lib.backtrack_util import (first_unassigned_variable, 
                                    unordered_domain_values,
                                    no_inference, 
                                    mrv, 
                                    lcv,
                                    forward_checking)

def backtracking_search(csp,
                        select_unassigned_variable=mrv,
                        order_domain_values=lcv,
                        inference=forward_checking):
    """backtracking_search
    Given a constraint satisfaction problem (CSP),
    a function handle for selecting variables, 
    a function handle for selecting elements of a domain,
    and a set of inferences, solve the CSP using backtrack search
    """
    
    # See Figure 6.5] of your book for details
    

    def backtrack(assignment):
        """Attempt to backtrack search with current assignment
        Returns None if there is no solution.  Otherwise, the
        csp should be in a goal state.
        """
        # check if goal state has been reached and return result
        if csp.goal_test(assignment): 
            return assignment
        
        # decide which variable to use first using mrv (fail first)
        var = select_unassigned_variable(assignment, csp)
        
        # using lcv decide which value to use first and iterate 
        for val in order_domain_values(var, assignment, csp):      
            # check for consistency and assign the value
            if csp.nconflicts(var, val, assignment) == 0:  
                csp.assign(var, val, assignment)
                removals = csp.suppose(var, val)
               
               # run forward checking inferences 
                inference(csp, var, val, assignment, removals)  
                
                result = backtrack(assignment)
                if result is not None:
                    return result
                # restore the removals after backtrack
                csp.restore(removals)  
                del assignment[var]  # unassign the variable    
        return None
    
    # Call with empty assignments, variables accessed
    # through dynamic scoping (variables in outer
    # scope can be accessed in Python)
    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result
