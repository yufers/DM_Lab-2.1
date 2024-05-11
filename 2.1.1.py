def createSubset(i):
    D = []
    for x in range(0, 3):
        D.append('?')

    return D
def printSubset(D):
    n = len(D)
    print(f"{D} --> ", end="")
    subset = []
    for i in range(0, n):
        if D[n - i - 1] != 0:
            subset.append(i + 1)

    print(subset)
def makeSubsets(i, n, D):
    for x in range(0, 2):
        Dx = D.copy()
        Dx[i - 1] = x
        if i == n:
            printSubset(Dx)
        else:
            makeSubsets(i + 1, n, Dx)

D = createSubset(3)
makeSubsets(1,3, D)