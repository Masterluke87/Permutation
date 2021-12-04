import numpy as np
from itertools import permutations, combinations

if __name__ == "__main__":
    """
    N - Length of List
    k - number of Ones in the list
    M - number of required permutations
    Constraints:
    - A new candidate list should only share one index with all others

    Version 0.1: Simple approach
    """
    M = 154
    k = 5
    N = 192

    combs = combinations(range(M), k)
    grid  = np.zeros((N,M),dtype=np.int8)

    constCombs = [ ]
    for i in combs:
        unique = True
        for j in constCombs:
            if len(list(set(i).intersection(j)))>1:
                unique = False
        if unique==True:
            constCombs.append(i)
            print(len(constCombs))
        
    print("Running: M={}, k ={}, N= {}".format(M,k,N))
    print("Maximum permutations= {}".format(len(constCombs)))
    
    grid  = np.zeros((N,M),dtype=np.int8)
    gridCounter = 0 
    for i in constCombs:
        grid[gridCounter,[i]]= 1
        gridCounter+=1
        if gridCounter==grid.shape[0]:
            break    
    
    for i in grid:
        print(i)
    
