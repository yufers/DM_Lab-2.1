def createSubset(i):
    D = []
    for x in range(0, i):
        D.append('?')

    return D
def getSubset(D, printResult = True):
    n = len(D)
    if printResult:
        print(f"{D} --> ", end="")
    subset = []
    for i in range(0, n):
        if D[n - i - 1] != 0:
            subset.append(i + 1)

    if printResult:
        print(subset)
    return subset
def makeSubsets(i, n, D, R, printResult = True):
    for x in range(0, 2):
        Dx = D.copy()
        Dx[i - 1] = x
        if i == n:
            if printResult:
                getSubset(Dx)
            else:
                R.append(getSubset(Dx, printResult))
        else:
            makeSubsets(i + 1, n, Dx, R, printResult)

if __name__ == "__main__":
    D = createSubset(3)
    R = []
    makeSubsets(1,3, D, R)