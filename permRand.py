import numpy as np
import argparse


def flushArrayToFile(X,fName,sep=""):
    f = open(fName,"w")
    for i in X:
        for j in i:
            f.write(str(j)+sep)
        f.write("\n")
    f.close()

def calcSpread(A,M):
    u, counts = np.unique(A, return_counts=True)
    if len(u)<M:
        return np.max(counts)
    else:
        return np.max(counts) - np.min(counts)


def limitSpread(M,k,N,constCombs,randomSampleSize,tSpread):
    if not hasattr(sampleUnderConstraint,"RND"):
        sampleUnderConstraint.RND=np.random.default_rng()

    X = np.array([sampleUnderConstraint.RND.choice(range(M), (k), replace=False) for x in range(randomSampleSize)])
    for i in X:
        unique = True
        for j in constCombs:
            if len(np.intersect1d(i, j))>1:
                unique = False
        if unique==True:
            if constCombs:
                oldDist   = np.array(constCombs)
                oldSpread = calcSpread(oldDist,M)
                newDist   = np.array(np.append(constCombs,i))
                newSpread = calcSpread(newDist,M)
                print("Old Spread: {} , New Spread: {}  ".format(oldSpread,newSpread),end='')
                if (newSpread<=tSpread):
                     constCombs.append(i)
                print("Progress: {}/{}".format(len(constCombs),N))
            else:
                constCombs.append(i)
            if len(constCombs)==N:
                return True
    return False

def sampleUnderConstraint(M,k,N,constCombs,randomSampleSize):
    if not hasattr(sampleUnderConstraint,"RND"):
        sampleUnderConstraint.RND=np.random.default_rng()

    X = np.array([sampleUnderConstraint.RND.choice(range(M), (k), replace=False) for x in range(randomSampleSize)])
    for i in X:
        unique = True
        for j in constCombs:
            if len(np.intersect1d(i, j))>1:
                unique = False
        if unique==True:
            constCombs.append(i)
            print("Progress: {}/{}".format(len(constCombs),N))
            if len(constCombs)==N:
                return True
            
            
    return False


if __name__ == "__main__":  
    """
    N - Length of List
    k - number of Ones in the list
    M - number of required permutations
    Constraints:
    - A new candidate list should only share one index with all others

    Version 0.1: Random approach
    """

    parser = argparse.ArgumentParser(description='Generate Permutations under the constraint that permutations overlap with maximum a single index')
    parser.add_argument('-M', metavar='M',default=10, type=int,
                    help='Defines the length of the Array')
    parser.add_argument('-N', metavar='N',default=10, type=int,
                    help='Defines the number of permutations')
    parser.add_argument('-k', metavar='k',default=3, type=int,
                    help='Defines how many "ones" occur in the arrays')
    parser.add_argument('-t', metavar='t',default=-1, type=int,
                    help='Set a maximum taget spread')
    parser.add_argument('-maxRounds', metavar='maxR',default=1000, type=int,
                    help='Set number of Cycles to find permutations')
    parser.add_argument('-radomSampleSize', metavar='randS',default=10000, type=int,
                    help='In each cycle, how many random sample candidates should be created?')
    parser.add_argument('-arrOUT', metavar='arrOUT',default="", type=str,
                    help='Filename to save the array of permutations')
    parser.add_argument('-idxOUT', metavar='idxOUT',default="", type=str,
                    help='Filename to save the array of indices')
    args = parser.parse_args()         

    M = args.M
    N = args.N
    k = args.k
    maxRounds = args.maxRounds
    randomSampleSize = args.radomSampleSize
    arrOut = args.arrOUT
    idxOut = args.idxOUT
    tSpread = args.t

    constCombs = [ ]

    if tSpread!=-1:
        for l in range(maxRounds):
            if limitSpread(M, k, N, constCombs, randomSampleSize,tSpread):
                break
    else:
        for l in range(maxRounds):
            if sampleUnderConstraint(M, k, N, constCombs, randomSampleSize):
                break

    if len(constCombs)<N:
        print("WARNING!! We were not able to find enough uniqe lists.")
    
    print("Results: M={}, k ={}, N= {}".format(M,k,N))
    grid  = np.zeros((len(constCombs),M),dtype=np.int8)
    gridCounter = 0 
    for i in constCombs:
        grid[gridCounter,[i]]= 1
        gridCounter+=1
        if gridCounter==grid.shape[0]:
            break    
    
    distribution = np.sum(grid,axis=0)
    print("Min: {} ;Max: {};Spread: {};".format(np.min(distribution),
    np.max(distribution),np.max(distribution)-np.min(distribution)))

    if arrOut:
        flushArrayToFile(grid, arrOut)
        print("Array written to file: {}".format(arrOut),sep="")
    if idxOut:
        flushArrayToFile(np.array(constCombs), idxOut,sep=" ")
        print("Array written to file: {}".format(idxOut))