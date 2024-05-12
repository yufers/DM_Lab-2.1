def createPlacement(i):
    A = []
    for x in range(0, i):
        A.append('?')

    return A
def makePlacement(i, k, M, A, R, printResult = True):
    for x in M:
        Ac = A.copy()
        Ac[i - 1] = x
        if i == k:
            if printResult:
                print(f"{Ac}")
            else:
                R.append(Ac)
        else:
            makePlacement(i + 1, k, M - {x}, Ac, R, printResult)

if __name__ == "__main__":
    M = set(range(1, 4 + 1))
    A = createPlacement(2)
    R = []
    makePlacement(1, 2, M, A, R)