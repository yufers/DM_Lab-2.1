def createPermutation(i):
    P = []
    for x in range(0, i):
        P.append('?')

    return P
def makePermutation(i, n, M, P, R, printResult = True):
    for x in M:
        Pc = P.copy()
        Pc[i - 1] = x
        if i == n:
            if printResult:
                print(f"{Pc}")
            else:
                R.append(Pc)
        else:
            makePermutation(i + 1, n, M - {x}, Pc, R, printResult)

if __name__ == "__main__":
    M = set(range(1, 3 + 1))
    P = createPermutation(3)
    R = []
    makePermutation(1, 3, M, P, R)