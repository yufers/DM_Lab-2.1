def createCombination(i):
    C = []
    for x in range(0, i):
        C.append('?')

    return C
def getSubset(C, printResult = True):
    if printResult:
        print(f"{C}")
    return C
def makeCombination(i, b, k, n, C, R, printResult = True):
    for x in range(b, n - k + i + 1):
        Cx = C.copy()
        Cx[i - 1] = x
        if i == k:
            if printResult:
                getSubset(Cx)
            else:
                R.append(getSubset(Cx, printResult))
        else:
            makeCombination(i + 1, x + 1, k, n, Cx, R, printResult)

if __name__ == "__main__":
    C = createCombination(3)
    R = []
    makeCombination(1,1, 3, 5, C, R)