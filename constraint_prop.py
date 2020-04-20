'''
Constraint propagation
'''
from queue import Queue

def AC3(csp, queue=None, removals=None):
    """AC3 constraint propagation
    """    
    q = Queue()
    # iterate through the sudoku variables
    for var in csp.variables:
        # add all the neighbors for each variable to the queue
        for neighbor in csp.neighbors[var]:
            q.put((var, neighbor))
    
    # pull arc from the queue     
    while not q.empty():
        xixj = q.get()
        xi = xixj[0]
        xj = xixj[1]
        # check if the domain needs revising
        if revise(csp, xi, xj):  
            if not csp.domains[xi]:
                return False
            else:
                # add the neighbor arcs to the queue 
                for xk in csp.neighbors[xi]:  # further reductions 
                    if xk == xj:
                        pass
                    q.put((xk, xi))
    return True
    

# Auxilary functions used for AC3 constraint propogation
    
def revise(csp, xi, xj):
    """ revise function eliminates values from the domain of a variable """
    revised = False
    if xi == None:
        return 
    # Check for domain conflicts with neighbors
    for x in csp.domains[xi]:
        chk = check(csp, xi, xj, x)    
        if not chk:
            # update domains based on constraint satisfaction
            csp.domains[xi] = csp.domains[xi].replace(x,'')
            revised = True 
    return revised


def check(csp, xi, xj, x):
    """ check function iterates through the neighbors of first variable and 
        checks constraints
    """
    for y in csp.domains[xj]:
        if csp.constraints(xi, x, xj, y): # check constraints
            return True
        else:
            continue
    return False